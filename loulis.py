from flask import request, Response
from flask import Blueprint
from flask import send_from_directory
import os
import json
import datetime
import zipfile
import shutil
import redis
import scrapyd_api

manage_spider = Blueprint('manage_spider', __name__)


# 上传项目保存
@manage_spider.route('/project/new', methods=['POST'])
def add_new_spider():
    try:
        # 读取数据保存上传数据
        spider_name = request.form.get("spider")
        project_name = request.form.get("project")
        if os.path.exists("./project/" + project_name):
            return {
                "result": "fail",
                "info": "such project exists"
            }
        f = request.files["file"]
        if f.filename.find(".zip") < 0:
            return {
                "result": "fail",
                "info": "no need file"
            }
        os.makedirs("./project/" + project_name)
        print(f.filename)
        project_path = "./project/" + project_name
        f.save(project_path + "/" + f.filename)

        # 解压zip文件
        zip_file = zipfile.ZipFile(project_path + "/" + f.filename)
        zip_list = zip_file.namelist()
        for ff in zip_list:
            zip_file.extract(ff, project_path)
        zip_file.close()
        os.remove(project_path + "/" + f.filename)

        # 修改项目下cfg文件
        f = open(project_path + "/" + "scrapy.cfg", 'r')
        content = ""
        for line in f.readlines():
            if line.find("#url") >= 0 or line.find("# url") >= 0:
                content = content + "url = http://localhost:6800/" + "\n"
            else:
                content = content + line
        f.close()
        f = open(project_path + "/" + "scrapy.cfg", 'w')
        f.write(content)
        f.close()

        # 相关数据存入数据库
        r = get_redis()
        data_item = {
            "spider": spider_name,
            "time": "no record",
            "job_id": "no record"
        }
        r.hset("project", project_name, str(data_item))

        return {
            "result": "success",
            "info": "success"
        }
    except Exception as e:
        print(str(e))
        return {
            'result': 'fail',
            "info": str(e)
        }


# 获取当前文件下所有项目
@manage_spider.route('/project/all', methods=['GET'])
def get_all_spider():
    if not os.path.exists("./project"):
        print(os.listdir("./"))
    file_list = os.listdir("./project")
    result = []
    for file in file_list:
        if os.path.isdir("./project/" + file):
            item = {
                "name": file,
                "time": get_last_run_time(file),
                "state": get_project_state(file)
            }
            result.append(item)
    return Response(json.dumps(result), mimetype="application/json")


# 获取项目的输出
@manage_spider.route('/project/output', methods=['GET'])
def get_project_output():
    try:
        file_name = request.args.get('name', '')
        r = get_redis()
        spider_name = eval(r.hget("project", file_name))['spider']
        file_path = "C:/Users/Administrator/logs/" + file_name + "/" + spider_name
        if os.path.exists(file_path):
            f1 = os.listdir(file_path)
            output_path = file_path + "/" + f1[0]
            f = open(output_path, 'r', encoding='UTF-8')
            result = ""
            for i in f.readlines():
                result = result + i
                result + "\n"
            res = {
                'result': "success",
                "info": result
            }
        else:
            res = {
                "result": "fail",
                "info": "输出不存在"
            }

        return Response(json.dumps(res), mimetype="application/json")

    except Exception as e:
        print(str(e))
        return {
            "result": "error",
            "info": str(e)
        }


# 下载项目的输出
@manage_spider.route("/project/output/download", methods=['GET'])
def get_output_url():
    try:
        file_name = request.args.get('name', '')
        r = get_redis()
        spider_name = eval(r.hget("project", file_name))['spider']
        file_path = "C:/Users/Administrator/logs/" + file_name + "/" + spider_name
        log_path = os.listdir(file_path)[0]
        if os.path.exists(file_path + "/" + log_path):
            return send_from_directory(file_path, log_path, as_attachment=True)
        else:
            url_path = "not exist"
            return url_path
    except Exception as e:
        print(str(e))
        return str(e)


# 删除项目
@manage_spider.route("/project/delete", methods=['GET'])
def delete_spider():
    try:
        file_name = request.args.get('name', '')
        scrapyd = scrapyd_api.ScrapydAPI('http://localhost:6800')
        state = get_project_state(file_name)
        if state=='running' or state=='pending':
            return {
                "result":"fail",
                "info":"such project is running or pending"
            }
        file_path = "./project/" + file_name
        if os.path.exists(file_path):
            shutil.rmtree(file_path)
        output_path = "C:/Users/Administrator/logs/" + file_name
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        r = get_redis()
        r.hdel("project",file_name)
        scrapyd.delete_project(file_name)
        if r.hexists("project", file_name):
            r.hdel("project", file_name)
        return {
            "result": "success",
            "info": "success"
        }
    except Exception as e:
        print(str(e))
        return {
            "result": "fail",
            "info": str(e)
        }


# 运行项目
@manage_spider.route("/project/run", methods=['GET'])
def run_project():
    try:
        r = get_redis()
        name = request.args.get('name', '')
        if os.path.exists("./project/" + name):
            info = ""
            state = get_project_state(name)
            if state == "running" or state == "pending":
                return {
                    "result": "fail",
                    "info": "such project is running or pending"
                }
            scrapyd = scrapyd_api.ScrapydAPI('http://localhost:6800')
            project_list = scrapyd.list_projects()
            print(project_list)
            if name in project_list:
                r = get_redis()
                spider_name = eval(r.hget("project", name))['spider']
                info = scrapyd.schedule(name, spider_name)
            else:
                os.chdir("./project/" + name)
                os.system("scrapyd-deploy")
                r = get_redis()
                spider_name = eval(r.hget("project", name))['spider']
                info = scrapyd.schedule(name, spider_name)
                os.chdir("../../")
            save_run_time(name)
            item = eval(r.hget("project", name))
            item['job_id'] = info
            r.hset("project", name, str(item))
            save_run_time(name)
            return {
                "result": 'success',
                "info": "项目成功运行"
            }

        else:
            return {
                "result": "fail",
                "info": "no such project exists"
            }
    except Exception as e:
        if not os.path.exists("./project"):
            os.chdir("../../")
        print(str(e))
        return {
            "result": "error",
            "info": str(e)
        }


# 取消运行项目
@manage_spider.route("/project/cancel", methods=['GET'])
def cancel_project():
    try:
        r = get_redis()
        name = request.args.get('name', '')
        if r.hget("project", name) is None:
            return {
                "result": "fail",
                "info": "such project not exist"
            }
        else:
            job_id = eval(r.hget("project", name))['job_id']
            if job_id is None:
                return {
                    "result": "fail",
                    "info": "such project not exist"
                }
            else:
                scrapyd = scrapyd_api.ScrapydAPI('http://localhost:6800')
                str = scrapyd.cancel(name, job_id)
                return {
                    "result": "success",
                    "info": "job has cancelled from " + str
                }

    except Exception as e:
        print(str(e))
        return {
            "result": "error",
            "info": str(e)
        }


def get_project_state(name):
    try:
        scrapyd = scrapyd_api.ScrapydAPI('http://localhost:6800')
        r = get_redis()
        job_id = eval(r.hget("project", name))['job_id']
        state = scrapyd.job_status(name, job_id)
        return state
    except Exception as e:
        print(str(e))
        return "no record"


def save_run_time(name):
    r = get_redis()
    item = eval(r.hget("project", name))
    current_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
    item['time'] = time_str
    r.hset("project", name, str(item))


def get_last_run_time(name):
    try:
        r = get_redis()
        time = eval(r.hget("project", name))['time']
        if time is None:
            return "no record"
        return time
    except Exception as e:
        print(str(e))
        return "no record"


def get_redis():
    return redis.Redis(host="localhost", port=6379, decode_responses=True)

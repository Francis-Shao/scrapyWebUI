from flask import request, Response
from flask import Blueprint
from flask import send_from_directory
from flask import make_response
from scheduler import performanceOptimization
import subprocess
import os,zipfile
import shutil
import sys
from os.path import join
import json
import re
from flask import jsonify

auto_make = Blueprint('auto_make', __name__)

@auto_make.route('/')
def hello_world():
    return "hello world"

@auto_make.route('/autoMake', methods=['GET','POST'])

def scrapy_auto_make():#自动生成

    if request.method == 'POST':
        json_file_path = saveJson()

        url,scrapy_name,div_list,next_link,item,xpath,item_xpath = getForm(json_file_path)#获取表单数据

        subprocess.check_output(['scrapy', 'startproject', scrapy_name],cwd='./')

        modify_item(scrapy_name,item,item_xpath)#修改item
        modify_spider(scrapy_name,url,div_list,next_link,item,xpath,item_xpath)#修改spider
        performanceOptimization(json_file_path)  # 选择优化

        zipFilePath = os.path.join(sys.path[0],scrapy_name+".zip")
        zipFile = zipfile.ZipFile(zipFilePath,"w",zipfile.ZIP_DEFLATED)
        #absDir = os.path.join(sys.path[0],scrapy_name)
        absDir = auto_make.root_path + "/" + scrapy_name
        writeAllFileToZip(absDir,zipFile)
        zipFile.close()

        shutil.rmtree(absDir)#删除项目
        shutil.move(zipFilePath,auto_make.root_path+"/scrapyproject_zips/"+scrapy_name+".zip")

        return 'success'

    else:
        file_list = os.listdir("./scrapyproject_zips/")
        result = []
        for file in file_list:
            if os.path.isfile("./scrapyproject_zips/" + file):
                item = {
                    "name": file,
                    "time": 1
                }
                result.append(item)
        return Response(json.dumps(result), mimetype="application/json")

def getForm(json_file_path):
    #json_file_path = 'test.json'
    with open(json_file_path) as f:
        jsonStr = json.load(f)

    url = jsonStr["url"]
    #print(jsonStr)
    # url = request.form.get('url')
    #print(url)
    scrapy_name = jsonStr['projectName']
    #scrapy_name = '_' + scrapy_name
    div_list = jsonStr['div_list_xpath']
    next_link = jsonStr['next_link']
    item = jsonStr['item']
    xpath = jsonStr['xpath']
    item_xpath = jsonStr['item_xpath']
    #print(item_xpath)
    return url,scrapy_name,div_list,next_link,item,xpath,item_xpath

def saveJson():
    data = json.loads(request.get_data(as_text=True))
    jsonFilePath = 'option.json'
    with open(jsonFilePath, 'w') as file_obj:
        json.dump(data, file_obj)
    return jsonFilePath

def modify_item(scrapy_name,item,item_xpath):
    src_file = "./" + scrapy_name + "/" + scrapy_name + "/items.py"
    pattern = r"scrapy.Field"
    with open(src_file,"r",encoding='utf-8') as f:
        lines = f.readlines()
    with open(src_file,"w",encoding='utf-8') as f_w:
        for line in lines:
            if(re.search(pattern,line)):
                more_line_list = []
                temp = line
                more_line_list.append(temp)
                line = line.replace('# name',item)
                f_w.write(line)
                for i in range(len(item_xpath)):
                    more_item = item_xpath[i]['item']
                    more_line_list[i] = more_line_list[i].replace('# name',more_item)
                    f_w.write(more_line_list[i])
                    more_line_list.append(temp)
                continue
            f_w.write(line)
    pass
def modify_spider(scrapy_name,url,div_list,next_link,item,xpath,item_xpath):
    src_file, dest_file = "./template.py", "./" + scrapy_name + "/" + scrapy_name + "/spiders/myspider.py"
    #src_file, dest_file = "./tutorial/tutorial/spiders/template.py", "myspider1.py"
    pattern_url = r"start_urls"
    pattern_item = r"template_item"+"\["
    pattern_div_list = r"div_list ="
    pattern_next_link = r"next_link = response"
    pattern_from = r"from"
    pattern_Tutorial = r"Tutorial"
    with open(dest_file, "w", encoding='utf-8') as file_write, \
            open(src_file, 'r', encoding='utf-8') as file_read:
        for file_read_line in file_read:
            if(re.search(pattern_from,file_read_line)):
                file_read_line = file_read_line.replace("tutorial",scrapy_name)
            if(re.search(pattern_Tutorial,file_read_line)):
                file_read_line = file_read_line.replace("Tutorial",scrapy_name.capitalize())

            if (re.search(pattern_url, file_read_line)):
                file_read_line = file_read_line.replace("''", "'" + url + "'")
            if (re.search(pattern_item, file_read_line)):
                add_line_list = []
                temp_line = file_read_line
                add_line_list.append(temp_line)
                file_read_line = file_read_line.replace("''", "'"+item+"'")
                file_read_line = file_read_line.replace('div.xpath("")', 'div.xpath(' +'\"'+xpath+'\"' + ')')
                file_write.write(file_read_line)
                for i in range(len(item_xpath)):
                    more_item = item_xpath[i]['item']
                    more_xpath = item_xpath[i]['xpath']
                    add_line_list[i] = add_line_list[i].replace("''","'"+more_item+"'")
                    add_line_list[i] = add_line_list[i].replace('div.xpath("")', 'div.xpath(' +'\"'+more_xpath+'\"' + ')')
                    file_write.write(add_line_list[i])
                    add_line_list.append(temp_line)
                continue

            if (re.search(pattern_div_list,file_read_line)):
                file_read_line = file_read_line.replace('("")','("'+div_list+'")')
            if(re.search(pattern_next_link,file_read_line)):
                file_read_line = file_read_line.replace('("")','("'+next_link+'")')
            file_write.write(file_read_line)
def modify_settings():
    pass
def modify_middlewares():
    pass
def writeAllFileToZip(absDir,zipFile):
    for f in os.listdir(absDir):
        absFile = os.path.join(absDir, f)  # 子文件的绝对路径
        if os.path.isdir(absFile):  # 判断是文件夹，继续深度读取。
            relFile = absFile[len(os.getcwd()) + 1:]  # 改成相对路径，否则解压zip是/User/xxx开头的文件。
            zipFile.write(relFile)  # 在zip文件中创建文件夹
            writeAllFileToZip(absFile, zipFile)  # 递归操作
        else:  # 判断是普通文件，直接写到zip文件中。
            relFile = absFile[len(os.getcwd()) + 1:]  # 改成相对路径
            zipFile.write(relFile)
    return

@auto_make.route('/download',methods=['GET'])
def download_scrapy():
    file_name = request.args.get('projectName', '')
    res = make_response(send_from_directory(r"./scrapyproject_zips",filename=file_name,as_attachment=True))
    res.headers["Cache-Control"] = "no_store"
    res.headers["max-age"] = 0
    return res




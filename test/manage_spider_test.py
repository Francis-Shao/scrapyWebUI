import os
import json
import unittest
from loulis import manage_spider
from flask import Flask
import shutil
import scrapyd_api
import redis


class hello_world_test(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(manage_spider)
        app.testing = True

        self.client = app.test_client()
        self.file = open("./DistributedSpider-master.zip", "rb")
        self.scrapyd = scrapyd_api.ScrapydAPI('http://localhost:6800')
        if "DistributedSpider" in self.scrapyd.list_projects():
            self.scrapyd.delete_project("DistributedSpiders")
        self.redis=redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
        os.makedirs("./project")

    # def test_hello_word(self):
    #     response = self.client.get("/", data={})
    #     result=bytes.decode(response.data)
    #     file_list=os.listdir("./")
    #     print(file_list)
    #     self.assertEqual(result, "hello world")

    def test_project_upload(self):
        # 上传脚本
        data = {
            "file": self.file,
            "project": "DistributedSpiders",
            "spider": "Dis_Douban"
        }
        response = self.client.post("/project/new", data=data, content_type='multipart/form-data', )
        result = get_dict(response.data)
        self.assertEqual("success", result['result'])
        self.assertTrue(os.path.exists("./project/DistributedSpiders"))


        # 运行脚本
        response = self.client.get("/project/run?name=DistributedSpiders")
        result=get_dict(response.data)
        self.assertEqual(result['result'],"success")
        response = self.client.get("/project/run?name=DistributedSpiders")
        result = get_dict(response.data)
        self.assertEqual(result['info'], "such project is running or pending")
        response = self.client.get("/project/run?name=Distr")
        result = get_dict(response.data)
        self.assertEqual(result['info'], "no such project exists")

        #删除项目
        response=self.client.get("/project/delete?name=DistributedSpiders")
        result=get_dict(response.data)
        self.assertEqual(result['result'],'fail')
        self.assertEqual(result['info'],"such project is running or pending")

        #停止脚本
        response = self.client.get("/project/cancel?name=DistributedSpiders")
        result = get_dict(response.data)
        self.assertEqual(result['result'],"success")
        response=self.client.get("/project/cancel?name=etstdemo")
        result = get_dict(response.data)
        self.assertEqual(result['info'],'such project not exist')

        # 删除项目
        response=self.client.get("/project/delete?name=DistributedSpiders")
        result = get_dict(response.data)
        self.assertEqual(result['result'], 'success')

        #获取所有项目
        response=self.client.get("/project/all")
        project_list=get_dict(response.data)
        self.assertFalse("DistributedSpiders" in project_list)

    def tearDown(self):
        shutil.rmtree("./project")
        #shutil.rmtree("../../logs/DistributedSpiders")

def get_suite():
    suite=unittest.TestSuite()
    suite.addTest(hello_world_test("test_upload_project"))

def get_dict(result):
    result = bytes.decode(result)
    return eval(result)


if __name__ == '__main__':
    unittest.main()

import json

class optimizer:

    def readOptions(self, path):
        with open(path, "r", encoding='utf-8') as f:
            self.optionData = json.loads(f.read())

    def userAgentHandler(self, settingPath, middlewarePath):
        middlewareCodeStr = "\n\nclass RandomUserAgentMiddleware(object):\n" \
                            "\tdef process_request(self,request,spider):\n" \
                            "\t\tua = UserAgent()\n" \
                            "\t\trequest.headers['User-Agent'] = ua.random\n"
        with open(middlewarePath, 'a') as fm:
            fm.write(middlewareCodeStr)
        fm.close()

        settingCodeStr = "DOWNLOADER_MIDDLEWARES = {\n" \
                         "\t'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,\n" \
                         "\t'%s.middlewares.RandomUserAgentMiddleware': 543,\n" \
                         "}\n" % self.optionData['projectName']
        with open(settingPath, 'a') as fs:
            fs.write(settingCodeStr)

        middlewareCodeImportStr = "from fake_useragent import UserAgent\n"
        file = open(middlewarePath, 'r')
        content = file.read()
        pos = content.find("from scrapy import signals")

        if (pos != -1):
            content = content[:pos] + middlewareCodeImportStr + content[pos:]
            file = open(middlewarePath, 'w')
            file.write(content)
            file.close()


    def ipPoolHandler(self, path):

        #use cmd to run scrapy crawl xicidaili_spider

        settingCodeDownloaderStr = "DOWNLOADER_MIDDLEWARES = {\n" \
                                   "\t'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,\n" \
                                   "\t'scrapy_proxies.RandomProxy': 100,\n" \
                                   "\t'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,\n" \
                                   "}\n"

        settingCodeStr = "\nRETRY_TIMES = %d\n" \
                         "RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]\n" \
                         "PROXY_LIST = 'ips.txt'\n" \
                         "PROXY_MODE = 0\n" % self.optionData['delay']

        with open(path, 'a') as fp:
            fp.write(settingCodeDownloaderStr)
            fp.write(settingCodeStr)
        fp.close()


    def userAgentandIpPoolHandler(self, settingPath, middlewarePath):

        # use cmd to run scrapy crawl xicidaili_spider

        middlewareCodeStr = "\n\nclass RandomUserAgentMiddleware(object):\n" \
                            "\tdef process_request(self,request,spider):\n" \
                            "\t\tua = UserAgent()\n" \
                            "\t\trequest.headers['User-Agent'] = ua.random\n"
        with open(middlewarePath, 'a') as fm:
            fm.write(middlewareCodeStr)
        fm.close()

        settingCodeDownloaderStr = "DOWNLOADER_MIDDLEWARES = {\n" \
                                   "\t'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,\n" \
                                   "\t'%s.middlewares.RandomUserAgentMiddleware': 543,\n" \
                                   "\t'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,\n" \
                                   "\t'scrapy_proxies.RandomProxy': 100,\n" \
                                   "\t'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,\n" \
                                   "}\n" % self.optionData['projectName']

        settingCodeStr = "\nRETRY_TIMES = %s\n" \
                         "RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]\n" \
                         "PROXY_LIST = 'C:\iplist\iplist\ips.txt'\n" \
                         "PROXY_MODE = 0\n" % self.optionData['delay']

        with open(settingPath, 'a') as fs:
            fs.write(settingCodeDownloaderStr)
            fs.write(settingCodeStr)
        fs.close()

        middlewareCodeImportStr = "from fake_useragent import UserAgent\n"
        file = open(middlewarePath, 'r')
        content = file.read()
        pos = content.find("from scrapy import signals")

        if (pos != -1):
            content = content[:pos] + middlewareCodeImportStr + content[pos:]
            file = open(middlewarePath, 'w')
            file.write(content)
            file.close()

    def cookieHandler(self,path):
        if self.optionData['cookie'] == True:
            codeStr = "\n\nCOOKIES_ENABLED = True\n\n"
        else:
            codeStr = "\n\nCOOKIES_ENABLED = False\n\n"
        with open(path, 'a') as fp:
            fp.write(codeStr)
        fp.close()

    def robotHandler(self, path):
        file = open(path, 'r')
        content = file.read()
        pos_before = content.find("# Obey robots.txt rules")
        pos_after = content.find("# Configure maximum concurrent requests performed by Scrapy")

        if self.optionData['robot'] == True:
            return
        else:
            addCodeStr = "\nROBOTSTXT_OBEY = False\n\n"

        if (pos_before != -1) and (pos_after != -1):
            content = content[:pos_before] + addCodeStr + content[pos_after:]
            file = open(path, 'w')
            file.write(content)
            file.close()

    def bloomHandler(self, path):
        bloomCodeStr = "\nSCHEDULER = \"bloom_filter_buaasee.scheduler.Scheduler\"\n" \
                       "DUPEFILTER_CLASS = \"bloom_filter_buaasee.dupefilter.RFPDupeFilter\"\n" \
                       "USE_BLOOM = True\n" \
                       "ITEM_PIPELINES = {\n" \
                       "\t'bloom_filter_buaasee.pipelines.RedisPipeline': 300 ,\n" \
                       "}\n" \
                       "REDIS_HOST = 'localhost'\n" \
                       "REDIS_PORT = 6379\n" \
                       "BLOOMFILTER_BIT = 30\n" \
                       "SCHEDULER_FLUSH_ON_START = False\n"
        with open(path, 'a') as fm:
            fm.write(bloomCodeStr)
        fm.close()

    def cfgHandler(self, path):
        cfgStr = "[settings]\n" \
                 "default = %s.settings\n\n" \
                 "[deploy]\n" \
                 "url = http://localhost:6800/\n" \
                 "project = %s\n#spiderName = %s\n"% (self.optionData['projectName'],self.optionData['projectName'] ,self.optionData['projectName'])

        file = open(path, 'w')
        file.write(cfgStr)
        file.close()
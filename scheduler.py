import optimizer

def performanceOptimization(jsonFilePath):

    opt = optimizer.optimizer
    opt.readOptions(opt, jsonFilePath)

    print(opt.optionData)

    settingFilePath = "./" + opt.optionData['projectName'] + "/" + opt.optionData['projectName'] + "/settings.py"
    middlewareFilePath = "./" + opt.optionData['projectName'] + "/" + opt.optionData['projectName'] + "/middlewares.py"
    cfgFilePath = "./" + opt.optionData['projectName'] + "/" + "scrapy.cfg"

    opt.robotHandler(opt, settingFilePath)
    opt.cookieHandler(opt, settingFilePath)
    if (opt.optionData['userAgent'] == True) and (opt.optionData['ipPool'] == True):
        opt.userAgentandIpPoolHandler(opt, settingFilePath, middlewareFilePath)
    elif (opt.optionData['userAgent'] != True) and (opt.optionData['ipPool'] == True):
        opt.ipPoolHandler(opt, settingFilePath)
    elif (opt.optionData['userAgent'] == True) and (opt.optionData['ipPool'] != True):
        opt.userAgentHandler(opt, settingFilePath, middlewareFilePath)
    if opt.optionData['bloom'] == True:
        opt.bloomHandler(opt, settingFilePath)

    opt.cfgHandler(opt, cfgFilePath)

#performanceOptimization("option.json")


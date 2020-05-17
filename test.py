import database_manage
import os
import redis
import scrapyd_api
import zipfile

if __name__ == '__main__':
    zip_file = zipfile.ZipFile("./t1.zip")
    zip_list = zip_file.namelist()
    for ff in zip_list:
        print(ff)
    zip_file.close()

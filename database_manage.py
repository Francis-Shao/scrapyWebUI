import pymongo


class mongo(object):

    def __init__(self, address, port, data, table):

        self.database_address = address
        self.port = port
        self.database = data
        self.table = table

    def save_output(self, name, output):

        try:
            client = pymongo.MongoClient(self.database_address, self.port)

            dblist = client.list_database_names()
            if self.database in dblist:
                current_database = client[self.database]
                table = current_database[self.table]
                data = {
                    "name": name,
                    "output": output
                }
                id = table.insert_one(data)
                return {
                    "result": "success",
                    "info": "insert success"
                }

            else:
                return {
                    "result": "fail",
                    "info": "no such database exist"
                }

        except:
            return {
                "result": "error",
                "info": "unknown error"
            }

    def get_output(self, name):
        try:
            client = pymongo.MongoClient(self.database_address, self.port)

            dblist = client.list_database_names()
            if self.database in dblist:
                current_database = client[self.database]
                table = current_database[self.table]
                myquery = {
                    "name": name
                }
                result = table.find(myquery).sort("_id",-1).limit(1)
                return {
                    "result": "success",
                    "info": result[0]['output']
                }

        except Exception as e:
            print(str(e))
            return {
                "result": "error",
                "info": "unknown error"
            }

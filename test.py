import database_manage
import os
import redis
import scrapyd_api

if __name__ == '__main__':
    pass
    # # scrapyd=scrapyd_api.ScrapydAPI("http://121.199.12.225:6800")
    # # scrapyd.list_projects()
    r=redis.Redis(host="121.199.12.225", port=6379, decode_responses=True)
    r.hgetall("project")

from NetEase import NetEase_Crawler 
from NetEase import NetEase_Mongodb 
import json

def read_fromJson(path):
    with open(path, 'r') as f:
        data = json.load(f)
        f.close()
        return data

def main():
    database = NetEase_Mongodb.Database()         # 创建一个MongoDBClient的instance
    database.start()                              # 使用刚刚创建的instance连接database
    # result = NetEase_Crawler.craw(505508015)    # 爬取用户界面，解析并返回字典结果
    result = read_fromJson("../src/user/export.json") # 这里暂时用本地数据代替
    database.dump_user(result, 505508015)         # 把爬到的内容存进数据库
    NetEase_Crawler.__driver__.quit()             # 退出浏览器
    return

if __name__ == "__main__":
    main()


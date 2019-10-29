import pymongo

def mongodb_connect():
    myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    return myclient
def get_china_list():
    # 获取地域字典
    myclient = mongodb_connect()
    twodb = myclient['two']
    china = twodb["china"]
    china_list = china.find({'Id': {'$regex': '^13'}}, {'Name': 1, '_id': 0})
    # 地区列表
    #  data = self.collection.find({'catch_time': re.compile(start_date)})
    #  data = self.collection.find({'catch_time': {'$regex': catch_date}})
    # china_list = china.find({'Id':re.compile('13')}, {'Name':1, '_id':0})
    return china_list
def get_hospital_name_list():
    # 医院列表
    myclient = mongodb_connect()
    twodb = myclient['two']
    hospital_colection = twodb["hospital"]
    hospital_name_list = hospital_colection.find({}, {'departname': 1, 'departid': 1, '_id': 0})
    return hospital_name_list
def update_hospital_city(h_name,city):
    myclient = mongodb_connect()
    twodb = myclient['two']
    hospital_colection = twodb["hospital"]
    result = hospital_colection.update_one({'departname':h_name},{'$set':{'citys':city}})
# encoding=utf-8
import db_connect as dbc
import py_jieba as jb
import difflib
import re

def string_similar(s1, s2):
    # 文本匹配度
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
# 医院列表
hospital_name_list = dbc.get_hospital_name_list()
hospital_name = []
for hospital in hospital_name_list:
    hospital_dict = dict.fromkeys(hospital['departid'], hospital['departname'])
    hospital_name.append(hospital['departname'])
china_list = dbc.get_china_list()
china_name = []
for china in china_list:
    #print(china['Name'])
    china_name.append(china['Name'])
#print(china_list[1]['Name'])
for h_name in hospital_name:
    seg_list = jb.jieba_analyse(h_name)
    city=''
    for name in china_name:
        for seg in seg_list:
            ppd = string_similar(name, seg)
            if  ppd >= 0.8:
                # print(h_name+"-->"+seg+"=="+name+":"+str(ppd))
                city = city + f"{name}"
    result = dbc.update_hospital_city(h_name,city)
    print(h_name+":"+city)






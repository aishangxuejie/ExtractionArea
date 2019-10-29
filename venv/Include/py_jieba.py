# encoding=utf-8
import jieba
import jieba.analyse
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

# 停用词
def jieba_analyse(h_name):
    jieba.analyse.set_stop_words("D:/PycharmProjects/ExtractionArea/venv/Include/stop_words.txt")
    seg_list = jieba.analyse.extract_tags(h_name)
    # print(", ".join(seg_list))
    return seg_list
# jieba_analyse("唐山曹妃甸唐海中医医院")
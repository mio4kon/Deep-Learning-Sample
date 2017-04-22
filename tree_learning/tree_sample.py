# -*- coding:utf-8 -*-
__author__ = 'mio'

from  sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from utils.common import CommonUtils

trainingData = open(r'./test.csv')
reader = csv.reader(trainingData)

# print(headers)

headers = next(reader)
feature_list = []
label_list = []

# 构建特征向量和label向量
for row in reader:
    print(row)
    label_list.append(row[len(row) - 1])
    # 每一个特征向量
    row_dict = {}
    for i in range(0, len(row) - 1):
        row_dict[headers[i]] = row[i]
    feature_list.append(row_dict)

print(label_list)
print(feature_list)

# 转换特征向量为 -> [0,1,0,...]
vec = DictVectorizer()
dummyX = vec.fit_transform(feature_list).toarray()
print(dummyX)
print(vec.get_feature_names())

# 转换label向量
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(label_list)
print(dummyY)

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(dummyX, dummyY)
print('clf :' + str(clf))

with open("./test.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f, feature_names=vec.get_feature_names())

CommonUtils.dot_to_pdf_graphviz('./test.dot', './test.pdf')

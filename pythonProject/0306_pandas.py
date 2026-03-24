# -*- coding: gbk -*-
import numpy
import pandas as pd
import matplotlib.pyplot as plt
# data=pd.read_csv("C:\\Users\\Windows\\PycharmProjects\\pythonProject\\1960-2019全球GDP数据.csv",encoding='gbk')
# # print(data)
# china_gdp=data[data.country=="中国"]
# # print(china_gdp)
# jopan_gdp=data[data.country=="日本"]
# us_gdp=data[data.country=="美国"]
# china_gdp=china_gdp.set_index("year")
# jopan_gdp=jopan_gdp.set_index("year")
# us_gdp=us_gdp.set_index("year")
#
# china_gdp.rename(columns={'GDP':'CN'},inplace=True)
# jopan_gdp.rename(columns={'GDP':'JP'},inplace=True)
# us_gdp.rename(columns={'GDP':'US'},inplace=True)
#
# china_gdp.CN.plot(legend=True)
# us_gdp.US.plot(legend=True)
# jopan_gdp.JP.plot(legend=True)
#
# plt.show()


#创建Series对象
# s1=pd.Series([1,2,3,4])
# print(s1)
# s2=pd.Series([1,2,3,4],index=['A','B','C','D'])
# print(s2)
# tst=(1,2,3,4,5,6)
# s3=pd.Series(tst)
# print(s3)
# dict={'A':1,'B':2,'C':3,'D':4}
# s4=pd.Series(dict)
# print(s4)
# s5=pd.Series(numpy.arange(10))
# print(s5)
# s6=pd.Series([i for i in range(6)],index=[i for i in 'ABCDEF'])
# print(s6)
# print(s6.index)
# print(s6.values)
# print(s6['A'])

#创建DataFrame对象 DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引
#字典
# df1_data={'日期':['08-21','08-22','08-23'],
#           '温度':[25,26,30],
#           '湿度':[81,50,33]
# }
# df1=pd.DataFrame(data=df1_data)
# print(df1)

#元组
# df2_data=[('08-21',25,81),
#           ('08-22',26,50),
#           ('08-23',30,33)]
# df2=pd.DataFrame(df2_data,columns=['日期','温度','适度'],index=['row_1','row_2','row_3'])
# print(df2)
#用numpy创建df
# df3=pd.DataFrame(numpy.random.randn(4,3))
# print(df3)
# score = numpy.random.randint(40, 100, (10, 5))
# print(score)
# score_df=pd.DataFrame(score)#给列表增加行列索引
# print(score_df)
# subjects=["语文","数学","英语","政治","体育"]
# stu=['同学'+str(i) for i in range(score_df.shape[0])]
# data=pd.DataFrame(score,columns=subjects,index=stu)#增加列索引subjects,增加行索引stu
# print(data)

#DataFrame对象属性
# print(data.shape)#(10,5)
# print(data.index)#行索引表
# print(data.columns)#列索引表
# print(data.values)#获取表的所有值
# print(data.T)#转置

#DataFrame的对象方法
# print(data.head())#打印前5行，默认是前5
# print(data.tail())#打印后5行，默认是后5

#DataFrame索引的设置
# stu=["学生_"+str(i) for i in range (score_df.shape[0])]
# data.index=stu#data的行索引全部修改成stu
# print(data)
# data=data.reset_index()#drop默认为False为不删除原来的索引，新建一个索引值
# print(data)
# data=data.reset_index(drop=True)#drop为True为删除原来的索引值，新建一个索引
# print(data)

#set_index(keys,drop=True)
# df = pd.DataFrame({'month': [1, 4, 7, 10],
#                     'year': [2012, 2014, 2013, 2014],
#                     'sale':[55, 40, 84, 31]})
# print(df)
# print(df.set_index('month'))#以月份作为索引
# df=df.set_index(['year','month'])#多个索引
# print(df)

#Pandas的数据类型

# print(df.dtypes)#打印每一列的索引和数据类型
# print(df.info())#打印的更全面，还包括是否有空值 有多少个

#datetime类型
# dates=pd.to_datetime(['2024-09-01','2024-09-02','2024-09-03'])
# print(dates)
# start_date=pd.to_datetime('2024-09-01')
# end_date=pd.to_datetime('2024-09-05')
# dt=end_date-start_date
# print(dt)

#category类型
# 常用于有限集合中的数据类型，优点：占用内存少，对分类数据的操作更快
# categories=pd.Series(['apple','banana','apple','orange'])
# print(categories)

#Pandas基本数据操作
# data=pd.read_csv("stock_day.csv")
# print(data)
# data=data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"],axis=1) #删除列 axis=0则删除行
# print(data)
#索引操作
# print(data['open']['2018-02-27'])#dataframe的索引是先列后行
#loc和iloc使用索引
# print(data.loc['2018-02-27':'2018-02-11','open'])
# print(data.iloc[:3,:5])#前3天，前5列的数据
#赋值操作
# data['close']=1#或data.close=1:把close列的值改成1 若没有close列则新增一个列
# print(data)
#排序操作，DataFrame
# data.sort_values(by=,ascending=)
# by指定排序的键 ascending默认升序 False降序，True升序
# data=data.sort_values(by='open',ascending=True).head()
# print(data)
# data=data.sort_values(by=['open','high'])#按照多个键进行排序，先排open再排high
# print(data)
# data=data.sort_index()#按照索引（日期）从小到大排序
# print(data)

#Series排序
# df1=data['p_change'].sort_values(ascending=True).head()#只排p_change列
# print(df1)
# df2=data['p_change'].sort_index(ascending=True).head()
# print(df2)

#DataFrame运算
#算法运算
# print(data['open'].add(100))#加
# print(data['open'].sub(100))#减
#逻辑运算符
# print(data['open']>23)#返回的是True or False
# print(data[data['open']>23])#会输出筛选完后的行
# print(data[(data['open']<24 )& (data['open']>23)])#完成多个逻辑判断
# print(data.query('open>23&open<24'))#结果同上，查询判断
# print(data[data['open'].isin([23.53,23.85])])#查询open值为23.53和23.85的行

#统计运算
# print(data.describe())#打印统计结果：如count mean std min max等
# print(data.max())#返回最大的值
# print(data.idxmax())#返回最大值的索引
#累计统计函数
# print(data['p_change'].cummax())#当前行累计的最大值
# print(data['p_change'].cumsum())#当前行的累加值
# data['p_change'].cumsum().plot()#插入趋势图
# plt.show()

#apply自定义运算
# df3=data[['open','close']].apply(lambda x:x.max()-x.min(),axis=0)#计算open和close列的最大值减最小值
# print(df3)

#文件读取

#CSV
#pd.read_csv(filepath_or_buffer,sep=',',usecols)
#filepath_of_buffer:文件路径
#sep:分隔符 默认用","隔开
#usecols：指定读取的列名，列表形式

# data = pd.read_csv("stock_day.csv", usecols=['open', 'close'])#读
# data[:10].to_csv("test.csv",columns=['open'])#写
# df1=pd.read_csv("test.csv")
# print(df1)


#DataFrame数据的增删改查操作
#增加列
# df=pd.read_csv("1960-2019全球GDP数据.csv",encoding='gbk')
# df2=df.head()
# df3=df2.copy()
# df3['col1']=33
# df3['col2']=[1,2,3,4,5]
# df3['col3']=df3.year*2
# print(df3)
# df2=df2.assign(new0=66)
# df2=df2.assign(new1=[1,2,3,4,5])
# s=pd.Series([6,7,8,9,10])
# df2=df2.assign(new2=s)
# df2=df2.assign(new3=df2.year+df2.GDP)
# print(df2)
#定义函数必须接受一个参数，该参数为df对象
# def foo(df):
#     ret=df.index.values
#     return ret
# df2.assign(new4=foo)

# movie=pd.read_csv("movie.csv",encoding='utf-8')
# print(movie.isnull())
# print(movie.notnull())
# print(movie.isnull().sum())#查看每个列的缺失值个数
# print(movie.notnull().sum())#查看每个列非缺失值的个数


#数据合并
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                         'key2': ['K0', 'K1', 'K0', 'K1'],
#                         'A': ['A0', 'A1', 'A2', 'A3'],
#                         'B': ['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                         'key2': ['K0', 'K0', 'K0', 'K0'],
#                         'C': ['C0', 'C1', 'C2', 'C3'],
#                         'D': ['D0', 'D1', 'D2', 'D3']})
# df3 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                         'key2': ['K0', 'K0', 'K0', 'K0'],
#                         'E': ['E0', 'E1', 'E2', 'E3'],
#                         'F': ['F0', 'F1', 'F2', 'F3']},index=[10, 11, 12, 13])
#
# print(pd.concat([left,right],axis=1))

#数据分组

df=pd.read_csv("uniqlo.csv")
# gs=df.groupby(['gender_group'])
# print(gs.groups.keys())#查看所有组名
# print(gs.groups)# 查看每个分组对应的行索引
# print(gs.size())#查看每个组的行数
df_gb=df.groupby('gender_group')
# print(df_gb.get_group('Female'))
gs2 = df.groupby(['gender_group', 'city'])
# print(gs2.first())#打印每组第一条数据
# print(gs2.last())#打印每组最后一天数据
gs2 = df.groupby(['gender_group', 'channel'])
print(gs2.get_group(('Female', '线上')))
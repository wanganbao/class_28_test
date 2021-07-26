# 索引
# str_1='classmeat'
# print(str_1[0])
# print(str_1[5])
# print(str_1[-3])
# num_1=0
# while num_1<len(str_1):
#     print(str_1[num_1],end=' ')
#     num_1+=1
# print(len(str_1))

# 切片/分片
# print(str_1[1:-1])#左闭右开
# print(str_1[-1::-2])#步长为负数，反向切片----右闭左开

# list--列表
b=['1','2','3','wang','wang',345,346]
# a=list('1234')#转换--字符串转列表
# print(a,type(a))
# print(b,type(b))
# # c=(b[3])
# # print(c[1])
# print(b[3][1:3])#对列表中的元素切片
# print(b.count('wang'))#统计元素出现次数
print(b.index('wang',0))#获取元素的索引位置，左闭右开
# b.append('lili')#追加
# print(b)
# b.insert(3,'cc')#指定位置添加元素，索引位置前面添加
# print(b)
# b.extend(a)#合并列表

# d=['1','2','3','wang',['wang','xc'],345,346]
# print(d.pop())#默认删除最后一个元素，并返回
# print(d)
# print(d.remove('d'))#删除指定元素
# print(d)

# del d#删除列表
# del d[4]
# del d[4:]
# d.clear()#清空列表

# d[0]='xiaohao'
# d[1]=['dabao','xiaobao']
# d[3:5]=list('1234')
# d[1][1]='100'

# str_1='xc'
# print(str_1 in d[-3])
# print(d)

# list_1=['1','2','3','wang','wang',345,346]
# list_3=['1','23','A','a','345','2345']
# list_2=[12,34,57]#两个列表相加获得新的列表
# print(list_1+list_2)
# list_1.reverse()#列表倒序
# print(list_1)

# list_2.sort(reverse=False)#正序
# list_2.sort(reverse=True)#倒序
# list_3.sort()#默认根据元素长度排序
# list_3.sort(reverse=False,key=ascii)
# print(list_2)
# print(list_1)
# print(list_3)
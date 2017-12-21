#txt在线文档下载
from urllib import request
response = request.urlopen(r'http://python.org/')#HTTPResponse类型
print(type(response))
page = response.read()
print(type(page))
page = page.decode('utf-8')
#上面两个语句可简化
#page = response.read().decode('utf-8')
print(type(page))
print(len(page))
print(page[:14])
print(page[:15])

# This is my shopping list 列表例子
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

#元组例子
zoo = ('python', 'elephant', 'penguin')#元组
zoo1 = ['python', 'elephant', 'penguin']#列表
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
len(new_zoo)-1+len(new_zoo[2]))
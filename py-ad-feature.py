#################################### 五、高级特性 #############################################

print('#################################### 1、切片 #############################################')

## 1、切片（slice）
# 对这种经常取指定索引范围的操作，Python提供了切片（Slice）操作符

list1 = ['paul', 'jack', 'rose', 'danny', 'candy']

# 从index 0开始，取到index 3的前一位
print(list1[0:3])
print(list1[1:3])

# 如果第一个索引是0，可以忽略
print(list1[:3])

# 切片支持倒数，list[-n:] 表示从后往前取n位
print(list1[-1:])
print(list1[-2:])

list2 = list(range(0, 100))
print(list2)

# 取前10
print(list2[:10])

# 取后10
print(list2[-10:])

# 取10-20之间
print(list2[11:20])

# 0-10每两个数取一个
print(list2[:10:2]) # [0, 2, 4, 6, 8]

# list2 中所有数据，每隔5个数取一个
print(list2[::5])

## 切片操作同样适用 str 和 tuple

## 利用 slice 实现一个 trim

# 循环实现
def trim(origin_str):
    start_index = 0
    for s in origin_str:
        if s != ' ':
            break
        start_index += 1

    end_str = len(origin_str)
    for s in origin_str:
        if s != ' ':
            break
        end_str -= 1

    print(start_index)
    print(end_str)
    print(origin_str[start_index:end_str + 1])

str_ipt = '   123  '
trim(str_ipt)

# 递归实现
def trim2(org_str):
    if org_str[:1] == ' ': # 处理前面的空格
        return trim2(org_str[1:])
    elif org_str[-1:] == ' ': # 处理后面的空格
        return trim2(org_str[:-1])
    else:
        return org_str

print(len(str_ipt), trim2(str_ipt), len(trim2(str_ipt)))

print('#################################### 2、迭代（Iterable） #############################################')

## 2、迭代（Iterable）
# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

# dict 类型迭代
dict_iterable = {
    'k1': 'v1',
    'k2': True,
    'k3': 100
}

for key in dict_iterable:
    print(key)

for val in dict_iterable.values():
    print(val)


# 判断一个对象是否为可迭代对象


## 3、列表生成式（range）

## 4、生成器

## 5、迭代器
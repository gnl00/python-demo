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
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3,], Iterable))
print(isinstance((1,2,3,), Iterable))


# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(li):
    if li == []:
        return None, None
    min = max = li[0]
    for i in li:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

print(findMinAndMax([5, 0, 45, 3, -2, 9]))

## 3、列表生成式（range()）
# 列表生成式即 List Comprehensions，是 Python 内置的非常简单却强大的可以用来创建 list 的生成式。

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 1、常规做法
list3 = []

for i in range(1, 11):
    list3.append(i * i)
print(list3)

# 2、列表生成式
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
list4 = [x * x for x in range(1, 11)]
print(list4)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
list5 = [x * x for x in range(1, 11) if x %2 == 0]
print(list5)

# 使用两层循环，可以生成全排列
list6 = [m + n for m in 'ABC' for n in 'XYZ']
print(list6)

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
file_dir_list = [d for d in os.listdir('.')]
print(file_dir_list)

# 在列表生成式中使用方法，如 lower()
list7_tmp = ['Hello', 'World', 'Python']
list7 = [s.lower() for s in list7_tmp]
print(list7)

# 带if-else的列表生成式必须将if-else放在for循环之前
[x if x % 2 == 0 else -x for x in range(1, 11)] # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]


# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# 使用内建的isinstance函数可以判断一个变量是不是字符串，请通过添加if语句保证列表生成式能正确地执行
def list_str_to_lowercase(li):
    if li == []:
        return None
    return [s.lower() for s in li if isinstance(s, str)]

list8 = ['Apple', 100, True, 'banana', 'Lemon']
print(list_str_to_lowercase(list8))

## 4、生成器（generator）
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值

for i in g:
    print(i)


# 生成一个 n 位的 fibonacci 数列
# 1, 1, 2, 3, 5, 8, 13
def gen_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1

gen_fib(6)

# 仔细观察，可以看出，gen_fib 函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似 generator
# 上面的函数和 generator 仅一步之遥。要把 gen_fib 函数变成 generator 函数，只需要把 print(b) 改为 yield b 就可以了

# 这就是定义generator的另一种方法
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，
# 调用一个generator函数将返回一个generator
# 注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator
def gen_fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

print(gen_fib2(8))  # <generator object gen_fib2 at 0x0000028E0CC1A6C0>

for i in gen_fib2(8):
    print(i)

gen_tmp = gen_fib2(8)
while True:
    try:
        x = next(gen_tmp)
        print('gen_tmp: ', x)
    except StopIteration as e:
        print(e.value)
        break

# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就结束。
# 而 generator 的函数，在每次调用 next() 的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

print(odd())
for o in odd():
    print(o)

# 使用迭代器输出杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 输出n行的杨辉三角
# l1 = [1]
# l2 = [1,1]
# l3 = [1,2,1]
# l4 = [1,3,3,1]

def triangles(max):
    n = 0
    L = [1]
    while n < max:
        yield L
        X = [0] + L
        Y = L + [0]
        L = [X[i] + Y[i] for i in range(len(X))]
        n += 1
    

t = triangles(6)
for i in t:
    print(i)


## 5、迭代器

# 使用isinstance()判断一个对象是否是Iterable对象/判断某对象是否可迭代
from collections.abc import Iterable

print(isinstance([], Iterable))

# ist、dict、str虽然是Iterable，却不是Iterator，把list、dict、str等Iterable变成Iterator可以使用iter()函数
# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
# Python的for循环本质上就是通过不断调用next()函数实现的
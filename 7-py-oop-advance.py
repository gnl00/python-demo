#################################### 九、面向对象高级编程 #############################################


class Student(object):
    pass

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
stu = Student()

# 1、尝试给实例绑定一个属性（动态给实例绑定一个属性）
stu.name = 'Alan'
print(stu.name)

# 2、给实例绑定一个方法
def set_name(self, name):
    self.name = name

from types import FunctionType, MethodType
stu.set_name = MethodType(set_name, stu)

stu.set_name('Brown')
print(stu.name)

# 给一个实例绑定的属性和方法，对另一个实例是不起作用的

stu2 = Student()
# print(stu2.name) # has no attribute 'name'
# stu2.set_name('CC') # has no attribute 'set_name'


# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

stu3 = Student()
stu3.set_score(95)
print(stu3.score)

stu2.set_score(88)
print(stu2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

# 但是，如果我们想要限制实例的属性怎么办？
# 比如，只允许对Student实例添加name和age属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

## __slot__
## 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
## 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Teacher(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')

tea = Teacher()
tea.name = 'Danne'
tea.age = 40
print(tea.name)
print(tea.age)

# 由于 gender 没有被放到__slots__中，所以不能绑定 gender 属性，试图绑定 gender 将抛出 AttributeError 错误
# tea.gender = 'male'
# print(tea.gender)


## 2、@property

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
# 但是没办法检查参数，导致实例可以把对内部属性随便改，这显然不合逻辑

# 比如 score 属性，为了限制 score 的范围，
# 可以通过一个set_score()方法来设置成绩，就可以检查参数
# 再通过一个get_score()来获取成绩

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student1(object):

    # 把一个getter方法变成属性，只需要加上@property就可以
    # 注意：属性的方法名不要和实例变量重名
    @property
    def score(self):
        return self._score

    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError('score must be numeric')
        elif score < 0 or score > 100:
            raise ValueError('socre must between 0-100')
        else:
            self._score = score

    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    @property
    def isPass(self):
        return self._score > 60


s1 = Student1()
s1.score = 53 # 实际转化为s.set_score(60)
print(s1.score) # 实际转化为s.get_score()
print(s1.isPass)





## 3、多重继承

class Animal(object):
    def move(self):
        print('animal can move')

    def eat(self):
        print('animal need to eat something')

class Flyable(object):

    def fly(self):
        print('i can fly')


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
class Bird(Animal, Flyable):
    def eat(self):
        print('rewrite eat method by myself')


bird = Bird()
bird.move()
bird.fly()
bird.eat()

## MixIn
# MixIn的目的就是给一个类增加多个功能，
# 在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系

# Python自带的很多库也使用了MixIn。
# 举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
# 而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。


## 4、定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的

# __str__
class Person(object):
    
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # 打印一个 Person 实例，会输出其内存地址如：<__main__.Person object at 0x000001E98035D8B0>
    # 怎么才能打印得好看呢？
    # 只需要定义好__str__()方法，返回一个自定义的字符串就可以
    # 这样打印出来的实例，结构清晰，而且容易看出实例内部重要的数据
    def __str__(self):
        return 'Object Person(name: %s)' % (self._name)

    __repr__ = __str__

p1 = Person('AAA')
print(p1.name)

print(p1) # Object Person(name: AAA)

# 自定义 __str()__ 使用print输出是正常的
# 但是使用命令行直接敲变量不用print，打印出来的实例还是输出内存地址
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的（输出控制台内容的）
# 解决方法是简单的，一般来说__repr()__ 方法的内容和__str()__是一样的
# 所以，可以直接在类内部进行 __repr__ == __str__ 这一操作



# __iter()__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
    def __init__(self, count):
        # 初始化两个计数器a, b
        self.a, self.b = 0, 1
        self.count = count

    def __iter__(self):
        return self
    
    def __next__(self):
        # 计算出下一个值
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.count :
            raise StopIteration()
        return self.a # 返回下一个值
            
    def __getitem__(self, n):
        # __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断

        if isinstance(n, int): # 传入 int
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # 传入切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

fib = Fib(1000)
for i in fib:
    print(i)


# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，
# 比如，取第5个元素。要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
print('#####')

print(fib[10])

# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
print(fib[0:5])

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错

class AttrClazz(object):

    def __init__(self):
        self.name = 'Micheal'

    # 当调用不存在的属性时，比如score，
    # Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    # 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
    def __getattr__(self, attr):
        if attr == 'score':
            return 95
        if attr == 'age': # 返回age函数
            return lambda: 25
        raise AttributeError('class AttrClazz has no attribute: %s' % attr)

attr = AttrClazz()
# 调用name属性，没问题
print(attr.name)

# 调用不存在的score属性，就会报错 has no attribute 'score'
# 此时可以自定义__getattr__() 方法，动态返回一个属性
print(attr.score)

print(attr.age())

# 任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# print(attr.abc)

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段

# 这种完全动态调用的特性有什么实际作用呢？
# 作用就是，可以针对完全动态的情况作调用

# 利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, param):
        return Chain('%s/%s' % (self._path, param))

    __repr__ = __str__


# 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变
print(Chain().status.user.timeline.list)


# 还有些REST API会把参数放到URL中
# user/gnl00/home
print(Chain().user('gnl00').home)



# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。

# 能不能直接在实例本身上调用呢
# 在Python中，答案是肯定的。任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

# 怎么判断一个变量func是对象还是函数呢？
# callable(func) == True 是函数

class CallClazz(object):
    def __init__(self, name):
        self._name = name

    def __call__(self, param):
        print('My name is: %s' % self._name)
        print(param)

    def __getattr__(self):
        pass

callClazz = CallClazz('AAA')
callClazz('bbb')



print('################# 枚举 ###############')
## 5、枚举
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month)
for m in Month:
    print(m)

for name, item in Month.__members__.items():
    print(name, ' ==> ', item, ' ==> ', item.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
@unique
class MyEnum(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(MyEnum.Mon)
print(MyEnum['Tue'])
print(MyEnum.Wed.value)





print('################# 元类 ###############')
## 6、元类 

## type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# type()函数可以查看一个类型或变量的类型

from Hello import Hello
h = Hello()
h.hello()

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
print(type(Hello)) # <class 'type'>
print(type(h)) # <class 'Hello.Hello'>

# 要创建一个class对象，type()函数依次传入3个参数
# 1、class的名称 
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法 
# 3、class的方法名称与函数绑定


## metaclass()
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass，直译为元类

# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例

# 定义ListMetaclass，
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
class ListMetaClass(type):
    
    # clazz 当前准备创建的类的对象
    # name 类的名字
    # bases 类继承的父类集合
    # attrs 类的方法集合
    def __new__(clazz, name, bases, attrs):
        attrs['add'] = lambda self, val: self.append(val)
        return type.__new__(clazz, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaClass):
    pass

L = MyList()
L.add(1)
print(L) # [1]




## 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？
# ORM就是一个典型的例子。
# 把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。


# Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如 StringField，IntegerField等等
class StringField(Field):
    def __init__(self, name, column_type):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name, column_type):
        super(IntegerField, self).__init__(name, 'bigint')


# 编写 ModelMetaclass
class ModelMetaclass(type):
    pass

# 基类Model
class Model(object):
    pass

class User(Model):
    pass



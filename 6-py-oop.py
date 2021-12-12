#################################### 八、面向对象编程 #############################################

## 1、类与实例
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，
# 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# class 后面紧接着是类名，即 Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

class Person(object):
    pass

# 定义好了 Person 类，就可以根据 Person 类创建出 Person 的实例，创建实例是通过类名+()实现的

per = Person()
print(per) # <__main__.Person object at 0x00000299DEEA2FD0> 0x00000299DEEA2FD0 表示per实例的内存地址

# 可以自由地给一个实例变量绑定属性，比如，给实例 per 绑定一个 name 属性
per.name = 'Candy'
print(per.name) # Candy

## 数据封装
# 和静态语言不同，Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同

per1 = Person()
per2 = Person()
per1.age = 18

print(per1.age) # 18
# print(per2.age) # has no attribute 'age'

class Student(object):
    
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去

    # __init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
    # 并且调用时不用传递该参数。除此之外，类的方法和普通函数没有什么区别
    def show_info(self):
        print('name: %s, score: %d' % (self.name, self.score))

alan = Student('Alan', 93)
barry = Student('Barry', 89)

alan.show_info()
barry.show_info()

print('######################################### 访问权限/访问限制 #################################################')
## 2、访问权限/访问限制

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Student1(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

stu1 = Student1('ABC', 90)
stu1.__score = 95 # 在类外部对private属性的修改不会生效
stu1.print_score() # ABC: 90

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# print(stu1.__name) # Student1' object has no attribute '__name'

# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以仍然可以通过_Student__name来访问__name变量

print(stu1._Student1__name) # ABC


print('######################################### 继承与多态 #################################################')
## 3、继承与多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

class Animal(object):

    def run(self):
        print('animal can run')


class Cat(Animal):
    pass

class Dog(Animal):
    pass

dogg = Dog()
catt = Cat()

dogg.run()
catt.run()

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，
# 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了


print('######################################### 4、获取对象信息 #################################################')
## 4、获取对象信息

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

## 1、判断对象类型 type()

print(type(123)) # <class 'int'>
print(type(123)==type(456)) #True
print(type(123)==int) # True

# 如果要判断一个对象是否是函数怎么办？
# 用types模块中定义的常量：FunctionType

import types

def fn():
    pass

print(type(fn) == types.FunctionType) # True
print(type(lambda x: x) == types.LambdaType) # True
print( type((x for x in range(10))) == types.GeneratorType) # True

## 2、使用 isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
print(isinstance(dogg, Animal)) # True

## 3、使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list

# 比如，获得一个str对象的所有属性和方法
print(dir(str))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，
# 比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法

strr = 'AAABBBCCC'
print(len(strr))
print(strr.__len__())

# 自己写的类，如果也想用len(xxx)的话，就需要在类中实现一个 __len__() 方法

## getattr()、setattr() 以及 hasattr()
# 仅仅把属性和方法列出来是不够的，配合 getattr()、setattr()以及 hasattr()，我们可以直接操作一个对象的状态

class MyObject(object):

    def __init__(self):
        self.__x = 10
        self.X = 100

    def power(self):
        return self.__x ** 2

obj = MyObject()
print(hasattr(obj, '__x')) # 有属性'__x'吗？False，无法查看某个类的private属性
print(hasattr(obj, 'X')) # 有属性'X'吗？True

print(hasattr(obj, 'y')) # 有属性'y'吗？False

setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？True

print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'

# 如果试图获取不存在的属性，会抛出AttributeError的错误
# print(getattr(obj, 'z')) # 获取属性'z' 'MyObject' object has no attribute 'z'

# 此时可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

print(hasattr(obj, 'power')) # 有属性'power'吗？
my_fn = getattr(obj, 'power') # 获取属性'power'
my_fn()

## 一个正确的用法的例子如下

# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None

# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
# 它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。



print('######################################### 4、获取对象信息 #################################################')
## 5、实例属性和类属性

class Student2(object):
    name = 'student'

    def __init__(self):
        pass

stu21 = Student2()

print(Student2.name) # student
print(stu21.name) # student

stu21.name = 'stu21_name'

print(Student2.name) # student
print(stu21.name) # stu21_name

Student2.name = 'change_name'

print(Student2.name) # change_name
print(stu21.name) # stu21_name
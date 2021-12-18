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

from types import MethodType
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


## 2、@property https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208

## 3、多重继承 https://www.liaoxuefeng.com/wiki/1016959663602400/1017502939956896

## 4、定制类 https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904

## 5、枚举 https://www.liaoxuefeng.com/wiki/1016959663602400/1017595944503424

## 6、元类 https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
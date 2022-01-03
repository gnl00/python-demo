# 1、异常处理

# 1) try-except-finnaly 块

# 2) raise 异常抛出


# 2、调试
# 1) 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

print(foo(1))
# foo(0) # AssertionError: n is zero

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用 -O 参数来关闭assert 
# 断言的开关“-O”是英文大写字母O，不是数字0

# python -O 8-py-exception.py

# 2) logging
import logging

# 默认仅输出 error 级别及以上的错误日志

# 将日志输出级别调低
logging.basicConfig(level=logging.DEBUG)

logging.debug('debugggggg')
logging.info('logging info')
logging.error('errorrrrrr')


# Python 调试器 pdb
# 让程序以单步方式运行，可以随时查看运行状态

# python -m pdb 8-py-exception.py
# 输入命令l来查看代码
# 输入命令n可以单步执行代码
# 输入命令p 变量名来查看变量
# 输入命令q结束调试


# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行

# 3、单元测试



# 4、文档测试
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Argparse Tutorial
From: https://docs.python.org/2/howto/argparse.html#introducing-positional-arguments
This was written for argparse in Python 3.
A few details are different in 2.x, especially some exception messages, which were improved in 3.x.
"""
from __future__ import print_function
import argparse


# The basics
def main0():
    """"""
    parser = argparse.ArgumentParser()
    parser.parse_args()


'''
$ python prog.py
$ python prog.py --help   # 查看命令帮助信息
usage: prog.py [-h]       # 展示使用方式

optional arguments:       # 可选参数
  -h, --help  show this help message and exit

$ python prog.py --verbose
usage: prog.py [-h]
prog.py: error: unrecognized arguments: --verbose
$ python prog.py foo
usage: prog.py [-h]
prog.py: error: unrecognized arguments: foo
'''


# Introducing Positional arguments
def main1():
    parser = argparse.ArgumentParser()  # 实例化一个对象
    parser.add_argument("echo", help="display a square of a given number", type=int)  # 添加了一个位置参数,没有double dash
    args = parser.parse_args()  # 解析命令行参数到对象
    print(args.echo ** 2)  # echo 对应的参数存储在了args.echo的同名方法(?)中


'''
$ python prog.py --help
usage: prog.py [-h] echo  # 命令模板

positional arguments:    # 位置参数,没有双短线
  echo   echo the string you use here

optional arguments:      # 可选参数，前面有短线
  -h, --help  show this help message and exit

$ python prog.py foo
foo

$ python Mylab.py
usage: Mylab.py [-h] echo          # 位置参数默认必填，否则报错
Mylab.py: error: too few arguments

$ python Mylab.py "hello"  # 接受的参数默认为string类型，除非指定其他类型
hello

$ python Mylab.py 2
4

'''


# Introducing Optional arguments
def main2():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")  # verbosity: n.信息显示， 冗长；赘言；唠叨
    args = parser.parse_args()

    if args.verbosity:
        print(args.verbosity)
        print("verbosity turned on")     # print的结果可以直接显示到命令行的结果里


'''
$ python prog.py --help
usage: prog.py [-h] [--verbosity VERBOSITY]
optional arguments:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY     # 可选参数，使用方式：键值对方式 python script.py --verbosity VERBOSITY 
                        increase output verbosity

$ python prog.py --verbosity
usage: prog.py [-h] [--verbosity VERBOSITY]
prog.py: error: argument --verbosity: expected one argument   # 少参数

$ python Mylab.py --verbosity 1   # 键：--verbosity 值：1 --->  args.verbosity
1
verbosity turned on

'''


def main3():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increse output verbosity", action="store_true")
    #  action="store_true"  命令行如果有整个参数，则赋值True给verbose
    args = parser.parse_args()
    if args.verbose:
        print(args.verbose)
        print("verbosity turned on")


'''
$ python prog.py --help
usage: prog.py [-h] [--verbose]
optional arguments:
  -h, --help  show this help message and exit
  --verbose   increase output verbosity        #  无需跟参数的 flag： n. 标志；旗子

$ python Mylab.py --verbose
True
verbosity turned on

$ python Mylab.py --verbose 1          # 后面不跟参数
usage: Mylab.py [-h] [--verbose]
Mylab.py: error: unrecognized arguments: 1

$ python Mylab.py --help
usage: Mylab.py [-h] [-v]               # short options，一个短横
optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increse output verbosity

'''


# Combining Positional and Optional arguments
def main4():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbodity")
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbose:
        print("args.verbose:{}".format(args.verbose))
        print("the square of the %d equals %d" % (args.square, answer))
    else:
        print("args.verbose:{}".format(args.verbose))  # 可选参数没有就默认为None
        print("the square of {} equals {}".format(args.square, answer))


'''
$ python prog.py
usage: prog.py [-h] [-v] square
prog.py: error: the following arguments are required: square

$ python Mylab.py
usage: Mylab.py [-h] [-v] square
Mylab.py: error: too few arguments

$ python Mylab.py 3
args.verbose:False
the square of 3 equals 9


$ python Mylab.py -v 3
args.verbose:True
the square of the 3 is 9

$ python Mylab.py 3 -v   # 参数顺序可以颠倒
args.verbose:True
the square of the 3 equals 9

'''


def main5():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number", type=int)
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity", choices=[0, 1, 2])
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbosity == 2:  # 只有--verbosesity双短横的参数才会被转化为args的属性，否则报错no attribute
        print("args.verbosity ={}".format(args.verbosity))
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print("args.verbosity ={}".format(args.verbosity))
        print("{} x  2  = {}".format(args.square, answer))
    else:
        print(answer)


'''
$ python Mylab.py --help
usage: Mylab.py [-h] [-v {0,1,2}] square
positional arguments:
  square                display a square of a given number
optional arguments:
  -h, --help            show this help message and exit
  -v {0,1,2}, --verbosity {0,1,2}
                        increase output verbosity

$ python Mylab.py -v 3 4
usage: Mylab.py [-h] [-v {0,1,2}] square
Mylab.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2) # 同时显示错误信息和帮助信息

$ python Mylab.py -v 2 4
args.verbosity =2
the square of 4 equals 16

'''


def main6():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number", type=int)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)
    # action="count" 记录可选参数的出现次数, default=指定默认值（不存在参数时）为0，取代原先的None

    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbosity == 2:
        print("args.verbosity ={}".format(args.verbosity))
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print("args.verbosity ={}".format(args.verbosity))
        print("{} x  2  = {}".format(args.square, answer))
    else:
        print("args.verbosity ={}".format(args.verbosity))
        print(answer)


'''
# python Mylab.py --help
usage: Mylab.py [-h] [-v] square
positional arguments:
  square           display a square of a given number
optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity  increase output verbosity

# python Mylab.py 4
16

$ python Mylab.py 4 -v
args.verbosity =1
4 x  2  = 16

$ python Mylab.py 4 -vv     # 
args.verbosity =2
the square of 4 equals 16

$ python Mylab.py 4 --verbosity --verbosity
args.verbosity =2
the square of 4 equals 16

$ python Mylab.py 4
args.verbosity =0
16


'''


# Getting a little more advanced
def main7():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
    args = parser.parse_args()
    answer = args.x ** args.y
    if args.verbosity >= 2:
        print("args.verbosity:".format(args.verbosity))
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    elif args.verbosity == 1:
        print("args.verbosity:".format(args.verbosity))
        print("{} ** {} = {}".format(args.x, args.y, answer))
    else:
        print("args.verbosity:".format(args.verbosity))
        print("{} ** {} = {}".format(args.x, args.y, answer))


'''
$ python Mylab.py --help
usage: Mylab.py [-h] [-v] x y
positional arguments:
  x                the base
  y                the exponent
optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity  increase output verbosity


$ python Mylab.py  2 3
args.verbosity:
2 ** 3 = 8


$ python Mylab.py  2 3 -vvv
args.verbosity:
2 to the power 3 equals 8


$ python Mylab.py  2 3 -v
args.verbosity:
2 ** 3 = 8
'''


def main8():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
    args = parser.parse_args()
    answer = args.x ** args.y
    if args.verbosity >= 2:
        print("args.verbosity:".format(args.verbosity))
        print("Running '{}'".format(__file__))
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    elif args.verbosity == 1:
        print("args.verbosity:".format(args.verbosity))
        print("{} ** {} = {}".format(args.x, args.y, answer))
    else:
        print("args.verbosity:".format(args.verbosity))
        print("{} ** {} = {}".format(args.x, args.y, answer))


# Conflicting options
def main9():
    parser = argparse.ArgumentParser(description="Calculate X to the power of Y")

    group = parser.add_mutually_exclusive_group()  # 相互冲突的两个参数
    group.add_argument("-v", "--verbosity", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)
    args = parser.parse_args()
    answer = args.x ** args.y
    if args.quiet:
        print("args.quiet:{}".format(args.quiet))
        print(answer)
    elif args.verbosity:
        print("args.verbosity:{}".format(args.verbosity))
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print("{} ** {} = {}".format(args.x, args.y, answer))


'''
$ python Mylab.py  --help
usage: Mylab.py [-h] [-v | -q] x y
positional arguments:
  x
  y
optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity
  -q, --quiet

$ python Mylab.py  3 2 -v
args.verbosity:True
3 to the power 2 equals 9

$ python Mylab.py  3 2 -q
args.quiet:True
9

$ python Mylab.py  3 2
3 ** 2 = 9

$ python Mylab.py  -vq   # 两个参数使用一个短横线
usage: Mylab.py [-h] [-v | -q] x y
Mylab.py: error: argument -q/--quiet: not allowed with argument -v/--verbosity

'''


if __name__ == "__main__":
    main0()
    main1()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
    main9()

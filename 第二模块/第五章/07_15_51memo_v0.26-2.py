#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo.v026.py
# A memo demo 51备忘录,使用函数进行优化
# author : Elliot


import sys


__author__ = 'Elliot'


def welcome():
    "欢迎词."
    desc = '51备忘录'.center(30, '-')
    print(desc)

    welcome = 'welcome'
    print(f'{welcome}', __author__)

    print('请输入备忘信息 : ')


all_memo = []


def input_memo():
    "输入备忘录"
    try:
        is_add = True
        all_time = 0
        while(is_add):
            in_date = input('日期:')
            in_thing = input('事件:')
            in_time = input('用时:')
            print('代办列表'.center(30, '-'))

            add_memo(in_date, in_thing, in_time)
            all_time += int(in_time)
            print_memo(all_time)

            is_add = input().strip() == 'y'
    except Exception as error:
        print('备忘录出错啦! 问题是:', error)


def print_memo(all_time):
    """打印出memo"""
    num = 0
    for m in all_memo:
        num += 1
        print('%s:%s' %   (num, m))

    print(f'共{len(all_memo)}条代办事项,总时长: {all_time}.', end='')
    print('(y:继续添加, n:退出)')


def add_memo(in_date, in_thing, in_time):
    """只管添加备忘"""
    one = {}
    one['date'] = in_date
    one['thing'] = in_thing
    one['time'] = in_time
    all_memo.append(one)

def help_no_argv():
    print("没有argv参数, 重试")


def help():
    print(" usage: ")

def main():
    """
    main: 程序主入口, 当前文件单独运行时候从这里运行
    函数优化: 每个函数尽量只干一个活
    """
    # print(sys.argv)
    if len(sys.argv) == 1:
        help_no_argv()
    welcome()
    if sys.argv[1] in {"-h", "--help"}:
        help()
    input_memo()

if __name__ == "__main__":
    main()

#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 作业2: 51memo
# 第一次作业尝试
# author: E11iot

#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo.v026.py
# A memo demo 51备忘录,使用函数进行优化
# author : Elliot


import sys
import pickle


__author__ = 'Elliot'


class Memo():
    '四个属性处理类'

    def __init__(self, id, name, thing, date):
        '初始化'
        self.__id = 0
        self.name = name
        self.thing = thing
        self.date = date



    @property
    def id(self):
        'id只读'
        return self.__id

    @id.setter
    def id(self, val):
        '可修改id'
        self.__id = val


class MemoAdmin():
    '增删改查, 处理输出输入'

    def __init__(self):
        self.memo_list = []

    def welcome(self):
        "欢迎词."
        desc = '51备忘录'.center(30, '-')
        print(desc)
        print(f'Welcome, {__author__} !')

        print('请输入备忘信息 : ')
        memu = {
            '1': '增',
            '2': '删',
            '3': '改',
            '4': '查'
        }
        for k, v in memu.items():
            print(k, v)
        
        choose = input('请输入选择项目: ')
        # self.judge(choose)

    def judge(self, choose):
        '用来判断输入'


    def add(self):
        '增'
        pass

    def delete():
        '删'
        pass

    def modify():
        '改'
        pass

    def query():
        '查'
        pass


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
        print('%s:%s' % (num, m))

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
    主函数
    """
    
    admin = MemoAdmin()
    admin.welcome()
    while True:
        select = input('请输入你的选择: ')
        if select in memo_dict:
            run = getattr(admin, me)


if __name__ == "__main__":
    main()

#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51备忘录
# 作业2_尝试2.py
# author:  E11iot
'''
还能在这里加注释
'''

import pickle


__author__ = 'E1iot'


class Memo():
    '四个属性处理类'

    def __init__(self, date, name, thing):
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
        self.memo_list = self.load()

    @staticmethod
    def welcome():
        "欢迎词."
        desc = '51备忘录'.center(30, '-')
        print(desc)
        print(f'Welcome, {__author__} !')

    @staticmethod
    def deal_input_data(self):
        '处理用户输入'
        input_memo = input('请输入代办(如: 1.1-小8-学习python): ').strip()
        input_list = input_memo.split('-')
        if len(input_list) == 3:
            return input_list

    def add(self):
        '增'
        memo_date_list = MemoAdmin.deal_input_data(self)
        print(memo_date_list)
        memo = Memo(*memo_date_list)
        memo.id = len(self.memo_list) + 1
        self.memo_list.append(memo)

    def delete(self):
        '删'
        delete_id = int(input('请输入想要删除的备忘录(如: 1, 2, 3): '))
        if delete_id > len(self.memo_list):
            print('输入出错, 请重新输入!')
            self.delete()
            return  # 这里直接返回, 不在函数中嵌套运行
        self.memo_list.remove(self.memo_list[delete_id - 1])
        print('删除成功!')

    def modify(self):
        '改'
        modify_id = int(input('请输入需要修改的备忘录(如: 1, 2, 3): '))
        if modify_id > len(self.memo_list):
            print('输入出错, 请重新输入!')
            self.modify()
            return  # 这里直接返回, 不在函数中嵌套运行
        modify_stuf = self.deal_input_data(self)
        memo = Memo(*modify_stuf)
        memo.id = modify_id
        self.memo_list[modify_id - 1] = memo

    def query(self):
        '查'
        query_id = int(input('请输入需要查询的备忘录(如: 1, 2, 3): '))
        if query_id > len(self.memo_list):
            print('输入出错, 请重新输入!')
            self.query()
            return  # 这里直接返回, 不在函数中嵌套运行
        # memo = self.memo_list[query_id - 1]
        memo = self.memo_list[query_id - 1]
        print(memo.id, memo.date, memo.name, memo.thing)

    def save(self):
        '保存'
        with open('memo.pkl', 'wb') as f:
            f.write(pickle.dumps(self.memo_list))

        # print(f)
        return True

    def print_all(self):
        '打印出全部代办'
        if len(self.memo_list) == 0:
            print('没有记录, 请添加! ')
        for memo in self.memo_list:
            print(memo.id, memo.date, memo.name, memo.thing)

    @classmethod
    def load(self):
        '加载'
        try:
            with open('memo.pkl', 'rb') as file:
                memo_list = pickle.load(file)
        except Exception as e:
            memo_list = []

        # print(file)
        return memo_list


def main():
    '入口'
    admin = MemoAdmin()
    memu = {
        '1': 'add',
        '2': 'delete',
        '3': 'modify',
        '4': 'query',
        '5': 'print_all',
        '6': '退出'
    }

    while True:
        print('请输入备忘信息 : ')
        for k, v in memu.items():
            print(k, v)
        select = input('请输入你的选择: ')
        if select == '6':
            admin.save()
            break
        if select in memu:
            run = getattr(admin, memu.get(select))  # getattr返回值可直接运行
            # print(run)
            print(memu.get(select))
            if run:
                run()
            else:
                print('选项出错, 请检查是否正确')


if __name__ == "__main__":
    main()

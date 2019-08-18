#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 作业1_重构单位转换器
# author: E11iot


class Transfer(type):
    def __init__(self, temp, choose, retry):
        "初始化, 跳转欢迎界面"
        self.temp = temp
        self.choose = choose
        self.retry = retry

    def welcome():
        '打印出欢迎语和程序信息'
        print('欢迎使用万能单位转换器'.center(30, '-'))
        menu = {
            'T': '温度转换',
            'L': '长度转换',
            'C': '货币转换'
        }
        for k, v in menu.items():
            print(k, v)

    def ERROR(self):
        "用来处理输入出错的情况"
        retry = input('输入出错了! 是否重试? (y/n)')
        self.JUDGE(retry)

    def JUDGE(self, temp='PASS', choose='PASS'):
        '用来判断各个输入参数'
        if choose == 'T' or 't':
            Tempp = Temperature
        elif choose == 'L' or 'l':
            Length()
        elif choose == 'C' or 'c':
            pass
        elif choose == 'PASS':
            pass
        else:
            self.ERROR()

    def Retry(self, retry='PASS'):
        if retry == 'Y' or 'y':
            self.welcome()
        elif retry == 'N' or 'n':
            exit
        elif retry == 'PASS':
            pass
        else:
            self.ERROR()

    def Continue(self):
        retry = input('计算完毕, 是否继续? Y/N')
        self.JUDGE(retry)

    def __call__(self):
        "将类作为函数调用"
        self.welcome()


class Temperature(metaclass=Transfer):  # 新增父类继承 Transfer
    def __init__(self, temp, choose, retry):
        "初始化界面"
        self.temp = temp
        self.choose = choose
        self.retry = retry
        self.welcome(self)

    def welcome():  # 此处没有实例, 不带参数self
        "欢迎词, 并跳转判断函数JUDGE()"
        temp = input('温度选择, 请输入温度(实例: 1C 或 1F ): ')
        return temp

    def JUDGE(self, temp):
        "判断温度输入是否正确, 以及分流"
        if self.temp.find('C') != -1:
            self.Tc2Tf(temp)
        elif temp.find('F') != -1:
            self.Tf2Tc(temp)
        else:
            super.ERROR()

    def Tc2Tf(self, temp):
        "摄氏转华氏"
        temp = float(temp.strip('C').strip('F'))
        # 摄氏温度转华氏温度 Tf = (9/5) TC + 32
        Tf = (9/5) * temp + 32
        print(Tf, end='华氏度')
        super.Continue()

    def Tf2Tc(self, temp):
        "华氏转摄氏"
        temp = float(temp.strip('C').strip('F'))
        # 华氏温度转摄氏温度 Tc=(Tf-32)(5/9)
        Tc = (temp - 32) * (5/9)
        print(Tc, end='摄氏度')
        super.Continue()

    def __call__():
        "将类作为函数调用"
        self.__init__()


class Length(metaclass=Transfer):
    def __init__(self, temp, choose, retry):
        "初始化, 跳转欢迎界面"
        self.temp = temp
        self.choose = choose
        self.retry = retry

    def welcome(self):
        temp = input('请输入长度(例如: 100km或100mi): ')
        self.JUDGE(temp)

    def JUDGE(self, temp):
        if temp.find('km') != -1:
            self.Km2Mi(temp)

        elif temp.find('mi') != -1:
            self.Mi2Km(temp)

        else:
            super.ERROR()

    def Km2Mi(self, temp):
        temp = float(temp.strip('km').strip('mi'))
        # 1公里等于0.62137英里
        mi = temp * 0.62137
        print(mi, end='英里')
        super.Continue()

    def Mi2Km(self, temp):
        temp = float(temp.strip('km').strip('mi'))
        # 1英里等于1.61公里
        km = temp * 1.61
        print(km, end='公里')
        super.Continue()

    def __call__(self):
        "将类作为函数调用"
        self.welcome(self)


class Currency(metaclass=Transfer):
    def __init__(self, temp, choose, retry):
        "初始化, 跳转欢迎界面"
        self.temp = temp
        self.choose = choose
        self.retry = retry

    def welcome(self):
        temp = input('请输入货币(实例：100USD或100CNY): ')
        self.JUDGE(temp)

    def JUDGE(self, temp):
        if temp.find('USD') != -1:
            self.USD2CNY(temp)

        elif temp.find('CNY') != -1:
            self.CNY2USD(temp)

        else:
            super.ERROR()

    def USD2CNY(self, temp):
        "美元转人民币"
        temp = float(temp.strip('USD').strip('CNY'))
        # 1美元等于6.7272人民币
        CNY = temp * 6.7262
        print(CNY, end="人民币")

    def CNY2USD(self, temp):
        "人民币转美元"
        temp = float(temp.strip('USD').strip('CNY'))
        # 1人民币等于0.15美元
        USD = temp * 0.15
        print(USD, end="美元")

    def __call__(self):
        "将类作为函数调用"
        self.welcome(self)


def main():
    Transfer.welcome()
    choose = input('请输入转换类型: ')
    Transfer.JUDGE(choose)


if __name__ == "__main__":
    main()

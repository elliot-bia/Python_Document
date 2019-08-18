#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 作业1_重构单位转换器
# 尝试2, 再次尝试
# author: E11iot
# --函数通过main()函数进行输入, 然后Tranfer类进行处理,
# --在Transfer类中, 实例化调用其他三个类


class Transfer():
    "主类"

    def __init__(self):
        '初始化'
        # self.choose = choose
        pass

    def welcome(self):
        '打印出欢迎语和程序信息, 并且返回转换类型'
        print('欢迎使用万能单位转换器'.center(30, '-'))
        menu = {
            'T': '温度转换',
            'L': '长度转换',
            'C': '货币转换'
        }
        for k, v in menu.items():
            print(k, v)

        choose = input('请输入转换类型: ')

        self.JUDGE(choose)

    def JUDGE(self, choose):
        '用来判断各个输入参数, 并进入各个子类处理'
        if choose == 'T' or choose == 't':
            start_tp = Temperature()
            start_tp.welcome_tp()
            # # print(temp)
            # pass
            self.Continue()

        elif choose == 'L' or choose == 'l':
            start_ln = Length()
            start_ln.welcome_ln()
            # # print(temp)

            # pass
            self.Continue()
        elif choose == 'C' or choose == 'c':
            start_cr = Currency()
            start_cr.welcome_cr()
            # pass
            self.Continue()
        else:
            self.ERROR()

    def ERROR(self):
        "用来处理输入出错的情况"
        retry = input('输入出错了! 是否重试? (y/n): ')
        self.Retry(retry)

    def Retry(self, retry='PASS'):
        '判断重试'
        if retry == 'Y' or retry == 'y':
            # print(retry)
            self.welcome()
            return  # 这里直接返回, 不在函数中嵌套运行
        elif retry == 'N' or retry == 'n':
            exit()
        elif retry == 'PASS':
            pass
        else:
            self.ERROR()

    def Continue(self):
        '每次在Transfer.JUDGE中运行完子类后, 进行判断是否重新开始'
        retry = input('计算完毕, 是否继续? (Y/N): ')
        self.Retry(retry)


class Temperature(Transfer):
    '温度转换类, 新增父类继承 Transfer'

    def __init__(self):
        "初始化界面"
        pass
        # self.temp = temp
        # self.choose = choose
        # self.retry = retry

    def welcome_tp(self):  # 此处没有实例, 不带参数self
        "欢迎词, 返回值"
        temp = input('温度选择, 请输入温度(实例: 1C 或 1F ): ')
        # print(temp)
        self.JUDGE_tp(temp)

    def JUDGE_tp(self, temp):
        "判断温度输入是否正确, 以及分流"
        if temp.find('C') != -1:
            self.Tc2Tf(temp)
            return  # 这里直接返回, 不在函数中嵌套运行
        elif temp.find('F') != -1:
            self.Tf2Tc(temp)
            return  # 这里直接返回, 不在函数中嵌套运行
        else:
            Transfer.ERROR(self)
            return  # 这里直接返回, 不在函数中嵌套运行

    def Tc2Tf(self, temp):
        "摄氏转华氏"
        temp = float(temp.strip('C').strip('F'))
        # 摄氏温度转华氏温度 Tf = (9/5) TC + 32
        Tf = (9/5) * temp + 32
        print(Tf, end='华氏度\n')

    def Tf2Tc(self, temp):
        "华氏转摄氏"
        temp = float(temp.strip('C').strip('F'))
        # 华氏温度转摄氏温度 Tc=(Tf-32)(5/9)
        Tc = (temp - 32) * (5/9)
        print(Tc, end='摄氏度\n')


class Length(Transfer):
    '长度转换'

    def welcome_ln(self):
        '加入神奇的注释, 欢迎并输入'
        temp = input('请输入长度(例如: 100km或100mi): ')
        self.JUDGE_ln(temp)

    def JUDGE_ln(self, temp):
        '加入神奇的注释, 用来判断Length(ln)传入参数'
        if temp.find('km') != -1:
            self.Km2Mi(temp)

        elif temp.find('mi') != -1:
            self.Mi2Km(temp)

        else:
            Transfer.ERROR(self)

    def Km2Mi(self, temp):
        '加入神奇的注释, 公里转英里'
        temp = float(temp.strip('km').strip('mi'))
        # 1公里等于0.62137英里
        mi = temp * 0.62137
        print(mi, end='英里\n')

    def Mi2Km(self, temp):
        '加入神奇的注释, 英里转公里'
        temp = float(temp.strip('km').strip('mi'))
        # 1英里等于1.61公里
        km = temp * 1.61
        print(km, end='公里\n')


class Currency(Transfer):
    '货币转换'

    def welcome_cr(self):
        '加入神奇的注释, 用来欢迎, 并处理输入'
        temp = input('请输入货币(实例：100USD或100CNY): ')
        self.JUDGE_cr(temp)

    def JUDGE_cr(self, temp):
        '加入神奇的注释, 用来判断Currency(cr)传入的参数'
        if temp.find('USD') != -1:
            self.USD2CNY(temp)

        elif temp.find('CNY') != -1:
            self.CNY2USD(temp)

        else:
            Transfer.ERROR(self)

    def USD2CNY(self, temp):
        "美元转人民币"
        temp = float(temp.strip('USD').strip('CNY'))
        # 1美元等于6.7272人民币
        CNY = temp * 6.7262
        print(CNY, end="人民币\n")

    def CNY2USD(self, temp):
        "人民币转美元"
        temp = float(temp.strip('USD').strip('CNY'))
        # 1人民币等于0.15美元
        USD = temp * 0.15
        print(USD, end="美元\n")


def main():
    "主函数, 进行输入"
    start = Transfer()
    start.welcome()


if __name__ == "__main__":
    main()

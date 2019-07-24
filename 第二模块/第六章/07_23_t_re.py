import re


#  定义正则表达式对象
RE_PHONE = re.compile(r'\d{3}-\d{8}|\d{4}-\d{7}')
#   验证输入汉字
RE_CHINESE = re.compile(r'^[\u4e00-\u9fa5]{1,8}$')
#   验证密码
RE_PWD = re.compile(r'^[a-zA-Z]\w{7,17}$')


def find_phone(text: str) -> list:
    """函数注释"""
    return RE_PHONE.findall(text)


def verify_CH(text):
    "函数注释"
    if RE_CHINESE.match(text):
        return True
    else:
        return False


def verify_user(re_obj, text):
    if re_obj.match(text):
        return True
    else:
        return False


def main():
    # text = '随便写几个电话号码 111-123141245153然后来这个の24425-342521, 还有1234-11234556发我'
    # print(find_phone(text))
    name = 'elliot'
    name = '中文'
    # name = '中1文'
    print('NAME:', verify_user(RE_CHINESE, name))

    password = 'ffeafe123ajjy'
    print('Password:', verify_user(RE_PWD, password))


if __name__ == "__main__":
    main()

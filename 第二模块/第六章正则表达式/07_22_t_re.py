import re


#  定义正则表达式对象
RE_PHONE = re.compile(r'\d{3}-\d{8}|\d{4}-\d{7}')


def find_phone(text:str) -> list:
    """函数注释"""
    return  RE_PHONE.findall(text)


def main():
    text = '随便写几个电话号码 111-123141245153然后来这个の24425-342521, 还有1234-11234556发我'
    print(find_phone(text))


if __name__ == "__main__":
    main()
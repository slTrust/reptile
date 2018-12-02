import re

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
aa = re.match(r'^\d{3}\-\d{3,8}$', '010-12345678')
print(aa)


def test(str):
    if re.match(r'^\d{3}\-\d{3,8}$', str):
        print('ok')
    else:
        print('failed')


while True:
    userInput = input("请输入电话号码:")
    test(userInput)
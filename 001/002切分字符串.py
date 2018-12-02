import re

arr = 'a b   c'.split(' ')
#['a', 'b', '', '', 'c']

# 切分字符串 可匹配一个或多个空格
arr2 = re.split(r'\s+', 'a b   c')
# ['a', 'b', 'c']
print(arr2)

# 匹配以, 空格 ; 为分割点

arr3 = re.split(r'[\s\,\;]+', 'a,b;; c  d')
# ['a', 'b', 'c', 'd']
print(arr3)
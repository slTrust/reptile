
# re模块

# 由于Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'


# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

s2 = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'
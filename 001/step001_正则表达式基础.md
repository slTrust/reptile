### 基础1：

- 全局匹配函数使用格式	re.compile(正则表达式).findall(源字符串)

```
普通字符     正常匹配
\n          匹配换行符  
\t          匹配制表符
\w          匹配字母、数字、下划线
\W          匹配除字母、数字、下划线
\d          匹配十进制数字
\D          匹配除十进制数字
\s          匹配空白字符
\S          匹配除空白字符
[ab89x]	    原子表，匹配ab89x中的任意一个
[^ab89x]    原子表，匹配除ab89x以外的任意一个字符
```

#### 实例1：

```
源字符串："aliyunedu"
正则表达式："yu"
匹配出什么？	yu

源字符串：(有换行符)
'''aliyun
edu'''
正则表达式："yun\n"
匹配出什么？	yun\n

源字符串："aliyu89787nedu"
正则表达式："\w\d\w\d\d\w"
匹配出什么？	u89787


源字符串："aliyu89787nedu"
正则表达式："\w\d[nedu]\w"
匹配出什么？	87ne
```


### 基础2：

```
.	匹配除换行外任意一个字符
^	匹配开始位置
$	匹配结束位置
*	前一个字符出现0\1\多次 
?	前一个字符出现0\1次
+	前一个字符出现1\多次
{n}	前一个字符恰好出现n次
{n,}	前一个字符至少n次
{n,m}   前一个字符至少n，至多m次 
|	模式选择符或
()	模式单元，通俗来说就是：想提取出什么内容，就在正则中用小括号将其括起来
```


#### 实例2:

```
源字符串：'''aliyunnnnji87362387aoyubaidu'''

正则表达式："ali..."
匹配出什么？	aliyun

正则表达式："^li..."
匹配出什么？	None

正则表达式："^ali..."
匹配出什么？	aliyun

正则表达式："bai..$"
匹配出什么？	baidu

正则表达式："ali.*"
匹配出什么？	aliyunnnnji87362387aoyubaidu
Tips：默认贪婪，即默认尽可能多地进行匹配

正则表达式："aliyun+"
匹配出什么？ aliyunnnn

正则表达式："aliyun?"
匹配出什么？ aliyun

正则表达式："yun{1,2}"
匹配出什么？	yunn

正则表达式："^al(i..)."
匹配出什么？	iyu
```

#### 基础3：

- 贪婪模式：尽可能多地匹配
- 懒惰模式：尽可能少地匹配，精准模式

> 默认贪婪模式


如果出现如下组合，则代表为懒惰模式：

```
*?
+?
```

#### 实例3：

```
源字符串："poytphonyhjskjsa"
正则表达式："p.*y"
匹配出什么？	poytphony
为什么？	默认贪婪模式

源字符串："poytphonyhjskjsa"
正则表达式："p.*?y"
匹配出什么？	['poy', 'phony']
为什么？	懒惰模式，精准匹配
```

#### 基础4：

> 模式修正符：在不改变正则表达式的情况下通过模式修正符使匹配结果发生更改

```
re.S		让.也可以匹配多行
re.I		让匹配时忽略大小写
```

#### 实例4:

```
源字符串："Python"
正则表达式："pyt"
匹配方式:re.compile("pyt").findall("Python")
匹配结果： []

源字符串："Python"
正则表达式："pyt"
匹配方式:re.compile("pyt",re.I).findall("Python")
匹配结果： Pyt

源字符串：string="Python"
正则表达式："pyt"
匹配方式:re.compile("pyt",re.I).findall("Python")
匹配结果： Pyt

源字符串：string="""我是阿里云大学
欢迎来学习
Python网络爬虫课程
"""
正则表达式：pat="阿里.*?Python"
匹配方式:re.compile(pat).findall(string)
匹配结果： []

源字符串：string="""我是阿里云大学
欢迎来学习
Python网络爬虫课程
"""
正则表达式：pat="阿里.*?Python"
匹配方式:re.compile(pat,re.S).findall(string)
匹配结果： ['阿里云大学\n欢迎来学习\nPython']
```

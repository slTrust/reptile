### xpath基础

- / 逐层提取
- text() 提取标签下面的文本
- //标签名**  提取所有名为**的标签
- //标签名[@属性='属性值']  提取属性为XX的标签
- @属性名  代表取某个属性值

```
<html>
<head>
<title>
主页
</title>
</head>
<body>
  <p>abc</p>
  <p>bbbvb</p>
  <a href="//qd.alibaba.com/go/v/pcdetail" target="_top">安全推荐</a>
  <a href="//qd.alibaba.com/go/v/pcdetail" target="_top">安全推荐2</a>
  <div class="J_AsyncDC" data-type="dr">
    <div id="official-remind">明月几时有</div>
  </div>
</body>
```

> 分析以下XPath表达式提取的内容：

```
/html/head/title/text()
//p/text()
//a
//div[@id='official-remind']/text()
//a/@href
```

####　实例：

```
提取标题：/html/head/title/text()
提取所有的div标签：//div
提取div中<div class="tools">标签的内容： //div[@class='tools']/text()
```


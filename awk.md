# awk

## 概念

awk则是基于列的文本处理工具，它的工作方式是按行读取文本并视为一条记录，每条记录以字段分割成若干字段，然后输出各字段的值

awk认为文件都是结构化的，也就是说都是由单词和各种空白字符组成的，这里的“空白字符”包括空格、Tab，以及连续的空格和Tab等。每个非空白的部分叫做“域”，从左到右依次是第一个域、第二个域，等等。 $1、$2分别用于表示域，$0则表示全部域

```shell
# 只打印第一个域和第四个域
[root@yyds testsed]# awk '{print $1,$4}' awd.txt 
john.wang 021-11111111
lucy.yang 021-22222222
jack.chen 021-33333333
lily.gong 021-44444444

# 打印全部内容
[root@yyds testsed]# awk '{print $0}' awd.txt    
john.wang       Male    30      021-11111111
lucy.yang       Female  25      021-22222222
jack.chen       Male    35      021-33333333
lily.gong       Female  20      021-44444444    ShangHai
```

## -F 指定打印分隔符

默认情况下awk是使用空白字符作为分隔符的，但是也可以通过-F参数指定分隔符，来区分不同的域（有点像之前学过的cut命令）

```shell
# 把.作为分隔符，$1就是.之前的字符，$2就是.之后的字符
[root@yyds testsed]# awk -F . '{print $1,$2}' awd.txt 
john wang       Male    30      021-11111111
lucy yang       Female  25      021-22222222
jack chen       Male    35      021-33333333
lily gong       Female  20      021-44444444    ShangHai 
```

## 内部变量NF

NF 可以获取文件的列数（即域数）

```shell
# 使用默认分隔符来获取列数
[root@yyds testsed]# awk '{print NF}' awd.txt 
4
4
4
5

# 指定.为分隔符来获取列数
[root@yyds testsed]# awk -F . '{print NF}' awd.txt  
2
2
2
2
```

## 打印固定区域

通过内部变量可以简单地得到每行的列数，而如果在NF之前加上$符号，则代表“最后一列”，这样不管每行有多少列，只要使用$NF就能打印出最后一行

```shell
# 打印最后一列（最后的域）
[root@yyds testsed]# awk '{print $NF}' awd.txt 
021-11111111
021-22222222
021-33333333
ShangHai

# 打印倒数第二列（倒数第二个域）
[root@yyds testsed]# awk '{print $(NF-1)}' awd.txt   
30
25
35
021-44444444
```

## 截取字符串

可以使用substr()函数对指定域截取字符串，该函数的基本使用方法如下：

substr（指定域，第一个开始字符的位置，第二个结束的位置）其中第二个结束的位置可以为空，表示默认输出到该域的最后一个字符

```shell
# 截取第一个域从第六个字符到第一个域最后一个字符
[root@yyds testsed]# awk '{print substr($1,6)}' awd.txt 
wang
yang
chen
gong
```

## 确定字符串的长度

使用内部变量length可以确定字符串的长度

```shell
# 统计全部域的字符串长度
[root@yyds testsed]# awk '{print length}' awd.txt 
30
32
30
41

# 统计第一个域的字符串长度
[root@yyds testsed]# awk '{print length($1)}' awd.txt   
9
9
9
9
```

## 求列和

```shell
# 求年龄的总和
[root@yyds testsed]# awk 'BEGIN{total=0}{total+=$3}END{print total}' awd.txt 
110
 
# 求平均年龄
[root@yyds testsed]# awk 'BEGIN{total=0}{total+=$3}END{print total/NR}' awd.txt 
27.5
```


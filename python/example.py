from this import d


name = "lyj"
age = 25
height = 163
weight_of_lyj = "50kg"
print(name)
print(age)
print(height)
print(name,weight_of_lyj)
print(age)

# 变量加了引号都是字符串
type(name),type(age),type(height),type(weight_of_lyj)

# 多引号作用是引用多行支付
msg = '''床前明月光
疑是地上霜
举头望明月
低头思故乡
'''
print(msg)

# 字符串拼接，必须都是字符串
str1 = "love"
str2 = "lwl"
# 两个变量字符串拼接
str1 + str2
print(str1 + str2)
# 把变量复制多少次再拼接在一起
str1 * 2
print(str1 * 2)

# 布尔类型，用于逻辑判断
a = 3
b = 5
print("a>b is",a > b)
#a > b
#a < b
#print(a > b)
#print(a < b)
if a > b:
    print("a is bigger than b")
else:
    print("a is smaller than b")


# 列表类型List
names = ["lyj","lwl","hyx","lyp","wwj"]
print(names[3])
# 在第三位添加一个新元素
names.insert(3,"yzb")
print(names)
print(names[3])
# 在列表结尾添加一个新元素
names.append("wzl")
names
# 修改列表中的元素
names[1] = "my love lwl"
names
# 删除列表中的元素，两个方法：1，删除下标；2，删除元素值
#names.remove("wzl")
#del names[6]
print(names)
# 判断元素是否在列表中
"lwl" in names

print("Alex金角大王是沙河最靓的仔" * 10)

room = ["lyj","lwl","hyx","wwj","lyp","yzb"]
room.insert(1,"alex")
print(room)
#room.remove("lyj")
del room[0]
room.append("lyj")
print(room)

a = 10
b = 20
c = 1.4
print("result is",a + b)
print(a + c)
print(a - b)
print(a * b)
print(a * c)
print(b / a)
print(a / b)
print(b % a)
print(a ** b)
print(b // a)
print(a == b) 
print(a != b)
#print(a <> b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

a = 10
b = 20
#c = a+b 
d = 1
d += a
print(d)

a = 10
b = 20
print(a > 10 and b > 10)
print(a > 10 or b > 10)
print(not a > b)

a = 10 
b = 20
c = 5
print(a > b and a < c or b > c and a > b and a >c )

room = ["lyj","lwl","hyx","wwj","lyp","yzb"]
print("lyj" in room)
print("lyj" not in room)
s = "我是三水最靓的仔"
print("三水" in s)

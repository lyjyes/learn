# 集合  set   无序且不重复

# set1 = {1,2,3,4,5}
#
#
# five_men_fight_bg = {"mingzhe.li", "Alex", "佩奇", "Old_Shang", "智哥", "black_girl"}
#
# happy_day = {"唐艺昕", "李孝利", "black_girl", "刘诗诗", "李沁", "柳岩", "mingzhe.li"}
#
#
# # 要找出，同时参演了，这两部电影的人，都有谁。（交集）
#
# print(five_men_fight_bg.intersection(happy_day))
#
# print(five_men_fight_bg & happy_day)
#
#
# # 这两部电影中，一共包含了有，哪些演员。(并集)
# print(five_men_fight_bg.union(happy_day))
#
# print(five_men_fight_bg | happy_day)
#
#
# # 参演了抗战片，五男大战黑姑娘的演员中，谁没有参演，开心的一天。(差集)
#
# print(five_men_fight_bg.difference(happy_day))
#
# print(five_men_fight_bg - happy_day)
#
#
#
# # 哪些演员，只参演了一部电影。(交叉补集)
# print(five_men_fight_bg.symmetric_difference(happy_day))
#
# print(five_men_fight_bg ^ happy_day)


# set1 = {1,2,3,1,2,3,4,4,4,4,5,6,7}
# print(set1)

# list1 = [1,2,3,1,2,3,4,4,4,4,5,6,7]
# print(list(set(list1)))


# 流程控制结构
# 顺序结构
# 选择结构   分支结构  条件语句
# 循环结构

# 循环嵌套


# flag = True
# #控制楼层
# for floor in range(1,6):
#     print(f"欢迎来到第{floor}层")
#
#     if floor == 3:
#         print("嘿，还不让我进了，可惜啊可惜")
#         continue
#
#     #控制房间号
#     for room in range(1,9):
#         print(f"{floor}0{room}")
#
#         if floor == 4 and room == 4:
#             print("啊~~~我的草原我的马呀，你*******")
#             flag = False
#             break
#
#     if flag != True:
#         break
#             # exit()
#
#         # 循环控制保留字
#         # continue：跳过本次循环，直接开始下一次循环
#         # break：跳出循环


# 算法
# hight = 100  # 原始高度

# distance = 0  # 记录经过多少米
#
# for i in range(10):
#     distance = distance + hight
#
#     hight /= 2   # hight = hight / 2
#
#     if i == 9:
#         break
#     distance += hight
# print(f"共经过{distance}米")


# 年会抽奖
import faker
import random

alex = faker.Faker(locale="zh_CN")  # en_US   zh_YW

staff_list = []

for i in range(1, 301):
    staff_list.append(alex.name())

level = [30, 6, 3]

for i in range(3):
    winner_list = random.sample(staff_list, level[i])
    for winner in winner_list:
        staff_list.remove(winner)
    print(f"获得{3 - i}等奖的是：{winner_list}")
print(len(staff_list))

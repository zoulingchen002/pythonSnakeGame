# shift + enter 快捷换行
# alt+ shift + 方向键  当前行上移或者下移
name = '顾清寒'
sex = '女'
grade = 11.01
# 占位符去插入字符串
message = "角色姓名：%s，角色性别：%s，角色评分：%.2f" % (name,sex,grade )
print(message)
# f标记字符串，然后字符串内可以使用{变量名} 去对字符串插入变量数据
fmsg = f"角色姓名：{name}，角色性别：{sex}，角色评分：{grade}"
print(fmsg)
# 不使用变量，使用表达式
bdsmsg = "1 + 2的值为：%d" % (1+2)
print(bdsmsg)
bdsmsg2 = f"1 + 2的值为：{1+2}"
print(bdsmsg2)

# # 键盘输入
# print("请输入角色名称：")
# input_str = input()
# print("角色名称是：%s" % input_str)
#
# intp = input("你的名字")
# print(f"你的名字：{intp}")
#
# age = 16
# if age>30 or age<15 :
#     print("年龄不在15到30之间")
# print("真不错")
# print("真好")


# if int(input("请输入一个整数")) in {1,2,3} :
#     print("在范围1内")
#
# elif int(input("请再输入一个整数")) >= 4 :
#     print("在范围2内")
# else :
#     print("不在范围内")








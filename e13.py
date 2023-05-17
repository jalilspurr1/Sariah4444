chenji = float(input("请输入一个成绩分数："))
if (chenji >= 90 and chenji <= 100):
    dengji = ("优秀")
elif (chenji >= 70 and chenji < 90):
    dengji = ("良好")
elif (chenji >= 60 and chenji < 70):
    dengji = ("及格")
elif (chenji >= 0 and chenji < 60):
    dengji = ("不及格")
else:
    dengji = ("成绩有误")

print(dengji)

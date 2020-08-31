import ga
print('欢迎使用遗传算法工具箱！')
nums = input('请输入初始种群大小：')
length = input('请输入染色体长度：')
ge = ga.Initialization(int(nums), int(length))
print('初始化种群成功！')

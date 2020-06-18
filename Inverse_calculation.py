x=int(input("请输入数字:"))
for i in range(96):
    if((i*x)%17==1):
        print(i)
        break

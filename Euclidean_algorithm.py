x=int(input("请输入数字:"))
y=int(input("请输入数字:"))
for i in range(26):
    if(((i*x)%26)==y):
        print(i)
        break

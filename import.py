import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍截值: ')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True :
    count = count + 1
    x = input('輸入數字: ')
    x = int(x)
    if r == x:
        print('終於猜對了!')
        print('這是你猜的第',count, '次')
        break
    elif x > r:
        print('比答案大')
    elif x < r:
        print('比答案小')
    print('這是你猜的第',count, '次')

      
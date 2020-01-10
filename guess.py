#產生一隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話印出"終於猜對了"
#猜錯的話 要告訴他 比答案大或小
import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count +=1  #count = count + 1
	one = input('請猜一個數字:')
	one = int(one)
	if one == r:
		print('恭喜你,猜對了')
		print('這是你猜的第', count, '次')
		break
	elif one > r:
		print('比答案大')
	elif one < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
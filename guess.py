#產生一隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話印出"終於猜對了"
#猜錯的話 要告訴他 比答案大或小
import random
r = random.randint(1,100)
while True:
	one = input('1~100請猜一個數字:')
	one = int(one)
	if one == r:
		print('恭喜你,猜對了')
		break
	elif one > r:
		print('比答案大')
	elif one < r:
		print('比答案小')
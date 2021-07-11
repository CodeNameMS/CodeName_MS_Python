# import random # 실행 시 1보다 작은 소수로 나오는 이유는 철저한 계산에 의해서임
# i=0
# for i in range(5):
#     print(i," ",random.random())

# import random
# i=0
# for i in range(5):
#     print(i," ",int(random.random()*100))

# import random
# i=0
# for i in range(5):
#     print(i," ",random.randrange(1,10)) #랜덤의 범위에 실수는 안됨. 정수만 가능


#  Computer 는 랜덤하게 가위,바위,보 결정, 사용자는 가위,바위,보 중 선택하여
# 승,패,무 결과를 출력하시오


#  간단한 로또 프로그램 만드시오(중복되는값이 체크) / 리스트1~45까지 랜덤



# import random
# i=0
# com={1:'가위',2:'바위',3:'보'}
# while True :
#     mjb = input("가위 바위 보 중 입력하세요 : ")
#     if mjb=='가위' : mjb=1
#     elif mjb=='바위' : mjb=2
#     elif mjb=='보' : mjb=3

#     for i in range(1) :
#         print("컴퓨터 :",com.get(random.randrange(1,4)))
# # -----------------------------------------------------------
# while True :
#     import random
#     computer = random.randrange(0,3)
#     user=int(input("메뉴선택 : 0.가위   1.바위  2.보\n>>> "))
#     menu=("가위","바위","보")
#     print("Computer - %s  VS  User - %s"%(menu[computer],menu[user]))
#     if computer == user :
#         print("결과 : Draw !!!")
#     elif computer - user == -1 or computer - user == 2:
#         print("결과 : You win  !!!")
#     else : 
#         print("You lose !!!")
#     select= input("계속 하려면 Y(y) / 그만하려면 N(n)\n>>>  ")
#     if select == "y" or select == "Y" :
#         continue
#     elif select== "n" or select == "N" :
#         break
#     else :
#         print("잘못누르셨습니다. 종료하겠습니다")
#         break

# 로또 프로그램
# def lotto_func() :
#     import random
#     lotto=[]
#     while True :
#         number = random.randrange(1,46)
#         if lotto.count(number) == 0 : #새로운 번호가 맞는가 확인
#             lotto.append(number)
#         if len(lotto) >= 6 :
#             break
#     lotto.sort()
#     print("이번주 행운의 번호 :",lotto)

# i=0
# for i in range(1) :
#     lotto_func()

# n1= 10 
# n2=0 
# try: 
#  result=n1/n2 
#  print("%d / %d = %d" %(n1,n2,result)) # try가 성공하면 except를 실행하지 않음.
# except: 
#  print("0으로 나눌 수 없습니다.") 
# print("프로그램 정상 종료!!") 

# while True:
#     try : 
#         n1= int(input("정수1: ")) 
#         n2= int(input("정수2: ")) 
#         break
#     except: 
#         print("숫자로만 입력하세요~") 
#         print("%d / %d = %d" %(n1,n2,result)) 
# try: 
#     result=n1/n2 
#     print("%d / %d = %d" %(n1,n2,result)) 
# except: 
#     print("0으로 나눌 수 없습니다.") 
#     print("프로그램 정상 종료!!") 

s = input("정수: ") 
try : 
 point = int(s) 
 print(150 /point) 
except ValueError: 
 print("숫자로만 입력하세요~") 
except ZeroDivisionError: 
 print("0으로 나눌 수 없습니다.") 
except: 
 print("알수 없는 오류 발생. 점검 후 조치하겠습니다..") 
print("프로그램 정상 종료!") 
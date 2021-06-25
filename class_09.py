# for i in range(1 , 11 , 1) :
#     if i %2 == 0:
#         print("i = " , i , ": 값 확인")
# print("다음 문장")

# for i in range(0 , 11 , 2) :
#     print("i = " , i , ": 값 확인")

# for i in range(10 , -1 , -1) :
#     print(i , ": 10 ~ 0 까지 출력")

# Sum = 0
# for i in range(1, 11, 1) :
#     if i <= 10 :
#         Sum = Sum+i
#         print("1부터 10까지 합 계산 : %d" %Sum)

# for i in range(1,11,1):
#     print(i,end=" ")

# for i in range(1, 31, 1):
#     print(i,end="\t")
#     if i%5 == 0 : 
#         print("\t")

# i , Sum = 0 , 0
# start , en , grow = 0 , 0 , 0
# start = int(input("시작값 입력 : "))
# en = int(input("끝값 입력 : "))
# grow = int(input("증가값 입력 : "))
# for i in range ( start , en + 1 , grow ):
#     Sum = Sum + i
#     print("%d에서 %d 까지 %d씩 증가한 값의 합 : %d" % (start , en , grow , Sum))

# for i in range(0,10): #초기값, 끝값만 지정, 증감값은 안쓰면 양수 1로 고정
#     print(i)
# --------------------------------------
# for i in range(10): #초기값,증감값 제외 끝값만 지정 초기값 Defalt는 0
#     print(i)
# # --------------------------------------
# for i in range(10,2): # 
#     print(i)
# # --------------------------------------
# for i in range(0,10,2): #일반적인 경우
#     print(i)

# a = int(input("시작 값:"))
# b = int(input("끝 값:"))
# c = int(input("증가 값:"))
# for i in range(a,b,c) :
#      if i%7 == 0 :
#          print(i)
# # ==================================
# sum_=0
# for i in range(1,101,1) :
#     if i%3 == 0 & i%5 ==0 :
#         sum_+=i
#         print(sum_,end=("\t"))
#         if i%5 == 0 :
#             print("\n")
# # ==================================
# su1 = int(input("첫 번째 수를 입력하세요 : "))
# su2 = int(input("두 번째 수를 입력하세요 : "))
# sum_ = 0
# if su1 < su2 :
#     for i in range(su1,su2,1) :
#         sum_ += i
#         print(sum_)     
# else :
#     for i in range(su2,su1,1) :
#         sum_ += i
#         print(sum_)
# # =====================================
# last_ = 10
# sum_ = last_
# print("마지막 저금액 : %d원" %last_)
# print("1일 째 최종 금액 : %d원\n" %sum_)
# for i in range(0,30,1) :
#     last_*=2
#     sum_ += last_
#     # if i ==  29 :
#     print("마지막 저금액 : %d원" %last_)
#     print("%d일 째 최종 금액 : %d원\n" %(i+1,sum_))

# 첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 동안 
# 저축한 금액중 마지막 저금액을 구하시오.
# (첫날 10, 둘째날 20 , 셋째날 40 . . .무조건 2배씩 증가되는 값이다)


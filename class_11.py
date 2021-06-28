# i=0
# while i<5:
#     print(i, "종속 문장")
#     i+=1
# else:
#     print("조건식이 거짓일 경우 : ",i)
# print("다음 문장")

# i=1
# flag = True
# while flag:
#     print(i, "종속 문장",end=" ")
#     if i == 10:
#         flag = False
#     i+=1

# i=0
# while True:
#     if i == 3:
#         print("3 출력")
#         break
#     print(i,"출력")
#     i+=1
# print("다음 문장")

# i=0
# while i<5:
#     i+=1
#     if i == 3:
#         continue
#         print("3출력")
#     print(i,"출력")
# print("다음 문장")

# num,result,i=0,0,1
# while True:
#     num = int(input("1~10사이의 숫자 입력 : "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     break
# else:
#     print("next...")
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합 : ",result)

# for i in range ( 0 , 3 , 1):
#     for k in range ( 0 , 5 , 1):
#         if k == 3:
#             break
#         print("(i : %d\tk : %d)" % (i , k ))

# i=0
# while i<3 :
#     k=0
#     while k<3 :
#         print("i : %d\tk : %d" %(i, k))
#         k+=1
#         if k==3 :
#             break
#     i+=1
#중첩 while문으로 변경

# 다 먹은날 x일, 쥐는 총 x마리

# ssal = 100 * 1000
# mouse = 2
# mouse_eat = 20
# cnt = 0

# while ssal > 0 :
#     ssal = ssal - (mouse * mouse_eat)
#     cnt+=1
#     if cnt%10 == 0 :
#         mouse *= 2
# print("쌀이 다 떨어진 날 : %d, 쥐는 총 %d마리" %(cnt, mouse))

# insult = int(input("요금을 투입하세요\n>"))
# while insult>0 :
#     print("{:=^30}".format("커피 자판기"))
#     print("1.커피(200)\t2.코코아(250)\t3.반환\t4.종료")
#     menu = int(input("메뉴를 선택하세요\n>"))
#     if menu == 1 :
#         print("커피를 선택하셨습니다.")
#         insult = insult-200
#         if insult > 0 :
#             print("거스름돈은 %d원 입니다. 감사합니다" %insult)
#         else :
#             print("감사합니다.")
#             break
#     if menu == 2 :
#         print("코코아를 선택하셨습니다.")
#         insult = insult-250
#         if insult > 0 :
#             print("거스름돈은 %d원 입니다. 감사합니다" %insult)
#         else :
#             print("감사합니다.")
#             break
#     if menu == 3 :
#         print("반환을 선택하셨습니다.")
#         insult = insult
#         if insult > 0 :
#             print("거스름돈은 %d원 입니다. 감사합니다" %insult)
#             break
#         else :
#             print("반환 할 금액이 없습니다.")
#             break
#     if menu == 4 :
#         print("종료를 선택하셨습니다.")
#         if insult != 0 :
#             print("거스름돈은 %d원 입니다. 감사합니다" %insult)
#             break
#         else :
#             break
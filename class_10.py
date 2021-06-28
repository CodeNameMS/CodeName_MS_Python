# money=10
# save =10 #money
# for day in range (2,31) :
#     money*=2
#     save+=money
# print("마지막 입금액 : %d원"%money)
# print("한달 총 저축액 : %d원"%save)

# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print("i : ",i)

# ls = [1,2,3,4,5,6,7,8,9,10]
# for i in ls:
#     print("i : ",i)
# for i in ls:
#     print(i,end=" ")

# st = "Hello Python"
# for i in st:
#     print("i : ",i)

# st = "it is a fun Python class"
# all = 0
# a = 0
# s = 0
# for i in st :
#     if i=='a' :
#         a+=1
#     elif i=='s' :
#         s+=1
#     all+=1
# print("총 개수 : %d" %all)
# print("a 개수 : %d" %a)
# print("s 개수 : %d" %s)

# print("{0}+{1}={2}".format(10,2,10+2))
# print("{2}+{1}={0}".format(10,2,10+2))
# print("{}+{}={}".format(10,2,10+2)) # 순서값을 지정하지 않으면 차례대로
# print("{:,}".format(1000000)) # :를 기준으로 사용
# print("{:<10},왼쪽정렬,{:0<10}".format('첫번째','두번째'))
# print("{:>10},오른쪽정렬,{:9>10}".format('첫번째','두번째'))
# print("{:^10},가운데정렬,{:5^10}".format('첫번째','두번째'))

# for i in range ( 0 , 3 , 1):
#     for k in range ( 0 , 5 , 1):
#         print("이중 for 문 (i : %d\tk : %d)" % (i , k ))
# print("========================== 구 구 단 ==========================")
# print("2단\t3단\t4단\t5단\t6단\t7단\t8단\t9단")
# print("==============================================================")
# for i in range ( 1 , 10, 1 ):
#     print(end="\n")
#     for k in range ( 2 , 10 , 1):
#         print("%d*%d=%d" %(k,i,k*i),end=("\t"))

# for i in range (0, 5, 1) :
#     print("상위포문 %d일 때 하위 포문 :" %i,end=(" "))
#     for k in range(0, 5, 1) :
#         j = i*k
#         print("%d" %j,end=(" "))
#     print(" ")

# for i in range(1,22,5) :
#     print(i,end="\t")
#     for j in range (1,5) :
#         print(i+j,end="\t")
#     print()

# for i in range(5) :
#     for j in range(1,6) :
#         print(j+i*5,end="\t")
#     print()

# i=0
# while i<5:
#     print(i, "종속 문장")
#     i+=1
# print("다음 문장")

# for i in range(5) :
#     print(i, "종속 문장")
# print("다음 문장")

# i=1
# odd,even=0,0
# while i<=10:
#     if i % 2 ==0:
#         even+=i
#     else:
#         odd+=i
#     i+=1
# print("1-10 짝수의 합 : ",even)
# print("1-10 홀수의 합 : ",odd)


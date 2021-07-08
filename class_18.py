# def reverseCode():
#     result,temp = 0,0
#     result = int(input("수 입력 : "))
#     while True:
#         temp = int(result%10)
#         result = int(result/10)
#         print(temp,end="")
#         if not result: break;
# print("프로그램 시작")
# reverseCode()
# print("\n프로그램 종료")

# sel = 0
# sel = int(input("음료 선택\n1.콜라\n2.핫6\n3.포카리\n입력 : "))

# def reverseCode():
#         if sel == 1 : print('콜라 등장')
#         elif sel == 2 : print('핫6 등장')
#         elif sel == 3 : print('포카리 등장')
#         else : print('만들어 드세요^^')
# reverseCode()
# if sel >=1 and sel <=3:
#             print("맛있게 드세요^^")

# def calc():
#     result=0
#     su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
#     if op=='-' :
#         result = su1-su2
#         print(su1,'-',su2,'=',result)
#     elif op=='+' :
#         result = su1+su2
#         print(su1,'+',su2,'=',result)
#     elif op=='/' :
#         result = su1/su2
#         print(su1,'/',su2,'= %.2f' %result)
#     elif op=='*' :
#         result = su1*su2
#         print(su1,'*',su2,'=',result)
# calc()

# def calc():    
#     su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
#     if op == "+": result = su1+su2
#     elif op == "-": result = su1-su2
#     elif op == "*": result = su1*su2
#     elif op == "/": result = su1/su2
#     print(su1,'+',su2,'=',result)
# calc()

# def cal(su1,op,su2):
#     result=0
#     result = su1+su2
#     print(su1,'+',su2,'=',result)
# su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
# cal(su1,op,su2)

# def cal(su1,op,su2):
#     result=0
#     result = su1+su2
#     print('cal 실행')
#     return result # return 함수를 종료하고 이때 반환할 값이 있다면 돌려주는 역할
# su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
# result=cal(su1,op,su2)
# print(su1,'+',su2,'=',result)
# print("다음 문장 실행")

# def showAvrg(a,b,c):
#     print("{}와 {}의 평균".format(a,b))
#     print("값은 {}입니다".format(round(c,1)))
# def avrg(j,k):
#     total=j+k; f=total/2
#     return f
# i=2; j=3
# f=avrg(i,j)
# showAvrg(i,j,f)
# print("다음 문장 실행")

# def func2(a,b):
#     a+=5; b*=10;
#     print("func2 : a={}, b={} ".format(a,b))
# def func1():
#     a=5;b=10
#     func2(a,b)
# print("func1 : a={}, b={}".format(a,b))
# func1()

# def aa(a):
#     if a==1:
#         print('1입력')
#     print('다음 문장 실행')
# a=aa(1)
# print("리턴 값 : ",a)
# print('프로그램 종료')

# def aa(a):
#     if a==1:
#         return
#         print('1입력')
#     print('다음 문장 실행')
# a=aa(1)
# print("리턴 값 : ",a)
# print('프로그램 종료')

# def move():
#     print('이동')
# def attack():
#     print('공격')
# def defense():
#     print('방어')
# move()
# attack()
# defense()

# def a(a):
#     if a==1:
#         pass
#     else :
#         print("1이 아니에요")
# a(1)

# # 짝,홀수를 구분하는 함수
# def hol() :
#     a = int(input("수를 입력하세요 : "))
#     if a%2 == 0 :
#         print("짝수")
#     else :
#         print("홀수")
# hol()

# # 3의 배수를 판별하는 함수
# def bae() :
#     if su%3 == 0 :
#         print("3의 배수")
#     else :
#         print("3의 배수 아님")
# su = int(input("수를 입력하세요 : "))
# bae()

# # 계산기 입력,출력,연산기능 나누기
# def input_data() : 
#     su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
#     func()
# def output_data(su1,op,su2,result) :
#     print(su1,op,su2,'=',result)
# def func(su1,op,su2,result) :
#     if op == '+' : result = su1+su2
#     elif op == '-' : result = su1-su2
#     elif op == '*' : result = su1*su2
#     elif op == '/' : result = float(su1/su2)
#     else : print("잘못 입력함")
#     output_data(su1,op,su2,result)
#     return result
# func(su1,op,su2,result)
# output_data(su1,op,su2,result)

# # 정답
# def output_data(num1,op,num2,result):
#     print(num1,op,num2,"=",result)
# def calc_func(num1,op,num2):
#     if op == '+' : result= num1+num2
#     elif op == '-' : result= num1-num2
#     elif op == '*' : result= num1*num2
#     elif op == '/' : result= num1/num2
#     output_data(num1,op,num2,result)
# def input_data():
#     num1,op,num2 =int(input("정수1입력 : ")),input("부호 입력 : "),int(input("정수2입력 : "))
#     calc_func(num1,op,num2)
# input_data()

# # 숫자 거꾸로 출력()
# result,temp,i = 0,0,0
# result = int(input("수 입력 : "))
# while True:
#     temp = int(result%10)
#     result = int(result/10)
#     if not result: break
#     i+=1
# temp1 = temp(10**i)
# print(temp)
# print(temp1)
# print("\n프로그램 종료")        

# def reverseCode():
#     reverse=0    
#     result = int(input("수 입력 : "))
#     while True:

#         temp = result%10
#         reverse*=10
#         reverse+=temp        
#         result = result//10
#         if not result:
#              return reverse
# print(reverseCode())

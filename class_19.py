# def func1() :
#     print("func1의 a : %d" % a)
# def func2() :
#     print("func2의 a : %d" % a)
# a =200 #전역 변수
# func1()
# func2()

# def func1() :
#     a = 123
#     print("func1의 a : %d" % a)
# def func2() :
#     print("func2의 a : %d" % a)
# a =200 #전역 변수
# func1()
# func2()

# def func1() :
#     global a
#     a = 1222
#     print("func1의 a : %d" % a)
# def func2() :
#     print("func2의 a : %d" % a)
# a =200 #전역 변수
# func1()
# func2()

# def sum_func(x1,x2,x3 = 100) :
#     result = 0
#     result =x1 + x2 + x3
#     return result
# def display():
#     Sum = 0
#     a,b,c = 10 , 20 , 30
#     Sum = sum_func(a , b)
#     print("매개변수 2개 함수 호출 : " , Sum)
#     Sum = sum_func(a ,b , c)
#     print("매개변수 3개 함수 호출 : " , Sum)
# display()

# def alba(day=30,time=8,won=8500):
#     result = day * time * 8500
#     return result
# def display():
#     num = int(input('1.기본급\n2.일한 날짜 입력\n'))
#     if num == 1:
#         result = alba()
#     elif num==2:
#         day = int(input('일한 날짜 입력(몇일) : '))
#         result=alba(day)
#     print("당신의 급여 :{}원 입니다".format(result))
# display()

# def sum_func(*par) :
#     result = 0
#     print("type : ",type(par))
#     print("par : ",par)
#     for num in par :
#         result = result + num
#         print("num : %d" % num)
#     return result
# Sum = 0
# Sum = sum_func(10 , 20)
# print("매개변수 2개 함수 : %d" % Sum)
# Sum = sum_func(10 , 20 , 30 , 40)
# print("매개변수 4개 함수 : %d" % Sum)

# def dic_func(**par) :
#     print("type(par):",type(par))
#     for k in par.keys() :
#         print("{} : {} 명입니다".format(k , par[k]))
# dic_func(똭뚝뽹 = 123 , 꿔익꿔익 = 8 , test = '테스뚜')

# def change(a,b,c):
#     return a+10,b+20,c+30
# a,b,c=change(10,20,30)
# d = change(10,20,30)
# print("a,b,c :",a,b,c)
# print("d:{}, type{}".format(d,type(d)))

# def swap(x,y):
#     return y,x
# a=10; b=20
# print("바꾸기 전 : ",a,b)
# a,b=swap(a,b)
# print("바꾼 후 : ",a,b)

# swap = lambda a,b:[b,a] #람다 함수는 변수값을 변환하여 반환하는 역할을 함
# a=swap(10,20)
# print("swap 결과",a)

# lam = lambda a:a*10
# hap = lambda a,b:a+b
# noData = lambda : print("인자값 없는 람다")
# print(lam(10))
# print(hap(5,10))
# noData()

# def startGame():
#     print("Game Start!!!!")
# def test():
#     print("1.게임 시작")
#     print("2.게임 종료")
#     num = input("선택 : ")
#     if num=="1":
#         startGame()
#     elif num=="2":
#         end()
# end = lambda :print("게임 종료")
# test()

# a,op,b = int(input("첫수:")),input("연산:"),int(input("두수:"))
# hap = lambda a,b:a+b
# avg = lambda a,b:float(a/b)
# double = lambda a,b:a*b
# sub = lambda a,b:a-b
# if op=='+' : print(hap(a,b))
# elif op=='-' : print(sub(a,b))
# elif op=='*' : print(double(a,b))
# elif op=='/' : print(avg(a,b))

# def transfer(dst,su=0,won=500):
#    for i in range(0,su):
#        won*=2
#    return "{}까지 요금 :{}입니다".format(dst,won)
# def disply():
#     num = int(input('1.환승안함\n2.환승 함\n3.장거리\n'))
#     destination = input('목적지 입력 : ')
#     if num == 1:
#         result = transfer(destination)
#     elif num==2:
#         su = int(input('환승 수 입력 : '))
#         result = transfer(destination,su)
#     else:
#         result = transfer(destination,1,10000)
#     print(result)
# disply()

# import math 
 
# print(math.pi) 
# print(math.factorial(5)) # 5!= 5x4x3x2x1 
# print(math.sqrt(5)) 
# print(math.log10(2)) 

# from math import factorial, sqrt, pi 
 
# print(factorial(5)) 
# print(sqrt(5)) 
# print(log10(2)) 

# from math import factorial, sqrt, pi 
# import math 
 
# print(factorial(5)) 
# print(sqrt(5)) 
# print(math.log10(2)) 
# print(math.log10(3)) 
# print(math.gcd(12,18)) #최대공약수 

# import statistics 
 
# points = [65, 75, 55] 
# print('평균 : ', statistics.mean(points)) 
# print('분산 : ', statistics.variance(points)) 
# print('표준편차 : ', statistics.stdev(points)) 
# #----------------------------------------- 
# import statistics as st 
 
# points = [65, 75, 55] 
# print('평균 : ', st.mean(points)) 
# print('분산 : ', st.variance(points)) 
# print('표준편차 : ', st.stdev(points))

# import calculator as cal #모듈명은 숫자로 시작x
# from calculator import info 
 
# print("1인치 : %.2fcm"%cal.inch) 
# print("1~10까지의 누적합:",cal.calc_sum(10)) 
 
# info() 
# info() 
# info() 
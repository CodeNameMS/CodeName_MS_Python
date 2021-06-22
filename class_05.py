#  flt = 123.567
#  print("round(flt) : " , round(flt))
#  print("round(flt,1)" , round(flt,1))
#  print("round(flt,2) : " , round(flt,2)) #round함수는 -1등 을 넣어 정수자리에서도 반올림이 가능하다.

# fit = 2.6
# flo = 13
# total = 5.0023 + (fit*flo)
# print("건물의 총높이는 %.3fm 입니다." %round(total,3))

# avg_height=260
# fl_cnt=14
# one_fl=500.23
# result=avg_height*(fl_cnt-1)+one_fl
# meter=result/100
# print("호텔의 총 높이 : %.3fm"%(round(meter,3)))

# avg_time = 100 / 11.27
# hour = 3600
# result = (avg_time * hour)/1000
# print("1시간 후 총 %.2fkm를 갔습니다." %(round(result,2)))

# sec_time=60*60 # 1시간을 초단위로 환산
# result=sec_time/11.27 # 1시간에 11.27초가 몇번들어가는지 계산
# meter = result *100 # 위의결과에 100m를 곱해주면 총거리
# kilo =meter /1000 #위결과는 m단위이므로 km 단위로 환산
# print("1시간후 이동거리 : %.2fkm"%kilo)

# flt = 123.123
# print("%.3f + %.3f = %.3f" % (flt,321.321,flt+321.321))
# print(flt,"+",321.321,"=",flt+321.321)
# ch1,ch2 ,ch3= "파",'2',"썬"
# print("%c + %c + %c = %s"%(ch1,ch2,ch3,ch1+ch2+ch3))
# print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3)
# str_1 = "python "; str_2 = "test"
# str_3 = str_1 + str_2
# print("%s + %s = %s" % (str_1,str_2,str_1+str_2))
# print(str_1,"+",str_2,"=",str_1+str_2)

# 피연산자            +      피연산자
# 숫자(정수,실수)            숫자(정수,실수)  -> 덧셈 연산
# ----------------------------------------------------------------
# 리스트                        리스트             -> 하나로 합쳐짐(업데이트 연산)
# 튜플                          튜플                -> 하나로 합쳐짐(업데이트 연산)
# 문자열                       문자열             -> 하나로 합쳐짐(업데이트 연산)

# ※ 리스트 ,튜플, 문자열 -> 시퀀스형 자료형 (시퀀스형 자료형의 특징은 인덱스를 사용)

# A=10
# B=5
# print("type :",type(A<B));print("type :",(A<B))
# num = 100;print("type : %s" % type(num))
# flt = 321.321;print("type : %s" % type(flt))
# ch = "A ";print("type : %s" % type(ch))
# st = "test";print("type : %s" % type(st)) 

# num = 100
# print("type : %s\tid : %s" % (type(num),id(num))) #id 함수는 같은 변수를 가리키는지 확인하는데 사용
# num = 321.321
# print("type : %s\tid : %s" % (type(num),id(num)))
# num = "A"
# print("type : %s\tid : %s" % (type(num),id(num)))
# num = "test"
# print("type : %s\tid : %s" % (type(num),id(num))) 

# st1 = "Python"
# st2 = "Test"
# su = 100
# flt = 1.11
# num = '100'
# print(flt+su)
# print(st1 + st2)
# # print(su+num)

# su = 100
# print('type(su) : ',type(su))
# print('type(str(su)) : ',type(str(su)))
# print('type(float(su)) : ',type(float(su)))

# su = 100
# num = '100'
# flt = "1.111"

# print(su+int(num))
# print(su+float(flt))
# print(str(su)+num)    # 모든 데이터(변수)는 문자열로 데이터변환이 가능
                        # 문자열도 숫자인 경우에만 변환 가능

# print("숫자 입력")
# num1 = input()
# print("입력 받은 값 : ", num1)

# print("이름 입력")
# name = input()
# print("나이 입력")
# age = int(input())
# print(name,"님의 나이는",age,"입니다")
# print("%s님의 나이는 %d살 입니다."%(name,age))

# print("두 수의 합을 구해 줍니다")
# print("두 수 입력")
# num1 = int(input())
# num2 = int(input())
# num3 = num1 + num2
# print("두 수의 합 ", num1,"+",num2,'=',num3)
# print("num1 type : ",type(num1))
# print("num2 type : ",type(num2))
# print("num3 type : ",type(num3))

# num1 = int(input())
# num2 = int(input())
# result = num1 + num2
# print(num1, "+", num2, "=", result) 
# result = num1 - num2
# print(num1, "-", num2, "=", result)
# result = num1 * num2
# print(num1, "*", num2, "=", result) 
# result = num1 / num2
# print(num1, "/", num2, "=", result) 

# print("문자열 입력")
# name = input()
# print("정수 입력")
# age = int(input())
# print("실수 입력")
# flt = float(input())
# print("name 값: ",name,"\t type : ",type(name))
# print("age 값: ",age,"\t type : ",type(age))
# print("flt 값: ",flt,"\t type : ",type(flt))

# name = input("이름을 입력 하세요 : ")
# age = int(input("나이를 입력 하세요 : "))
# addr = input("주소를 입력 하세요 : ")
# print("이름 : ",name,"\n나이 : ",age,"\n주소 : ",addr)

# year = int(input("올해의 년도를 4자리로 입력하세요 : "))
# age_year = int(input("당신이 태어난 년도를 4자리로 입력하세요 : "))
# age = (year - age_year)+1
# print("당신의 나이는 %d살 입니다." %age)
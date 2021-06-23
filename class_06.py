# obj_1 = float(input("첫 번째 물건의 무게를 입력하시오 : "))
# obj_2 = float(input("두 번째 물건의 무게를 입력하시오 : "))
# elv = 600 - (obj_1+obj_2)

# print("현재 엘리베이터의 허용무게는 %.2fkg입니다." %elv)

# height = float(input("키를 입력하세요 : "))
# std_weight = (height - 100) * 0.9
# print("표준체중은 %.1f입니다." %weight)

# height = float(input("키를 입력하세요 : "))
# my_weight = float(input("현재 체중을 입력하세요 : "))
# std_weight = (height - 100) * 0.9
# result = (my_weight / std_weight)*100

# print("표준 체중은 %.2fkg이고 비만도는 %.2f%%입니다." %(std_weight, result))

# Name = input("학생 이름 입력 : ")
# Kor = float(input("국어 점수 입력 : "))
# Eng = float(input("영어 점수 입력 : "))
# Mat = float(input("수학 점수 입력 : "))
# Sum = Kor+Eng+Mat
# Avg = Sum/3
# print("=================학생 정보==================")
# print("이름\t국어\t영어\t수학\t합계\t평균")
# print("%s\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f"%(Name,Kor,Eng,Mat,Sum,Avg))

# num1 = 9; num2 = 2
# print(num1 , " + " , num2 , " = " , num1 + num2)
# print(num1 , " - " , num2 , " = " , num1 - num2)
# print(num1 , " * " , num2 , " = " , num1 * num2)
# print(num1 , " / " , num2 , " = " , num1 / num2)
# print(num1 , " // " , num2 , " = " , num1 // num2)
# print(num1 , " % " , num2 , " = " , num1 % num2)
# print(num1 , " ** " , num2 , " = " , num1 ** num2)

# su1=3.1; su2=3
# print("su1 >= su2 : ",(su1 >= su2))
# print("su1 <= su2 : ",(su1 <= su2))
# print("su1 == su2 : ",(su1 == su2))
# print("su1 != su2 : ",(su1 != su2))

# su1 = su2 = 5
# su1+=1
# print("su1 + 1 = " ,su1) #6
# su1-=1
# print("su1 - 1 = ",su1) #5
# su1*=su2
# print("su1 * su2 = ",su1) #25
# su1//=su2
# print("su1 // su2 = ",su1) #5
# su1%=su2
# print("su1 % su2 = ",su1) #0

# su1 = 5
# su2 = 3
# su1**=su2 #125
# su1-=2 #123
# print("su1 / 4 = ",su1 / 4) #30.75
# print("su1 // 4 = ",su1 // 4) #30
# print("su1 % 4 = ",su1 % 4) #3

# print(0 and 0," : ",False and False)
# print(1 and 0," : ",True and False)
# print(0 and 1," : ",False and True)
# print(1 and 1," : ",True and True)
# print("not : ",not(0 or 0)," : ",not(False or False))
# print("not : ",not(1 or 1)," : ",not(True or True))

# a=20
# b=10
# print(False or (a+b))
# print(True or (a+b))
# print(False and (a+b))
# print(True and (a+b)) #논리연산자는 불 연산자가 아닌 계산연산자가 오면 정수를 출력

# 비트부정(~)의 경우 양수(+) -> 음수(-)의 경우 1이 더해지고 음수(-) -> 양수(+)의 경우 1이 빼진다.
# num1 = 3
# num2 = 5
# result1 = num1 | num2
# result2 = num1 & num2
# result3 = num1 ^ num2
# result4 = ~num1
# result5 = ~num2
# result6 = num1>>2
# result7 = num1<<2
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)

# 연산자 우선순위
# 논리연산자를 기준으로 좌/우를 구분하면 좀 더 쉽다.

# arr = [1,2,3,4,5]
# na = int(input("찾을 숫자 입력 : "))
# if na in arr:
#     print("arr : ",arr,"찾는 숫자가 존재 합니다 : ",na)
# else:
#     print("arr : ",arr,"안에는 찾고자 하는 숫자가 없습니다 : ",na)
# print('결과 : ',na in arr)
# in <- 멤버연산자
# A in B
# B 안에 A가 존재하면 True
#            존재하지 않으면 False
# A not in B
# B 안에 A가 존재하지 않으면 True
#            존재하면 False

# st = "Hello Python Fun"
# na = input("찾고자 하는 문자열 입력 : ")
# if na in st:
#     print("st : ",st,"찾는 문자열 : ",na,"존재 한다")
# else:
#     print("st 안에는 ",na,"존재 하지 않습니다")
#대,소문자 구분하기 / 띄워쓰기도 하나의 데이터값으로 인식

# old_id = input("저장할 ID 입력 : ")
# print("인증 프로그램 입니다")
# print("ID와 PW를 입력하세요")
# new_id = input("ID 입력 : ")
# if old_id == new_id :
#     print("인증 통과 했습니다")
# else:
#     print("인증 실패")

# num = int(input("수 입력 : "))
# if num % 3 == 0 | num % 2 == 0:
#     print("num은 3의 배수면서 짝수 입니다")
# else : 
#     print("다음-문장 실행")

# num = int(input("수 입력 : "))
# if num > 0:
#     if num % 2 == 0:
#         print("num은 양의 짝수 입니다")
#     else:
#         print("num은 양의 홀수 입니다")
# else:
#     print("num은 음수 입니다")
# print("다음문장 실행")

#중첩 if문 퀴즈
#네이버 방식(아이디,비밀번호 동시 입력)
#구글(아이디->비밀번호 순으로 입력)

# new_id = input("아이디 설정 : ")
# new_ps = input("비밀번호 설정 : ")
# old_id = input("아이디 : ")
# if new_id == old_id :
#     old_ps = input("비밀번호 : ")
#     if new_ps == old_ps :
#         print("인증 통과")
#     else :
#         print("비밀번호가 틀렸습니다.")
# else :
#     print("등록되지 않은 아이디 입니다.")
#==============================================
# #네이버 방식
# old_id=input("저장할 id 입력 : ")
# old_pw=input("저장할 pw 입력 : ")
# print("== 인증 프로그램 시작 ==")
# new_id=input("아이디 입력 : ")
# new_pw=input("패스워드 입력 : ")
# if old_id==new_id :
#     if old_pw == new_pw :
#         print("인증 통과")
#     else: 
#         print("비밀번호가 틀렸습니다")
# else :
#     print("등록되지 않은 아이디 입니다")
# #구글방식
# old_id=input("저장할 id 입력 : ")
# old_pw=input("저장할 pw 입력 : ")
# print("== 인증 프로그램 시작 ==")
# new_id=input("아이디 입력 : ")
# if old_id==new_id :
#     new_pw=input("패스워드 입력 : ")
#     if old_pw == new_pw :
#         print("인증 통과")
#     else: 
#         print("비밀번호가 틀렸습니다")
# else :
#     print("등록되지 않은 아이디 입니다")

# num = int(input("수 입력 : "))
# if num > 100:
#     print("100보다 큰 수 입력")
# elif num > 50:
#     print("50보다 큰 수 입력")
# elif num > 0:
#     print("0보다 큰 수 입력")
# else:
#     print("그 외의 값 입력")

# name = input("이름 : ")
# number = input("학번 : ")
# jum_1 = float(input("1과목 점수 입력 : "))
# jum_2 = float(input("2과목 점수 입력 : "))
# jum_3 = float(input("3과목 점수 입력 : "))
# avg = (jum_1+jum_2+jum_3)/3
# if avg >= 80 :
#     print("학점 : A")
# elif avg >= 70 :
#     print("학점 : B")
# elif avg >= 70 :
#     print("학점 : C")
# elif avg >= 60 :
#     print("학점 : D")
# else :
#     print("학점 : F")
# ##################################################
# cof = 2000
# cnt = int(input("커피의 갯수를 입력하세요 : "))
# if cnt > 10 :
#     cof = (cof*10)+(1500*(cnt-10))
#     print("커피 값은 %d원 입니다." %cof)
# else :
#     cof = cof*cnt
#     print("커피 값은 %d원 입니다." %cof)
# ###################################################
# su = int(input("정수를 입력하세요 : "))
# if su == 0 :
#     print("0은 3의 배수도 4의 배수도 아닙니다.")
# elif (su%3 == 0) & (su%4 == 0) :
#     print("3의 배수이면서, 4의 배수입니다. ")
# elif (su%3 == 0) & (su%4 != 0) :
#     print("3의 배수입니다.")
# elif (su%3 != 0) & (su%4 == 0) :
#     print("4의 배수입니다.")
# else : 
#     print("3의 배수도, 4의 배수도 아닙니다.")
# #####################################################
# time = int(input("비행기 탑승 시간을 분 단위로 입력해주세요 : "))
# pay_basic = 30000
# if time > 30 :
#     pay_all = pay_basic+((5000/10)*(time-30))
#     print("비행기 총 요금은 %d입니다. " %pay_all)
# else :
#     print("비행기 총 요금은 %d원 입니다. " %pay_basic)
# ######################################################
# 비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 10분 단위로 
# 추가요금 5000원씩 부가된다. 비행기 탈 시간을 입력하여 요금 계산기를 만드시오.

# money=30000
# time=int(input("비행기 탑승 시간 : "))
# time-=30
# if time > 0 :
#     money=money+(time-1)//10*5000+5000

#     # if time%10 == 0:
#     #     money=money+time//10*5000
#     # else :
#     #     money=money+time//10*5000+5000
# print("비행기 탑승 요금 :  %d원"%money)
# Keys() 키값만 추출해 리스트로 출력
# Values() 벨류값만 추출해 리스트로 출력
# Items() 키와 벨류 리스트 출력
# Clear() 내용을 전부 삭제
# Get() 키가 없으면 :None 키가 있으면 :value 출력
# Setdefault() key가 없으면 추가 설정 
# Update() 다른 딕셔너리의 내용을 추가 예) aaa.update(bbb) = aaa{aaa+bbb} (덮어쓰기)
# Pop() Key를 이용해서 해당하는 값을 지움 
# Fromkeys() (key,value)리스트나 튜플로 설정 

# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"}
# print(num.keys())
# print()
# print(num.values())

num = { 1:"일" , 2:'이' , 3:'삼',4:"사"}
print("num.keys() : ",num.keys())
print("list(num) : ",list(num))
print('list(num.keys()) : ' , list(num.keys()))
print()
print("num.values() : ",num.values())
print("list(num.values()) : ",list(num.values()))

# singer = {}
# singer['이름']=input("가수 이름 입력 : ")
# singer['구성원']=input("인원수 입력 : ")
# singer['대표곡']=input("대표곡 입력 : ")
# for i in singer.keys():
#     print('%s : %s' % (i,singer[i]))

# # 없는메뉴만 추가, 있는메뉴입니다. / 없는 메뉴 입력시 , 등록되지 않은 메뉴입니다.
# menu={}; bl = True; num = 0
# while bl:
#     print("1.메뉴 등록"); print("2.메뉴별 가격 보기"); print("3.가격 수정");print("4.종료")
#     num=int(input(">>> "))
#     if num == 1:
#         name = input("메뉴 입력 : ")
#         if menu.get(name) == None:
#             menu[name] = input("가격 입력 : ")
#         else : 
#             print("이미 등록된 메뉴입니다.")
#     elif num == 2:
#         for i in menu.keys():
#             print(i,":",menu[i])
#     elif num == 3:
#         name = input("수정할 목록 입력")
#         if menu.get(name) == None :
#             print("등록되지 않은 메뉴입니다.")
#         else :
#             menu[name] = input("수정가격 : ")
#     elif num ==4:
#         print("프로그램 종료 합니다")
#         bl = False

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}
# print(num)
# print("num.get(3) : ",num.get(3))
# print("num.get(9) : ",num.get(9))
# print("num.get(0) : ",num.get(0,'없음'))
# su = int(input("찾고자하는 키 입력 : "))
# if num.get(su) == None:
#     print("값이 없습니다")
# else:
#     print(num.get(su))

# student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'}
# print(student['학번'])
# print(student['이름'])
# print(student['학과'])
# print()
# print(student.items())
# print()
# print(student)

# name={ '이순신':"거북선",'세종대왕':'훈민정음','파이썬':'프로그래밍 언어'}
# for key,value in name.items():
#     print(key,":",value)
# print("삭제 : ",name.clear())
# print("삭제 후 값:",name)

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}
# print("변경전 값 : ",num)
# print()
# print("num.setdefault(9) : ",num.setdefault(9,"구~우"))
# print()
# print("변경전 후 : ",num)
# print()
# print("num.get(9)번째 value : ",num.setdefault(9,"구구구구구구"))

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}
# aaa={6:"육",7:"칠",8:"팔"}
# print("update 전 num : ",num)
# num.update(aaa)
# print("update 후 num : ",num)

# dic = {}
# ls = []
# ls.append(input("등록할 키값 입력 : "))
# ls.append(input("등록할 키값 입력 : "))
# ls.append(input("등록할 키값 입력 : "))
# dic = dic.fromkeys(ls)
# print("dic키 설정 : ",dic)
# dic=dic.fromkeys(ls,)
# print("dic 키&값 설정 : ",dic)

# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"}
# print("pop 전 num : ",num)
# print('\npop(3) 실행 : ' , num.pop(3))
# print("\npop 실행 후 num : ",num)

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}
# print("popitem() 전 num : %s\n" % num)
# print("popitem 실행 결과 => ",end=" ")
# print(num.popitem())
# print("popitem() 후 num : %s\n" % num)
# print("popitem 실행 결과 => ",end=" ")
# print(num.popitem())
# print("popitem() 후 num : %s" % num)
# # # popitem() = 딕셔너리의 맨 마지막값을 추출하기 위한 함수(값을 가지면 안됨)

# info={}; pe = []; bl = True; num = 0
# while bl:
#     print("1.인적사항 등록"); print("2.검색"); print("3.종료")
#     num=int(input(">>> "))
#     if num == 1:
#         pe.append(input("이름 입력 : ")); pe.append(input("점수 입력 : "))
#         info[pe[0]] = pe[1]
#     elif num == 2:
#         name = input("찾고자하는 학생 이름 입력 : ")
#         if info.get(name) == None: print("찾고자 하는 학생이 없습니다")
#         else: print(name,"님 점수 : ",info.get(name))
#     elif num ==3:
#         print("프로그램 종료 합니다")
#         bl = False
#     pe.clear() # <<<< 정답
# # 1. 인적사항 재등록이 불가능.(초기화가 안됨)

# names = {'허준','신사임담','권율','홍길동','허준'}
# print(type(names))
# print(len(names))
# print(names)

# s = {}
# print(type(s))
# print(set('programming'))
# print(set([12,15,17,11,15]))
# dic = {'a':1, 'b':2, 'c':3}
# print(set(dic))

# for x in {'가','나','다','라'}:
#     print(x)
# 4/10

# add() = append의 개념, 집합의 요소를 추가
# update() = 집합을 결합
# remove() = 집합의 요소를 삭제

# asia = {'korea','china','japan'}
# print(asia)
# asia.add('thailand')
# print(asia)
# asia.add('china')
# print(asia)
# asia.remove('japan')
# print(asia)

# asia = {'korea', 'china', 'japan'}
# print(asia)
# asia2 = {'iraq', 'singapore', 'korea'}
# asia.update(asia2)
# print(asia)
# print('-'*40)
# asia = {'korea', 'china', 'japan'}
# asia2 = {'iraq', 'singapore', 'korea'}
# asia3=asia+asia2
# print(asia3)

# 1] 합집합 (|) : 두 집합의 전체 요소들의 모음.union함수
# 2] 교집합 (&) : 두 집합의 공통 요소들의 모음.intersection함수
# 3] 차집합 (-) : 왼쪽 집합의 요소에서 오른쪽 집합의 요소를 제거.difference함수
# 4] 배타적 차집합(^) : 합집합 – 교집합. symmetric_difference함수
# 5] 부분집합( <= ) : 왼쪽 집합이 오른쪽 집합의 부분집합인지의 여부를 확인
# 6] 진성 부분집합( < ) : 부분집합이면서 추가로 요소가 더 존재하는지를 확인.

# two={2,4,6,8,10,12}
# three={3,6,9,12,15}
# print('교집합',two & three)
# print(two.intersection(three))
# print('합집합',two | three)
# print(two.union(three))
# print('차집합',two - three)
# print(two.difference(three))
# print('배타적 차집합',two ^ three)
# print(two.symmetric_difference(three))

#집합 확인
# animal = {'호랑이', '사자','강아지','치타','햄스터','고양이'}
# pet= {'강아지','고양이','햄스터'}
# print(pet <= animal)
# print(pet <= pet)
# print(pet < animal)
# print(pet < pet)
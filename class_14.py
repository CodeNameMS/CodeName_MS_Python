aa=[[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
# print('[0][0]',aa[0][0])
# print('[0][1]',aa[0][1])
# print('[0][2]',aa[0][2])
# print('[0][3]',aa[0][3])
# print('[1][0]',aa[1][0])
# print('[1][1]',aa[1][1])

# for i in range(3) :
#     for j in range(4) :
#         print("[%d][%d],%d"%(i,j,aa[i][j]))
# aa=[[1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]]

# for i in range (len(aa)) :
#     for j in range(len(aa[i])) :
#         print(aa[i][j],end="\t")
#     print()
# print()
# for i in aa:
#     for j in i:
#         print(j,end="\t")
#     print()
    
# aa=[
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12] 
# ]
# a = aa[0]
# a[1]=20000
# print('[0]',aa[0])
# print(a)
# print(aa)

# import copy
# aa=[
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12] 
# ]
# #a = aa[0][:]
# a = copy.deepcopy(aa[0])
# a[1]=200000000
# print('[0]',aa[0])
# print(a)
# print(aa)

# ls_1 =[]
# ls_2 =[]
# value =1
# for i in range(3):
#     for j in range(4):
#         ls_1.append(value)
#         value+=1
#     ls_2.append(ls_1)
#     ls_1=[]
# for i in range(3) :
#     print(ls_2)
# ============================
# ls_1=[];ls_2=[];value=1
# for i in range(3):
#     for j in range(4):
#         ls_1.append(value)
#         value+=1
#     ls_2.append(ls_1)
#     ls_1=[]
# print(ls_2)
# for i in ls_2:
#     for j in i:
#         print(j,end="\t")
#     print()

# be = ['2019','12','31']
# print(be)
# af=list(map(int,be)) #()
# print(af)

# tp = (10,20,30) #튜플 자료형에서 ()는 생략가능
# print("tp : ",tp)
# print("tp type : ",type(tp))
# print("tp len : ",len(tp))

# tp1 = 10,20,30
# print("tp1 : ",tp1)
# print("tp1 type : ",type(tp1))
# print("tp1[0] type : ",type(tp1[0]))
# tp1[0] = 100 #에러 발생

# tpInt = (10) #튜플 자료형으로 쓰려면 최소 1개의 값이 ,로 구분되어야 함
# print("tpInt : ",type(tpInt)); #<class ‘int’>
# tpT1 = (10,)
# print("tpT1 : ",type(tpT1)); #<class ‘tuple’>
# tpT2 = 10,
# print("tpT2 : ",type(tpT2)); #<class ‘tuple’>

# tt1 = ( 10 , 20 , 30 , 40 )
# tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3]
# print("튜플 합 : %d" % tt2)
# print("tt1[1:3] : " , tt1[1:3])
# print("tt1[1:] : " , tt1[1:])
# print("tt1[:3] : " , tt1[:3])

# a = 1,2,3
# b = 4,5,6
# c = a+b
# print("a : ",a)
# print("b : ",b)
# print("c : ",c)

# pack = 1,2,"패킹" # ★★★★매우 중요★★★★
# print("packing\npack : ",pack)
# a,b,c = pack
# print("unpacking\na:",a,"b:",b,"c:",c)

# tp = 100,200,"함수",100,'개수'
# print("tp안의 200의 위치 : " ,tp.index(200),"번째 인덱스")
# print("tp안의 100의 개수 : ",tp.count(100)," 개")

# ===== 튜플에서 사용되는 함수는 3개뿐임
# 1. len
# 2. index
# 3. count
# 4. 검사, 확인, 세어보기 정도만 가능

# tp = "회사정보","제품명","가격정보","출시일"
# ls = ["삼성전자","겔럭시","100원","미정"]
# i=0
# for i in range(len(ls)):
#     print("%5s\t"%tp[i],":",ls[i])
# for i in range(len(ls)):
#     print("{}\t:{:<5}".format(tp[i],ls[i]))
# for i in range(len(ls)):
#     print("{1}\t:{0:<5}".format(tp[i],ls[i]))
# for i in range(len(ls)):
#     print("{}\t:{:=^10}".format(tp[i],ls[i]))

# 튜플의 자료형을 바꾸려면
# 언패킹 -> 변환 -> 패킹 순으로 변환 가능

# student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'}
# print(student)
# mobile = {"품명":"겔럭시","가격":100,"크기":10}
# print(mobile)

# impo = {}
# impo['파이썬'] = 'www.python.org'
# impo['네이버']='www.naver.com'
# impo['구글']='www.google.com'
# print("파이썬 : ",impo['파이썬'])
# print("네이버 : ",impo['네이버'])
# print("구글 : ",impo['구글'])

# impo = {}
# name = input('키값 입력 : ')
# val = input('값 입력')
# impo[name] = val
# print(name,": ",impo[name])

# chmp = {}
# for i in range(5) :
#     name = input("이름 입력 : ")
#     skill = input("스킬 입력 : ")
#     chmp[name]=skill
# print(chmp)

# import collections
# #순서있는 사전
# overWatch = collections.OrderedDict()
# i=0; name=""; val = ""
# for i in range(5):
#     name = input("이름(key) 입력 : ")
#     val = input("값(value) 입력 : ")
#     overWatch[name]=val
# print(overWatch)
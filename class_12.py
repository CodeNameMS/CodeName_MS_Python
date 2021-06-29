# ls = [500 , 200 , 300 , 400]; Sum = 0
# print("ls : ",ls)
# print("ls[0] :", ls[0])
# print("ls[1] :", ls[-1])
# print("ls[2] :", ls[-2])
# print("ls[3] :", ls[-3])

# ls = [0 , 0 , 0 , 0]; Sum = 0
# ls[0]=int(input("첫번째 숫자 입력 : "))
# ls[1]=int(input("두번째 숫자 입력 : "))
# ls[2]=int(input("세번째 숫자 입력 : "))
# ls[3]=int(input("네번째 숫자 입력 : "))
# Sum = ls[0] + ls[1] + ls[2] + ls[3]
# print("ls[0] :", ls[0])
# print("ls[1] :", ls[1])
# print("ls[2] :", ls[2])
# print("ls[3] :", ls[3])
# print("리스트의 합 : %d" % Sum)

# ls = [0 , 0 , 0 , 0]; Sum = 0
# print("len(ls) : ",len(ls))  #len함수는 리스트 함수의 변수 갯수를 세는 함수
# for i in range(len(ls)):
#     ls[i]=int(input(str(i)+"째 숫자 입력 : "))
#     Sum += ls[i]
# for i in range(len(ls)):
#     print("ls[%d] :"% i,ls[i])
# print("리스트의 합 :", Sum)

# ls = [10 , 20 , 30 , 40]
# print("ls : ",ls)
# print("\nls[1:3] => ls[1] ~ [2] :",ls[1:3]) #시작값은 컴퓨터 / 끝값은 사람 기준
# print("ls[0:3] => ls[0] ~ [2] :",ls[0:3])
# print("ls[2:] => ls[2] ~ [끝까지] :",ls[2:])
# print("ls[:2] => ls[0] ~ [1] :",ls[:2])

# ls = [10 , 20 , 30 , 40]
# arr = ls
# print("ls : {} ls , id : {}".format(ls,id(ls)))
# print("arr : {} arr , id : {}".format(arr,id(arr)))

# ls = [10 , 20 , 30 , 40]
# arr = ls[:]
# arr[2]=20000
# print("ls : {} , ls id : {}".format(ls,id(ls)))
# print("arr : {} , arr id : {}".format(arr,id(arr)))

# import copy
# ls = [10 , 20 , 30 , 40]
# #arr = ls[:]
# arr = copy.deepcopy(ls)
# arr[2]='deepcopy'
# print("ls : {} , ls id : {}".format(ls,id(ls)))
# print("arr : {} , arr id : {}".format(arr,id(arr)))

# ls = [ 10 , 20 , 30 ]
# arr = [ 40 , 50 , 60 ]
# print("ls : " , ls)
# print("arr : " , arr)
# Str = [ls[0]+arr[0],ls[1]+arr[1],ls[2]+arr[2]]
# print("ls + arr => Str : ", Str)
# string = [ls[0]*3,ls[1]*3,ls[2]*3]
# print("ls * 3 => string : " , string)
# =========================================
# ls = [ 10 , 20 , 30 ]
# arr = [ 40 , 50 , 60 ]
# print("ls : " , ls)
# print("arr : " , arr)
# Str = [ls[0]+arr[0],ls[1]+arr[1],ls[2]+arr[2]]
# print("ls + arr => Str : ", Str)
# string = [ls[0]*3,ls[1]*3,ls[2]*3]
# print("ls * 3 => string : " , string)

# ls = [4,8,2,7,6]
# for i in range (len(ls)-1) :
#     for k in range (i+1,len(ls)) :
#         if ls[i] > ls[k] :
#             ls[i],ls[k] = ls[k],ls[i]
# print(ls)

# jumsu = [82,85,76,79,96]
# rank = [1,1,1,1,1]
# for i in range(len(jumsu)):
#     for j in range(len(jumsu)) :
#         if jumsu[i] < jumsu[j] :
#             rank[i]+=1
# for k in range(len(jumsu)) :
#         print("점수",jumsu[k],"은",rank[k],"등") 

# jumsu=[82,85,76,79,96]
# rank =[1,1,1,1,1]
# for i in range (len(jumsu)) :
#     for j in range(len(jumsu)) :
#         if jumsu[i] < jumsu[j] :
#             rank[i]+=1
# for k in range (len(jumsu)):
#     print("점수 : %d점 / %d 등"%(jumsu[k],rank[k]))


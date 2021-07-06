#append() : 제일 뒤 값에 추가 (무조건 맨 뒤)
#pop() : 제일 뒤 값을 빼고 빼낸 값을 리스트에서 삭제 (로또)
#sort() : 항목 정렬
#reverse() : 항목 순서를 역순으로 (역순 정렬은 sort 후 reverse)
#index() : 지정한 값을 찾아 그 위치를 반환
#insert() : 지정된 위치에 값 삽입(삽입한 위치부터 리스트의 인덱스가 뒤로 밀림)
#remove() : 리스트에서 지정한 값을 제거, 지정한 값이 여러 개일 경우 첫번째 값만 삭제(값을 삭제)
#extend() : 리스트 뒤에 리스트를 추가, 더하기(+)연산과 같음.
#count() : 리스트에서 찾을 값의 갯수를 셈(네이버 검색어순위 등)
#del() : 리스트에서 해당위치 항목을 삭제(중요하나 안하나 위치값으로 삭제)

# ls = [10,20,30]
# ls.append(1000)
# for i in range(len(ls)):
#     print("ls[{}] : {}".format(i,ls[i]))
# print("리스트의 총 개수 : ",len(ls))
# print("ls : ",ls)
# ls=[]
# print("ls초기화 후 : ",ls)

# ls = []
# for i in range(0 , 4) :
#     ls.append(0)
# Sum = 0
# for i in range(0 , len(ls)) :
#     ls[i] = int(input(str(i+1) + "번째 숫자 : "))
#     Sum += ls[i]
# for i in range(0 , len(ls)) :
#     print("입력 받은 값 ls[{}] : {}".format( i , ls[i] ))
# print("합 계 : %d " % Sum)

# num = int(input('몇개의 공간 만들겠습니까? :'))
# ls = []
# Sum = 0
# for i in range(num) :
#     ls.append(int(input(str(i+1) + "번째 숫자 : ")))
#     Sum += ls[i]
# for i in range(0 , len(ls)) :
#     print("입력 받은 값 ls[{}] : {}".format( i , ls[i] ))
# print("합 계 :", Sum)

# List = [ -20 , 30 ,10 ]
# print("현재 리스트 : " , List)
# List.append(40)
# print("append(40) 후 리스트 : " , List)
# print("pop() 으로 추출한 값 : " , List.pop())
# print("pop() 후 리스트 : " , List)
# List.sort()
# print("sort() 후 리스트 : " , List)
# List.reverse()
# print("reverse() 후 리스트 : " , List)
# del(List[2])
# print("del() 후 리스트 : " , List)

# List = [ 30 , 20 ,10 ]
# print("현재 리스트 : " , List)
# print(" 10 값의 위치 : " , List.index(10))
# List.insert(2,200)
# print("insert(2,200) 후 리스트 : " , List)
# List.remove(200)
# print("remove(200) 후 리스트 : " , List)
# List.extend( [ 555 , 666 , 555 ] )
# print("extend( [ 555 , 666 , 555 ] ) 후의 리스트 : " , List)
# print("555 값의 개수 : " , List.count(555))

ls = [10,5,20,7,9,31,12,11,19,32]
# #1
# ls_j =[]
# ls_h =[]
# ls_sum =[]
# for i in range(len(ls)) :
#     if i%2 == 0 :
#         ls_h.append(ls[i])
#     else :
#         ls_j.append(ls[i])
# for j in range(len(ls_j)) :
#     ls_sum.append(ls_j[j]-ls_h[j])
# print(ls_sum)
# #2
# ls = [10,5,20,7,9,31,12,11,19,32]
# jjak_sum=0
# hol_sum=0
# for i in range(len(ls)):
#     if i%2== 0:
#         jjak_sum+= ls[i]
#     else :
#         hol_sum+= ls[i]
# print(jjak_sum-hol_sum)

# #3-1
# ls = [10,5,20,7,9,31,12,11,19,32]
# temp_ls=ls[:]
# invertls=[]
# for i in range (len(ls)):
#     invertls.append(temp_ls.pop())
# print(invertls)
# #3-2
# invertls=[]
# temp = len(ls)-1
# for i in range (len(ls)) :
#     invertls.append(ls[temp])
#     temp-=1
# print(invertls)
# #3-3
# invertls=[]
# for i in range (1,len(ls)+1) :
#     invertls.append(ls[-i])
# print(invertls)

# #4
# ls = [10,5,20,7,9,31,12,11,19,32]
# sortls=ls[:]
# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if sortls[i] > sortls[j] :
#             sortls[i],sortls[j] = sortls[j],sortls[i]
# print(sortls)

# #5
# ls = [10,5,20,7,9,31,12,11,19,32]
# reversels=ls[:]
# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if reversels[i] < reversels[j] :
#             reversels[i],reversels[j] = reversels[j],reversels[i]
# print(reversels)

# aa=[[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]]
# print('[0][0]',aa[0][0])
# print('[0][1]',aa[0][1])
# print('[0][2]',aa[0][2])
# print('[0][3]',aa[0][3])
# print('[1][0]',aa[1][0])
# print('[1][1]',aa[1][1])
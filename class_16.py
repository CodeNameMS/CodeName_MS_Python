# Str = 'Have a nice day'

# for i in range (len(Str)):
#     print(Str[i],end="")
# print()
# for j in Str:
#     print(j,end="")
# print()

# st = 'Have a nice day Have a nice day Have a nice day'
# lo = 0 #최초 시작할 인덱스를 지정하기 위해 0으로 초기화
# ls=[]
# while True : #for문보다는 while문이 효율적
#     lo=st.find('a',lo) #찾은인덱스를 다시 인덱스 지정 변수에 저장
#     if lo != -1 :  #-1과 같지 않다는건 a의 값을 찾았다는뜻.               
#         ls.append(lo) #..그래서 인덱스를 list에추가
#         lo+=1 #다음 찾을 인덱스를 지정하기 위해 하나 증가시킨후 다시 찾음.
#     else :
#         break
# print("a 개수 : %d"%(st.count('a')))
# print(ls)

# st = """
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월14일
# """
# lo=0
# st = st.replace('-',':')
# while True :
#     lo=st.find(":",lo)
#     if lo != -1 :
#         st=st.replace(st[lo+1:lo+5],'1999')
#         lo+=1
#     else :
#         break
# print(st)

# # while True :
# #     lo=st.find("년",lo)
# #     if lo != -1 :
# #         st=st.replace(st[lo-4:lo],'1999')
# #         lo+=1
# #     else :
# #         break
# # print(st)
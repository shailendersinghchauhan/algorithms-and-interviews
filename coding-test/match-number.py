def solution(A,B):
   # code
   pass
   a = str(A)
   b = str(B)
   lengthA = len(a)
   for i in range(0, len(b) - lengthA +1, lengthA):
       #print("i=",i, "B[i]=",b[i])
       strB = b[i] + b[i+1]
       #print(strB)
       if( A == int(strB)):
           return i
  # print(a,b)
   return -1


print(solution(53 , 19536786))
print(solution(78 , 195378678))
print(solution(580 , 19530249580))
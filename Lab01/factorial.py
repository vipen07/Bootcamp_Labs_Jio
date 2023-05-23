import math
import sys
arg = sys.argv[1:]
n = arg[0]

if len(sys.argv)==1:
    exit()
else:
    class fact():
        def compute(m:int,self)->int:
            ans = 1
            print(m)
            i=1
            for i in range(1,int(m)+1):
                ans = ans*i
            
            return ans
        

    facto = fact()
    print(facto.compute(n))


#同花取到一把同花的概率
import numpy as np

import random
a=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]

k=0
for h in range(1,17):
    s=0
    for i in range(10000):
        b=random.sample(a,h)
        # print(b)
   
   
        for j in b:
            if b.count(j)==4:
                s=s+1
                #print("有同花")
                #print(s)
                break
    print(h,"张相同的扑克牌")        
    print(s/10000)
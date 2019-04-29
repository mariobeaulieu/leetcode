#!/usr/bin/env python
import sys

def intToRoman(num:int) -> str:
        S='IVXLCDM'
        r=''
        for i in range(0,7,2):
            v = num - int(num/10)*10
            print('v=%i'%v)
            if   v==1:r=S[i]+r
            elif v==2:r=S[i]+S[i]+r
            elif v==3:r=S[i]+S[i]+S[i]+r
            elif v==4:r=S[i]+S[i+1]+r
            elif v==5:r=S[i+1]+r
            elif v==6:r=S[i+1]+S[i]+r
            elif v==7:r=S[i+1]+S[i]+S[i]+r
            elif v==8:r=S[i+1]+S[i]+S[i]+S[i]+r
            elif v==9:r=S[i]+S[i+2]+r
            num = int(num/10)
        return r

print (intToRoman(int(sys.argv[1])))

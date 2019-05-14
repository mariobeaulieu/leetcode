#!/usr/bin/env python
import sys

class Solution:
    def divide(self, dividend:int, divisor:int) -> int:
        res_str=''
        if (dividend>0) ^ (divisor>0): res_str='-'
        dividend=abs(dividend)
        divisor =abs(divisor )
        divid_str=str(dividend)
        divis_str=str(divisor)
        l1=len(divid_str)
        l2=len(divis_str)
        if l1<l2: return 0
        calc_str=''
        for c in divid_str:
            calc_str+=c
            calc=int(calc_str)
            v=0
            while calc>=divisor:
                calc-=divisor
                v+=1
            calc_str=str(calc)
            res_str+=str(v)
        res=int(res_str)
        if res>2147483647 : res=2147483647
        if res<-2147483648: res=-2147483648
        return res
if __name__=='__main__':
    try:
        divid=int(sys.argv[1])
        divis=int(sys.argv[2])
    except:
        print('Program to perform integer division')
        print('Usage: %s <dividend> <divisor>'%sys.argv[0])
        print('       Will return the value of dividend/divisor')
        sys.exit(-1)
    s=Solution()
    print('%i/%i=%i'%(divid,divis,s.divide(divid,divis)))

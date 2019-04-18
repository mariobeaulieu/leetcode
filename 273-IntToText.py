#!/usr/bin/env python

import sys


def numberToWords(num: int) -> str:
        if num == 0:
           return 'Zero'
        U={1:'One ',2:'Two ', 3:'Three ',4:'Four ',5:'Five ',6:'Six ',7:'Seven ',8:'Eight ',9:'Nine ',
           10:'Ten ',11:'Eleven ',12:'Twelve ',13:'Thirteen ',14:'Fourteen ',15:'Fifteen ',16:'Sixteen ',
           17:'Seventeen ',18:'Eighteen ',19:'Nineteen ',
           20:'Twenty ',30:'Thirty ',40:'Fourty ',50:'Fifty ',60:'Sixty ',70:'Seventy ',80:'Eighty ',
           90:'Ninety ',100:'Hundred ',0:''}
        M={1:'',1000:'Thousand ',1000000:'Million ',1000000000:'Billion ',1000000000000:'Trillion '}
        multiplicator=1
        result = ''
        while num>0:
            v = num - int(num/1000)*1000
            if v>0:
               c = int(v/100)
               v = v - c*100
               #print ('c=%i,v=%i,multiplicator=%i'%(c,v,multiplicator))
               if c==0:
                   h=''
               else:
                   h=U[c]+U[100]
               if v<=20:
                   r = U[v]
               else:
                   d = int(v/10)*10
                   #print('d=%i,v=%i'%(d,v))
                   r = U[d]+U[v-d]
               result = h + r + M[multiplicator] + result
            num = int(num/1000)
            multiplicator *= 1000
        return result.strip()
print(numberToWords(int(sys.argv[1])))

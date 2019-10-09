# Bu dosyada matris oluşturup elemanlarına erişeceğiz.
import numpy as np

a = np.zeros([4,4],dtype='int8')    # 4 e 4'lük matrisi 0 ile doldur
print("a:\n",a)

b = np.ones([3,3,3],dtype='double')     # 3 , 3 , 3 'lük matrisi 1 ile doldur
print("b:\n",b)

c = np.full([2,2],10.8)            # 2 ye 2 'lik matrisi 10,8 ile doldur
print("c:\n",c)

d = np.random.randint(7,size=(4,4,4))
print("d:\n",d)

i = np.identity(3,dtype='int8')
print("i:\n",i)
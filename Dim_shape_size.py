# Bu dosyada listlerin boyutuna, şekline ve büyüklüğüne bakacağız
import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])
# kolayca başta ve sonda biriken parantez sayısı size boyutu verir

print("a.ndim=\n",a.ndim)
print("b.ndim=\n",b.ndim)
# görüntü işlemede çok kullanılmasa da hata ayıklamak için verilen datanın 2 boyutlu olup
# olmadığına bakabilirsiniz fakat zaten program büyük ihtimalle bunu sizin yerinize yapacaktır

print("a.shape:\n",a.shape)
print("b.shape:\n",b.shape)
# eğer kullandığınız fotoğraf ile aynı boyutta bir matris istiyorsanız bu fonksiyon işinize yarayabilir


print("b.size:\n",a.size)
print("b.size:\n",b.size)

# aldığınız görüntüdeki byte sayısını bulmak için kullanabilirsiniz
# Aşağıda verilen matrisi hazır matris oluşturma fonksiyonları ile en kısa yoldan oluşturmaya çalışın

import numpy as np

#       1 1 1 1 1
#       1 0 0 0 1
#       1 0 9 0 1
#       1 0 0 0 1
#       1 1 1 1 1

# Çözüm :

out = np.ones((5,5))
z = np.zeros((3,3))
out[1:4,1:4] = z    # ayrıca out[1:-1,1:-1] kullanarak sondan ilk elemanı yani baştan 4. elemanı alabilirsiniz
out[2,2] = 9

print(out)


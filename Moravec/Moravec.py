from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=np.array(Image.open('../test_image/test.jpg').convert('L'),'f')#'f'为float类型
rows,cols=img.shape[0:2]

plt.figure("原图")
plt.imshow(img,cmap='gray')
plt.axis('off')

m_hx=[[0 for i in range(cols)] for i in range(rows)]
bMatrix=[[0 for i in range(cols)] for i in range(rows)]
z=False
for i in range(5,rows-5,1):
    for j in range(5,cols-5,1):
        a=((img[i-2,j-2]-img[i-1,j-1])**2+(img[i,j]-img[i-1,j-1])**2+
        (img[i, j] - img[i + 1, j + 1]) ** 2 + (img[i + 2, j + 2] - img[i + 1, j + 1]) ** 2)
        b = (((img[i - 2, j]) - (img[i - 1, j])) ** 2 + ((img[i - 1, j]) - (img[i, j])) ** 2 +
             ((img[i, j]) - (img[i + 1, j])) ** 2 + ((img[i + 2, j]) - (img[i + 1, j])) ** 2)
        c = (((img[i - 2, j + 2]) - (img[i - 1, j + 1])) ** 2 + ((img[i, j]) - (img[i - 1, j + 1])) ** 2 +
             ((img[i, j]) - (img[i + 1, j - 1])) ** 2 + ((img[i + 2, j - 2]) - (img[i + 1, j - 1])) ** 2
             )
        d = (((img[i, j - 2]) - (img[i, j - 1])) ** 2 + ((img[i, j]) - (img[i, j - 1])) ** 2 +
             ((img[i, j]) - (img[i, j + 1])) ** 2 + ((img[i, j + 2]) - (img[i, j + 1])) ** 2
             )
        m_xq=min(a,b,c,d)

        if m_xq>2000:
            m_hx[i][j]=m_xq

#非极大值抑制
for i in range(5,rows-5,1):
    for j in range(5,cols-5,1):
        max=0
        for m in range(i-2,i+2,1):
            for n in range(j-2,j+2,1):
                if m_hx[m][n]>max:
                    max=m_hx[m][n]
                    m1=m
                    n1=n
                    z=True
        if z==True:
            bMatrix[m1][n1]=1

for i in range(rows-2):
    for j in range(cols-2):
        if bMatrix[i][j]==1:
            img[i+1][j]=255
            img[i][j]=255
            img[i-1][j]=255
            img[i][j+1]=255
            img[i][j-1]=255
            img[i][j+2]=255
            img[i][j-2]=255
            img[i+2][j]=255
            img[i-2][j]=255

plt.figure("特征")
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()
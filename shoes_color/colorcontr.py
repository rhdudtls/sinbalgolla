import cv2
import matplotlib.colors as cs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import re

#set path to image
imgpath = 'shoe.png'
#set number of cluster for kmeans
clusterno = 5

#read image
img = cv2.imread(imgpath)
#convert bgr to rgb
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#reshape img array
n_img = np.reshape(img,(img.shape[0]*img.shape[1],3))
cnt = 0
delcnt = 0
if n_img[0][0] == 0 and n_img[0][1] == 57 and n_img[0][2] == 15:
    for i in range(0,img.shape[0]*img.shape[1]):
        i = i - delcnt
        if n_img[i][0] == 0 and n_img[i][1] == 57 and n_img[i][2] == 15:
            n_img= np.delete(n_img,cnt,0)
            delcnt = delcnt + 1

        else:
            cnt = cnt + 1
elif n_img[0][0] == 245 and n_img[0][1] == 245 and n_img[0][2] == 245 :
    for i in range(0,img.shape[0]*img.shape[1]):
        i = i - delcnt
        if n_img[i][0] == 245 and n_img[i][1] == 245 and n_img[i][2] == 245:
            n_img= np.delete(n_img,cnt,0)
            delcnt = delcnt + 1

        else:
            cnt = cnt + 1
elif n_img[0][0] == 244 and n_img[0][1] == 244 and n_img[0][2] == 245 :
    for i in range(0,img.shape[0]*img.shape[1]):
        i = i - delcnt
        if n_img[i][0] == 244 and n_img[i][1] == 244 and n_img[i][2] == 245:
            n_img= np.delete(n_img,cnt,0)
            delcnt = delcnt + 1

        else:
            cnt = cnt + 1
#use kmeans to find cluster of color
clt = KMeans(n_clusters=clusterno)
clt.fit(n_img)

#get unique value of labels in kmeans
labels = np.unique(clt.labels_)

#find the pixel numbers of each color that is set by cluster number
hist,_ = np.histogram(clt.labels_,bins=np.arange(len(labels)+1))

#declare list to hold color to be used in chart
colors = []

#declare list to hold hex color code for labeling in chart
hexlabels = []

#get the main color
for i in range(clt.cluster_centers_.shape[0]):
  colors.append(tuple(clt.cluster_centers_[i]/255))
  hexlabels.append(cs.to_hex(tuple(clt.cluster_centers_[i]/255)))

#create pie chart for color
plt.pie(hist,labels=hexlabels,colors=colors,autopct='%1.1f%%')
plt.axis('equal')
plt.show()

pcent = []
for i in range (0,5):
  pcent.append((hist[i] / len(n_img)))
print(pcent)

colorrgb = []
for i in range (0,5):
    result = re.sub('#','',hexlabels[i])
    colorrgb.append(result)

def hex_to_rgb(hex):
  return list(int(hex[i:i+2], 16) for i in (0, 2, 4))
c= []
for i in range (0,5):
    c.append(hex_to_rgb(colorrgb[i]))

print(c)
#빨주노초파남보핑검흰베연하머스타드
rainbow = [[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[0,0,128],[95,0,255],[225,0,221],[0,0,0],[255,255,255],[245,245,220],[180,170,170],[160,186,210]]

def Euclidean_rgb(c1, c2) :
    rblist = []
    for j in range(0,5):
        for i in range(0, 13):

            def get_parm(p) :
                return [p[i][0], p[i][1], p[i][2]]
        
            def get_color(p):
                return [p[j][0], p[j][1], p[j][2]]
    
            def cal(p1, p2) :
                cal = np.square(p1-p2)
                return cal

            c1xyz = get_parm(c1)
    
            c2xyz = get_color(c2)
    
            def getSqrt(p1):
                sum = np.sqrt(p1)
                return sum

            d = cal(c1xyz[0], c2xyz[0]) + cal(c1xyz[1], c2xyz[1]) + cal(c1xyz[2], c2xyz[2])
            distance = getSqrt(d)
            rblist.append(distance)
    return rblist
    
lastrblist = Euclidean_rgb(rainbow, c)

new_b = np.reshape(lastrblist,(5,13))
disarr = []
for i in range(0,5):
    disarr.append(np.min(new_b[i]))


makecolor = []
for j in range(0,5):
    for i in range(0,13):
        if new_b[j][i] == disarr[j]:
            makecolor.append(i)

print(disarr, makecolor)

total = []
for i in range(0, 5):
  total.append(((pcent[i] * 0.5) + ((1 / disarr[0]) * 0.3)))
print(total)

choicecolor = np.zeros(11)

for i in range(0, 5):
  if makecolor[i] == 0: choicecolor[0] = choicecolor[0] + total[i]
  elif makecolor[i] == 1: choicecolor[1] = choicecolor[1] + total[i]
  elif makecolor[i] == 2: choicecolor[2] = choicecolor[2] + total[i]
  elif makecolor[i] == 3 or makecolor[i] == 11: choicecolor[3] = choicecolor[3] + total[i]
  elif makecolor[i] == 4 or makecolor[i] == 12: choicecolor[4] = choicecolor[4] + total[i]
  elif makecolor[i] == 5: choicecolor[5] = choicecolor[5] + total[i]
  elif makecolor[i] == 6: choicecolor[6] = choicecolor[6] + total[i]
  elif makecolor[i] == 7: choicecolor[7] = choicecolor[7] + total[i]
  elif makecolor[i] == 8: choicecolor[8] = choicecolor[8] + (total[i] * 0.9)
  elif makecolor[i] == 9: choicecolor[9] = choicecolor[9] + total[i]
  elif makecolor[i] == 10:  choicecolor[10] = choicecolor[10] + (total[i] * 0.8)

a = choicecolor.max()
if choicecolor[0] == a: print('Red')
elif choicecolor[1] == a: print('Orange')
elif choicecolor[2] == a: print('Yellow')
elif choicecolor[3] == a: print('green')
elif choicecolor[4] == a: print('Blue')
elif choicecolor[5] == a: print('Navy')
elif choicecolor[6] == a: print('Purple')
elif choicecolor[7] == a: print('Pink')
elif choicecolor[8] == a: print('Black')
elif choicecolor[9] == a: print('White')
elif choicecolor[10] == a: print('Beige')
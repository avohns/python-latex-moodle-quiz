import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import os
import io
from PIL import Image, ImageDraw, ImageFont

pointsX=[]
pointsY=[]

armX=[]
armY=[]
for r in range(0,8):
  armX.append([])
  armY.append([])
for r in range(1,6):
  armX[0].append(0)
  armY[0].append(r)
  armX[4].append(0)
  armY[4].append(-r)
  armX[6].append(r)
  armY[6].append(0)
  armX[2].append(-r)
  armY[2].append(0)
  armX[7].append(r*np.sqrt(2)/2)
  armY[7].append(r*np.sqrt(2)/2)
  armX[1].append(-r*np.sqrt(2)/2)
  armY[1].append(r*np.sqrt(2)/2)
  armX[5].append(r*np.sqrt(2)/2)
  armY[5].append(-r*np.sqrt(2)/2)
  armX[3].append(-r*np.sqrt(2)/2)
  armY[3].append(-r*np.sqrt(2)/2)

kolams=map(list, it.permutations([0,1,2,3,4]))

for kolam in kolams:
  plt.figure(figsize=[3.5,3.5])
  for i in range (0,41):
    plt.plot( [armX[i%8][kolam[i%5]],armX[(i+1)%8][kolam[(i+1)%5]]],[armY[i%8][kolam[i%5]],armY[(i+1)%8][kolam[(i+1)%5]]],)
  for x in range(0,8):
    plt.scatter(armX[x],armY[x],s=8)
  plt.axis('off')
  filename='kolam-'+''.join(map(str, kolam))+'.png'
  buf = io.BytesIO()
  plt.savefig(buf, format='png',dpi=150)
  buf.seek(0)
  image = Image.open(buf)
  image = image.convert("RGBA")
  datas = image.getdata()
  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 255 and item[2] == 255:
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  image.putdata(newData)
  image.save(filename, 'PNG', optimize=True, quality=95)
  plt.close()
  buf.close()
os.system('mogrify -crop 455x455+35+35  kolam-*.png')

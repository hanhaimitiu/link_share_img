from math import sqrt

from PIL import Image
import random
chrarray=[" ","!",'"',"#","$","%",
          "&","'","(",')','*'
          ,'+',',','-','.','/','0','1','2','3','4','5',
          '6','7','8','9',':',';',
          '<','=','>','?','@','A','B',
          'C','D','E','F','G','H','I',
          'J','K','L','M','N','O','P',
          'Q','R','S','T','U','V','W',
          'X','Y','Z','[','\\',']','^',
          '_',"`",'a','b','c','d','e',
          'f','g','h','i','j','k','l',
          'm','n','o','p','q','r','s',
          't','u','v','w','x','y','z','{','|',"}",'~']


def c_to_num(c_num):
	if c_num==0:
		return random.randint(0,51)

	elif c_num==1:
		return random.randint(52, 102)

	elif c_num==2:
		return random.randint(103, 153)

	elif c_num==3:
		return random.randint(154, 204)
	else:
		return random.randint(205, 255)

def read_string(s):
	print(len(s))
	s_lenthh=len(s)
	width=int(sqrt(len(s)))+1
	height=width+1
	print(width)
	print(height)
	temprgb=[]
	for i in s:
		temprgb.append(read_one_andpaint(i))
	newimg=Image.new('RGB',(width,height),0)

	for i in range(0,width):
		for j in range(0,height):
			temp=i*width+j
			if(temp<s_lenthh):

				newimg.putpixel((i,j),temprgb[temp])

			else:
				newimg.putpixel((i,j),(0,0,0))
	print(len(temprgb))
	newimg.save("1.png")


def read_one_andpaint(chr_img):
	numofchr = chrarray.index(chr_img)
	a = int(numofchr / 25)
	b = int((numofchr - a * 25) / 5)
	c = numofchr - a * 25 - b * 5

	newrgb = (c_to_num(a), c_to_num(b), c_to_num(c))
	return newrgb
sss='yi xiao da fang le jia ren men'
read_string(sss)
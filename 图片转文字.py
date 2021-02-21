from PIL import Image

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
	if 51>=c_num>=0:
		return 0
	elif 102>=c_num>51:
		return 1
	elif 153>=c_num>102:
		return 2
	elif 204>=c_num>153:
		return 3
	else:
		return 4

def rgbs_tostring(width,rgbs):
	stringsall=''
	temp=0
	for i in rgbs:
		if temp<width:
			a = c_to_num(i[0])
			b = c_to_num(i[1])
			c = c_to_num(i[2])
			realnum = 25 * a + 5 * b + c
			if realnum<=95:
				stringsall += str(chrarray[realnum])
			temp+=1
		else:
			temp = 0
	return stringsall

readimg=Image.open("1.png")
rgbsss=[]
print(readimg.width)
for i in range(0,readimg.width):
	for j in range(0,readimg.height):
		rgbsss.append(readimg.getpixel((i,j)))
print(len(rgbsss))


print(rgbs_tostring(readimg.width,rgbsss))



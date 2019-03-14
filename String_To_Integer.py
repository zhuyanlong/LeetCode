def myAtoi(str: str) -> int:
	str=str.lstrip()#delete leading space
	result=0
	sign=0
	if len(str)==0:
		return 0
	if (ord(str[0])>=ord('0') and ord(str[0])<=ord('9')) or str[0]=='-' or str[0]=='+':
		if str[0]=='-' or str[0]=='+':
			i=1
			if str[0]=='-':
				sign=1
		else:
			i=0
		for k in range(i,len(str)):
			if (ord(str[k])>=ord('0') and ord(str[k])<=ord('9')):
				tmp=ord(str[k])-ord('0')
				result=result*10+tmp
			else:
				break
		if sign==1:
			result=-result
		if result > int(pow(2,31)-1):
			return int(pow(2,31)-1)
		if result < -int(pow(2,31)):
			return -int(pow(2,31))
		return result
	else:
		return 0


def main():
	print(myAtoi("3.14159"))

main()

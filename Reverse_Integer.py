def reverse(x: int) -> int:
	flag=0
	result=0
	if x<0:
		flag=1
		x=-x
	while x:
		tmp=x%10
		x=int(x/10)
		result=result*10+tmp
	if flag==1:
		result=-result
	up=int(pow(2,31)-1)
	low=-int(pow(2,31))
	if result>up or result<low:
		result=0
	print(result)


def main():
	reverse(1534236469)

main()


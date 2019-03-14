def isPalindrome(x: int) -> bool:
		x=str(x)
		flag=0
		for i in range(int(len(x)/2)):
			if x[i]!=x[len(x)-i-1]:
				flag=1
				break
		if flag==1:
			return False
		else:
			return True

def main():
	print(isPalindrome(-101))

main()
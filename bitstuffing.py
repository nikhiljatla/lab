s=input("Enter The Message: ")
flag=input("Enter The Flag Character: ")
n=len(s)
s=list(s)
for i in range(0,n-len(flag)+1):
    fc=s[i:i+len(flag)]
    fc=''.join(fc)
    if(flag==fc):
        s.insert((i+len(flag)-2),0)
        print(s)
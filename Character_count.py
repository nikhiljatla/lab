def cs(msg,l):
    i=0
    while(i<=l):
        s=int(msg[i])
        for j in range(i+1,i+s):
            print(msg[j],end=" ")
        print()
        i=i+s
m=input("Enter The Encoded Message")
msg=list(m)
cs(msg, len(m))
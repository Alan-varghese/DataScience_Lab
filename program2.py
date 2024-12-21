l1=['Good','Nice','Happy','Positive']
l2=['Sad','Bad','Frustrated','Not','Negative']
str1=input("Enter your response")
flag=0
ncount=0
t=str1.split()
for i in range(len(t)):
    for j in range(len(l1)):
        if t[i]==l1[j]:
            flag=1
    for k in range(len(l2)):
        if t[i]==l2[k]:
            ncount=ncount+1
            flag=1
    if flag==0:
        print("You are in another mood")
    elif ncount%2==0:
        print("Positive")
    else:
        print("Negative")
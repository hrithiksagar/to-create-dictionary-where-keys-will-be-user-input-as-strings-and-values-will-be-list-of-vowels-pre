x=int(input("enter size: "))
d={}
for i in range(n):
    keys=input("enter keys:")
    values=[]
    for i in keys:
        if i in "aeiouAEIOU":        
            values.append(i)
    d.update({keys:values})
print(d)

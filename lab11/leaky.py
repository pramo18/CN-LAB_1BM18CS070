a=int(input("Enter Output Rate:"))
b=int(input("Bucket Size:"))

for i in range(5):
    s=int(input("Enter packet size:"))
    if(s<b):
        if(s<=a):
            print("Bucket output succesful")
            print("Last bytes sent: ",s)
        else:
            print("Bucket output successful")
            print("Bytes outputed:",a)
            sent=s-a
            print("Last bytes sent: ",sent)
            print(sent)
    else:
        print("Bucket is full")

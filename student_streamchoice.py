name=input("Enter your name: ")
print(f"{name}, enter your marks as stated below ")

P=int(input("Physics: "))
C=int(input("Chemistry: "))
B=int(input("Biology: "))
M=int(input("Mathematics: "))
CA=int(input("Computer Applications: "))
H=int(input("History: "))
G=int(input("Geography: "))
E=int(input("English: "))
S=int(input("Second_Language: "))
t=[P,C,B,M,CA,H,G,E,S]
t.sort()
print(t)
del t[0:4]
print(t)
s=sum(t)
per=(s*100)/500
print(per)

# SCIENCE
if(per<50):
    print(f"{name} you are not eligible for admission")
else:
    if(per>75):
        if(P>=75 and C>=75 and M>=75 and B>=75 and CA>=75):
            print(f"{name}, You can apply for Science Stream")
        if(P>=80 and C>=75 and M>=85 and CA>=90):
             print(f"{name} ,You can go for Engineering")
        if(P>=75 and C>=85 and M>=75 and B>=90):
            print(f"{name} ,You can go for Medical")

# HUMANITIES
    if(per>65):
        if(E>=85 and H>=75 and G>=70 and S>=75 and CA>=70):
            print(f"{name}, You can apply for Humanities Stream")

#COMMERCE
    if(per>50):
        if(E>=60 and M>=70 and CA>=60):
            print(f"{name}, You can apply for Commerce and Accountancy Stream")
            

    else:
        print(f"{name}, You can take any stream of your choice.")

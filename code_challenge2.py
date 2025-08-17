deposit = eval(input("Enter amount to deposit-->"))

a = deposit // 1000
deposit = deposit % 1000
 
b = deposit // 500
deposit = deposit % 500

c = deposit // 200
deposit = deposit % 200

d = deposit // 100
deposit = deposit % 100

e = deposit // 50
deposit = deposit % 50

f = deposit // 20
deposit = deposit % 20

g = deposit // 10
deposit = deposit % 10

h = deposit // 5
deposit = deposit % 5

i = deposit // 1
deposit = deposit % 1

print("\n\t\tYour current breakdown is:")
print("\t\t\t",a,"\t- \t1000")
print("\t\t\t",b,"\t- \t500")
print("\t\t\t",c,"\t- \t200")
print("\t\t\t",d,"\t- \t100")
print("\t\t\t",e,"\t- \t50")
print("\t\t\t",f,"\t- \t20")
print("\t\t\t",g,"\t- \t10")
print("\t\t\t",h,"\t- \t5")
print("\t\t\t",i,"\t- \t1")
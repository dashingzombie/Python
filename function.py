def computepay(h,r):
    if h>40 :
        pay=40*r
        h=h-40
        r=r*1.5
        pay=pay+h*r
        return pay
    else :
        pay=h*r

        return pay



hrs = input("Enter Hours:")
r=input("Enter Rate:")
hrs=float(hrs)
r=float(r)
p = computepay(hrs,r)
print(p)

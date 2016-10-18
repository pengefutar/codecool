# the 1st 30 numbers of the Fibonacci sequence

a = [0, 1]

print("\nFibonacci sequence:")

for i in range(2, 32):
     a.append(a[i-1] + a[i-2])
     print((i-2)+1, ". ", a[i-2], sep="")



# user imput about desired length

length = eval(input("\nHow long do you want the Fibonacci sequence to run? "))
b = [0, 1]

print("\nFibonacci sequence:")

for n in range(2, length+2):
    b.append(b[n-1] + b[n-2])
    print((n-2)+1, ". ", b[n-2], sep="")



# dynamic spaces
# I have no idea how to do this, I've been trying it for HOURS now ffs'

length = eval(input("\nHow long do you want the Fibonacci sequence to run? "))
c = [0, 1]

print("\nFibonacci sequence:")

for m in range(2, length+2):
    c.append(c[m-1] + c[m-2])
    print("{0}. {1}".format((m-2)+1, c[m-2]), sep="") 

   
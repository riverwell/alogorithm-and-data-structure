def euclid(m:int,n:int):
    while True:
        r:int = m%n
        if(r==0):
            return n 
        m=n;n=r

max_divide = euclid(1633,355)
print(max_divide)


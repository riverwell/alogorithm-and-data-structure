def binary_search(a:list,b:int)->bool:
    n:int = len(a)
    center:int =int(n/2)
    if(n==0):
        return False
    elif(a[center]==b):
        return True;
    elif(a[center]>b):
        return binary_search(a[:center],b)
    else:
        return binary_search(a[center+1:],b)

int_list = [13,16,23,45,54,58,76,92]
result = binary_search(int_list,73)
print(result)

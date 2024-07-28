def is_sorted(list):
    if sorted(list) == list:
        return True
    else:
        return False 
    
print(is_sorted([1,2,3,4,5]))
print(is_sorted([5,4,3,2,1]))
print(is_sorted([2,2,2,2]))
print(is_sorted([1]))
print(is_sorted([]))
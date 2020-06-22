def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

def is_between2(x, y, z):
    if x <= y <= z:
        return True
    return False

def is_between3(x, y, z):
    return x <= y <= z

print(is_between(1,2,3))
print(is_between(1,1,1))
print(is_between(1,1,0))
print(is_between2(1,2,3))
print(is_between2(1,1,1))
print(is_between2(1,1,0))
print(is_between3(1,2,3))
print(is_between3(1,1,1))
print(is_between3(1,1,0))
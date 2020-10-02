def is_between(x,y,z):
    if x <= y and y <= z:
        return True
    else:
        return False

def is_between2(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

def is_between3(x, y, z):
    return x <= y <= z


print(is_between(1, 2, 3))
print(is_between(2, 1, 3))
print(is_between(0, 0, 0))
print('----')
print(is_between2(1, 2, 3))
print(is_between2(2, 1, 3))
print(is_between2(0, 0, 0))
print('----')
print(is_between3(1, 2, 3))
print(is_between3(2, 1, 3))
print(is_between3(0, 0, 0))

# # 0x01 => 1 * 16^0
# flag1 = 0x01

# # 0x10 => 1 * 16^1
# flag2 = 0x10

# # bitwise comparison operator
# print(flag1 & flag2)
x = 5
y = 6
z = 7


def is_y_between_x_and_z(x, y, z):
    if x <= y and y <= z:
        print("True")
        return True
    else:
        print("False")
        return False


if is_y_between_x_and_z(x, y, z):
    print(f"{y} ist zwischen {x} und {z}")


if not is_y_between_x_and_z(3, 3, 2):
    print(f"3 ist nicht zwischen 3 und 2")

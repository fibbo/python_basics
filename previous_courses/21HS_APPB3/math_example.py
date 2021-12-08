import math


def calc_sine(angle):
    result = math.sin(angle)
    return result


log_res = math.log(17.0)

cos_res = math.cos(0)

sin_res = math.sin(90)  # does this return the correct result?

print(f"Cosine of 0: {cos_res}")

print(f"Sine of 90: {math.sin(math.radians(90))}")
print(f"Sine of pi/2: {math.sin(math.pi / 2)}")


print(f"Sine of pi/2: {calc_sine(90)}")

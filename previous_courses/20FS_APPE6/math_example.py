import math

"""
Important is also to never give your .py file the same name
as a python library has. If you name your file math.py and 
then proceed to use 'import math' inside that file, it will only
find your math.py and not the math library anymore.
"""

print(math.cos(90))
print(math.cos(math.radians(90)))

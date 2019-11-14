# Foundations of Programming with Python #

To download the solutions click the green button `Clone or download` where you have the option to either download a zip file with all the contents that you see here or you can also clone the repository.

This is the repository for the programming course offered by the ITC of the University of Zurich. The solutions to the exercises can be found inside the `solutions` folder. The presentation and the exercise itself can be found inside the `slides` folder.

For some of the exercises there are slight variations available:

#### Exercise 4 ####

Instead of working with 6 arguments per function we create a class called Point3D. This encapsulates the 3 invidivual coordinates of a point inside a single object which can be used in our code.

#### Excercise 9 ####

Similarly exercise 9 also makes use of a class. This time the class is called student.

To read more about classes click [here](https://docs.python.org/3/tutorial/classes.html)

### Custom Exercises ###

The folder custom exercises contains (yet) undocumented python code. If you are interested in plotting data check out `Simple_Plot.py`. In order to run this example you have to install `numpy` and `matplotlib`. For this open a terminal and type the following:

`python -m pip install numpy`
`python -m pip install matplotlib`

Afterwards you should be able to run this plotting example.

Another example worth looking at is the `TryExcept.py`. This shows you how to avoid complete crashes with the try-except (also known try-catch) mechanism. This allows us to write code which can recover from hard errors (like division by 0, or file not found errors)
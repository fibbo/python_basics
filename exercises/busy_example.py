def set_drawing(drawing):
    global is_drawing # without this line any change to is_drawing has no effect to the is_drawing outside the function
    is_drawing = drawing
    isBusy()

def set_saving(saving): 
    global is_saving # without this line any change to is_saving has no effect to the is_saving outside the function
    is_saving = saving
    isBusy()


def isBusy():
    if (is_saving or is_drawing):
        print("We are busy")
    else:
        print("Not busy")


is_drawing = False
is_saving = False


set_saving(True)

set_drawing(True)

set_saving(False)

set_drawing(False)


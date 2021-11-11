from tkinter import *
import random
from PIL import Image, ImageTk


# main window creation

window = Tk()
window.title('Minesweeper')
window.configure(borderwidth=5)
window.configure(bg='gainsboro')

# create frame for buttons

button_frame = Frame(window, borderwidth=4, relief='sunken')
button_frame.grid(row=1, column=0, pady=4)

# lists for values and button positions

button_value = []
buttons = []
bomb_places = []
final_values = []

# list value setting functions

for x in range(0, 100):
    button_value.append(0)
    final_values.append(0)


def reset_values():
    for _ in range(0, len(bomb_places)):
        del(bomb_places[0])

    for _ in range(0, len(button_value)):
        del(button_value[0])

    for _ in range(0, len(final_values)):
        del(final_values[0])


def set_bombs():
    global button_value, bomb_places

    used_spaces = []
    for k in range(0, 20):
        rand = random.randint(0, 99)

        while rand in used_spaces:
            rand = random.randint(0, 99)

        bomb_places.append(rand)
        button_value[rand] = 1

    for _ in range(0, len(used_spaces)):
        del(used_spaces[0])


def set_values():
    global button_value, bomb_places

    # top left
    if button_value[0] == 1:
        pass
    else:
        final_values[0] = button_value[1] + button_value[10] + button_value[11]
    # top right
    if button_value[9] == 1:
        pass
    else:
        final_values[9] = button_value[8] + button_value[18] + button_value[19]
    # bot left
    if button_value[90] == 1:
        pass
    else:
        final_values[90] = button_value[91] + button_value[81] + button_value[80]
    # bot right
    if button_value[99] == 1:
        pass
    else:
        final_values[99] = button_value[98] + button_value[89] + button_value[88]

    # top row
    for x in range(1, 9):
        if button_value[x] == 1:
            pass
        else:
            final_values[x] = button_value[x-1] + button_value[x+1] + \
                          button_value[x+9] + button_value[x+10] + button_value[x+11]

    # bottom row
    for x in range(91, 99):
        if button_value[x] == 1:
            pass
        else:
            final_values[x] = button_value[x-1] + button_value[x+1] + button_value[x-9] + \
                          button_value[x-10] + button_value[x-11]

    # left side
    counter = 10
    for _ in range(0, 8):
        if button_value[counter] == 1:
            pass
        else:
            final_values[counter] = button_value[counter+1] + button_value[counter-9] + button_value[counter-10] + \
                                button_value[counter+10] + button_value[counter+11]
        counter += 10


    # right side
    counter = 19
    for _ in range(0, 8):
        if button_value == 1:
            pass
        else:
            final_values[counter] = button_value[counter - 1] + button_value[counter + 9] + button_value[counter + 10] + \
                                button_value[counter - 10] + button_value[counter - 11]
        counter += 10


    # center
    counter = 11
    counter_two = 0
    for _ in range(0,81):

        if counter > 90:
            break

        if button_value[counter] == 1:
            pass
        else:
            final_values[counter] = button_value[counter-1] + button_value[counter+1] + \
                                button_value[counter-9] + button_value[counter-10] + button_value[counter-11] + \
                                button_value[counter+9] + button_value[counter+10] + button_value[counter+11]
        counter_two += 1

        if counter_two == 8:
            counter += 3
            counter_two = 0
        else:
            counter += 1

    for numbers in bomb_places:
        final_values[numbers] = -1


set_bombs()
set_values()

# button press function


def button_press(but_num, pressed_button):
    global final_values

    if final_values[but_num] == -1:
        face.configure(image=o_face)

        for count, button in enumerate(buttons):
            if final_values[count] == 0:
                button.configure(relief='groove', bg='gray89')
            elif final_values[count] == 1:
                button.configure(text='1', relief='groove', bg='gray89', fg='blue')
            elif final_values[count] == 2:
                button.configure(text='2', relief='groove', bg='gray89', fg='green')
            elif final_values[count] == 3:
                button.configure(text='3', relief='groove', bg='gray89', fg='red')
            elif final_values[count] == 4:
                button.configure(text='4', relief='groove', bg='gray89', fg='purple4')
            elif final_values[count] == 5:
                button.configure(text='5', relief='groove', bg='gray89', fg='tomato4')
            elif final_values[count] == 6:
                button.configure(text='6', relief='groove', bg='gray89', fg='light sea green')
            elif final_values[count] == 7:
                button.configure(text='7', relief='groove', bg='gray89')
            elif final_values[count] == 8:
                button.configure(text='8', relief='groove', bg='gray89', fg='gray89')
            elif final_values[count] == -1:
                button.configure(image=bomb, width=0, height=0, relief='groove', bg='gray89')

        pressed_button.configure(image=bomb, height=0, width=0, bg='red', relief='groove')

    elif final_values[but_num] == 0:
        pressed_button.configure(relief='groove', bg='gray89')
    else:
        pressed_button.configure(relief='groove', bg='gray89', text=final_values[but_num])
        if final_values[but_num] == 1:
            pressed_button.configure(fg='blue')
        elif final_values[but_num] == 2:
            pressed_button.configure(fg='green')
        elif final_values[but_num] == 3:
            pressed_button.configure(fg='red')
        elif final_values[but_num] == 4:
            pressed_button.configure(fg='purple')

# reset press function


def reset_clicked():

    face.configure(image=smiley)

    for _ in range(0, len(buttons)):
        buttons[0].destroy()
        del(buttons[0])

    count = 0
    for i in range(1, 11):
        for j in range(0, 10):
            buttons.append(Button(button_frame, width=3, height=1, relief='raised', font='bold', borderwidth=3,
                                  command=lambda count=count: button_press(count, buttons[count])))
            buttons[count].grid(row=i, column=j)
            count += 1

    reset_values()

    for x in range(0, 100):
        button_value.append(0)
        final_values.append(0)

    set_bombs()
    set_values()

# top section creation and image creation


image_bomb = Image.open('bomb.png')
image_bomb = image_bomb.resize((31, 26))
bomb = ImageTk.PhotoImage(image_bomb)

image = Image.open('smileyiphone.jpg')
image = image.resize((40, 40))
smiley = ImageTk.PhotoImage(image)

image_o = Image.open('ofaceimage.png')
image_o = image_o.resize((40, 40))
o_face = ImageTk.PhotoImage(image_o)

top_bar = Frame(window, height=50, relief='sunken', borderwidth=4)
top_bar.grid(row=0, column=0, columnspan=10, sticky=W)

bomb_entry = Entry(top_bar, width=4, bg='black', font=('bold', 18), fg='green4')
bomb_entry.grid(row=0, column=0, padx=10, ipady=5)

bomb_entry.insert(0, ' 020')

face = Button(top_bar, image=smiley, command=lambda: reset_clicked())
face.grid(row=0, column=1, padx=96, pady=3)

time_entry = Entry(top_bar, width=4, bg='black', font=('bold', 18), fg='green4')
time_entry.grid(row=0, column=2, padx=10, ipady=5)

time_entry.insert(0, ' 000')


def find_open_space():
    pass

# initial button creation
counter = 0
for i in range(1, 11):
    for j in range(0, 10):
        buttons.append(Button(button_frame, width=3, height=1, relief='raised', font='bold', borderwidth=3, command=lambda counter=counter: button_press(counter, buttons[counter])))
        buttons[counter].grid(row=i, column=j)
        counter += 1

window.mainloop()

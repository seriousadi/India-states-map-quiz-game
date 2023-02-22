import tkinter.messagebox
from tkinter import *
import gamelogic

gamebrain = gamelogic.gameLogic()
color = 'white'
window = Tk()
window.title("Find It")
window.minsize(width=530, height=620)
window.maxsize(width=530, height=620)
highlited = r"D:\programming channels work\python file\resources\Images\India's map\India's states highlited"

correctly_answered = []


def wrong():
    canvas.config(background="white")


def image_maker(value):
    global the_image
    the_image = PhotoImage(file=value)
    newPhoto_label = tkinter.Label(image=the_image)
    newPhoto_label.place(x=0, y=0)

    #canvas.create_image(260, 305, image=the_image)
#def displayImg(img):
#    image = Image.open(img)
#    photo = PhotoImage(image)
#    photos.append(photo)#keep references!
#    newPhoto_label = Label(image=photo)
#    newPhoto_label.pack()

def entry_taker():
    global the_image, correctly_answered
    entered_state = gamebrain.name_equalizer(entry.get())

    if gamebrain.checker(entry.get()):
        # image_maker(entered_state)
        the_image = PhotoImage(file=f"{highlited}\{entered_state}.png")
        correctly_answered.append(f"{highlited}\{entered_state}.png")
        canvas.create_image(260, 305, image=the_image)
    else:
        print("you were wrong")
        canvas.config(background="red")
        window.after(500, wrong)
    entry.delete(0, END)
for n in correctly_answered:
    image_maker(n)

# start button functionality
def start():
    global entry, button
    quit_btn.place(x=600, y=600)
    start_btn.place(x=600, y=600)
    score_btn.place(x=600, y=600)
    canvas.itemconfig(initial_image, image=india_map)
    window.bind("<Escape>", lambda e: esc_keypress(e))
    entry = Entry(window, width=35)
    entry.place(x=250, y=50)
    button = Button(text="Click me", command=entry_taker)
    button.place(x=250, y=25)
    window.bind("<Return>", lambda e: esc_keypress(e))


# esc key press
def esc_keypress(e):
    if e.keysym == "Escape":
        try:
            button.destroy()
            entry.destroy()
        except:
            Label.place(x=900, y=900, width=500)

        quit_btn.place(x=278, y=300)
        start_btn.place(x=278, y=200)
        score_btn.place(x=278, y=250)
        canvas.itemconfig(initial_image, image=game_starting_pic)
    elif e.keysym == "Return":
        entry_taker()


# quiting the game
def quit():
    # Label(text="Do you really want to quit the game")
    if tkinter.messagebox.askokcancel(message="Do you really want to quit game?"):
        window.destroy()


# options
def options():
    global Label
    quit_btn.place(x=600, y=600)
    start_btn.place(x=600, y=600)
    score_btn.place(x=600, y=600)

    window.bind("<Escape>", lambda e: esc_keypress(e))
    Label = tkinter.Label(
        text="I am too lazy to make it just open \n a timer  on a clock app or \n something and record it   ",
        font=("Arial", 25))
    Label.place(x=10, y=40, width=500)


# Canvas
canvas = Canvas(width=520, height=610, background="white")
canvas.place(x=0, y=0)

# Images and thing
game_starting_file = "../resources/Images/gamestartingfile/"
india_map_file = "../resources/Images/India's map/"
game_starting_pic = PhotoImage(file=game_starting_file + "gamestartingfile.png")
quit_button_pic = PhotoImage(file=game_starting_file + "quit.png")
start_button_pic = PhotoImage(file=game_starting_file + "start.png")
score_button_pic = PhotoImage(file=game_starting_file + "score.png")
india_map = PhotoImage(file=india_map_file + "India's map.png")
# Creating starting Window
initial_image = canvas.create_image(260, 305, image=game_starting_pic)

quit_btn = Button(window, image=quit_button_pic, borderwidth=0, background='white', command=quit)
quit_btn.place(x=278, y=300)

start_btn = Button(window, image=start_button_pic, borderwidth=0, background='white', command=start)
start_btn.place(x=278, y=200)

score_btn = Button(window, image=score_button_pic, borderwidth=0, background='white', command=options)
score_btn.place(x=278, y=250)

window.mainloop()

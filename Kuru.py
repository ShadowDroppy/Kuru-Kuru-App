from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
import threading
from tkinter import messagebox
import random

root = Tk()  # widget that functions as the window. Kinda cool I guess

root.title('Herta Kuru!')  # title of application
root.iconbitmap('resources/hertaiCO.ico')  # icon of app
root.geometry("800x800")  # dimension tweak of the app window!

# background image
c=Canvas(root, bg='#F9F3F7',height=1, width=1)
chibi = Image.open("resources/herta chibi.png")
chibi = ImageTk.PhotoImage(file= "resources/herta chibi.png")
background_label = Label(root, image=chibi)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

root.config(background='#765873')

welcome_message = Label(root, text = "Welcome to Kuru Kuru!", bg='#F9F3F7', fg='black', font="Verdana 32 bold italic").place(x=90, y=0)
flavor_text = Label(root, text= "Application for all of your Kuru Kuru needs! *genius noises intensifies*", bg='#F9F3F7', fg='black', font= "Comic 14 bold italic").place(x=60, y=63)

x_pos = 0
y_pos = 0

# leave global label out so it doesn't recuriveness what-evamabob for every frame. yuck...
gif_labels = [] # Store GIF labels

lbl = Label(root, bg='#F9F3F7')
lbl.place(x=0, y=0)


# preload Gif frames

gif_frames = []

def preload_gif_frames():
    img = Image.open("resources/kurukuru-kururing.gif")
    for frame in ImageSequence.Iterator(img):
        tk_image = ImageTk.PhotoImage(frame.convert("RGBA"))
        gif_frames.append(tk_image)

# play gif function

def play_gif(lbl):
    x_pos = 800
    for _ in range(200): #responsible for number of iterations
        for frame in gif_frames:
            lbl.config(image=frame)
            lbl.image = frame

            lbl.place(x=x_pos, y = 88)

            x_pos -= 100

            root.update()
            time.sleep(0.05)


# play Kuru Kuru

def play_sound():
    pygame.mixer.init()

    #List of Sounds

    sound_list =["resources/Kuru kuru~ sound.mp3", "resources/Herta's Kururin (Sound Effect).mp3", "resources/Herta Kururin voice line _ Honkai Star Rail.mp3"]

    #Choose a sound randomly

    random_sound = random.choice(sound_list)
    pygame.mixer.music.load(random_sound)
    pygame.mixer.music.play(loops=0)

def add_gif():
    lbl = Label(root, bg='#F9F3F7')
    lbl.place(x=0,y=0)
    gif_labels.append(lbl)
    thread = threading.Thread(target=play_gif, args=(lbl,))
    thread.start()

counter = 0

def counter_label():
   global counter

    # Milestone checks 
   if counter > 0:
       Milestone_Comments()

   counter += 1
   counter_text.set("You Kuru'd {} times!".format(counter))


#helper function
def helper_function():
    t1 = threading.Thread(target=play_sound)
    t2 = threading.Thread(target=add_gif)
    t1.start()
    t2.start()
    counter_label()
    
def exit():
    root.destroy()

# text for counter 
counter_text = StringVar()
counter_text.set("Times Kuru'd: {}".format(counter))
counter_entry = Entry(root, textvariable=counter_text, state='readonly', bg='#765873').place(x=325, y=600)

#button functionality
click_button1 = Button(root, text="CLICK HERE!", command=helper_function,fg='white', bg='#AB85A7').place(
    x=325, y=700)  # executes the click function
click_button2 = Button(root, text="EXIT!", command=exit).place(x=410, y=700)


# Click Milestone comments! -----------------------------------------------------------------------------------------------------------------------------------------------------
milestone_text= None

def Milestone_Comments():
    global milestone_text
    if counter == 10 and milestone_text is None:
        milestone_text = Label(root, text="10 Kurus! The spinning has only just begun!", fg='black', bg='#F9F3F7', font="Comic 12 bold italic")
        milestone_text.place(x=255, y= 645)
       
    if counter == 50 and milestone_text is not None:
        if milestone_text:
            milestone_text.config(text="50 kuru's is nothing for true bonafide geniuses!")

    if counter == 100 and milestone_text is not None:
        if milestone_text:
            milestone_text.config(text="100 Kuru's! Keep on spinning baby!")
            

preload_gif_frames()

root.mainloop()

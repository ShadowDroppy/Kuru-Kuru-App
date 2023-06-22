from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
import threading
from tkinter import messagebox
import random
import webbrowser

root = Tk()  # widget that functions as the window. Kinda cool I guess

root.title('pics/Herta Kuru!')  # title of application
root.iconbitmap('pics/hertaiCO.ico')  # icon of app
root.geometry("800x800")  # dimension tweak of the app window!

# background image
c=Canvas(root, bg='#F9F3F7',height=1, width=1)
chibi = Image.open("pics/herta chibi.png")
chibi = ImageTk.PhotoImage(file= "pics/herta chibi.png")
background_label = Label(root, image=chibi)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

root.config(background='#765873')

welcome_message = Label(root, text = "Welcome to Kuru Kuru!", bg='SystemButtonFace', fg='black', font="Verdana 32 bold italic").place(x=90, y=0)
flavor_text = Label(root, text= "Application for all of your Kuru Kuru needs! *genius noises intensifies*", bg='SystemButtonFace', fg='black', font= "Comic 14 bold italic").place(x=60, y=63)

x_pos = 0
y_pos = 0

# leave global label out so it doesn't recuriveness what-evamabob for every frame. yuck...
gif_labels = [] # Store GIF labels

lbl = Label(root, bg='#F9F3F7')
lbl.place(x=0, y=0)


# preload Gif frames

gif_frames = []

def preload_gif_frames():
    img = Image.open("pics/kurukuru-kururing.gif")
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

    sound_list =["audio/Kuru kuru~ sound.mp3", "audio/Herta's Kururin (Sound Effect).mp3", "audio/Herta Kururin voice line _ Honkai Star Rail.mp3"]

    #Choose a sound randomly

    random_sound = random.choice(sound_list)
    pygame.mixer.music.load(random_sound)
    pygame.mixer.music.play(loops=0)

def set_vol(val):
    global volume
    volume=int(val)/100
    pygame.mixer.music.set_volume(volume)

def volume_control():
    pygame.mixer.init()
    w3 = Toplevel()
    w3.title("Options")
    w3.geometry("500x500")
    w3.configure(bg="SystemButtonFace")

    #volume control
    vol_lbl = Label(w3, text="Volume", font="Verdana 10 bold italic")
    vol_lbl.place(x=0,y=0)

    global scale 
    scale=Scale(w3, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
    scale.set(70)
    pygame.mixer.music.set_volume(0.7)
    scale.place(x=0,y=20)

    root.lift()

def add_gif():
    lbl = Label(root, bg='SystemButtonFace')
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
click_button1 = Button(root, text="CLICK HERE!", command=helper_function,fg='white', bg='#AB85A7')
click_button1.place(x=325, y=700)

click_button2 = Button(root, text="EXIT!", command=exit)
click_button2.place(x=410, y=700)

#Credits window functionality --------------------------------------------------------------------------------------------------------------------------------------------------
#2nd Window (Credits)
def credits():
    global shadowdrop_img, seseren_kr_img
    w2 = Toplevel()
    w2.title("Credits")
    w2.geometry("500x500")
    w2.configure(bg="white")

    #credits label
    global cred_lbl, cred_lbl2
    cred_lbl = Label(w2, text="Credits",font="Verdana 24 bold italic", bg="white")
    cred_lbl.place(x=0,y=0)

    cred_lbl2 = Label(w2,text="In no specific order", font="Verdana 8", fg="grey", bg="white")
    cred_lbl2.place(x=0, y=50)

    #ShadowDrop Credits
    shadowdrop_img = Image.open('pics/deoxsus.png')
    shadowdrop_img = ImageTk.PhotoImage(file= "pics/deoxsus.png")

    shadowdrop_btn = Button(w2, text="ShadowDroppy\n\nMain Developer", image=shadowdrop_img, compound=LEFT, command=shadowdrop_link, bg="white", borderwidth=0)
    shadowdrop_btn.place(x=0, y=80)

    shadowdrop_btn.bind("<Enter>", on_enter)
    shadowdrop_btn.bind("<Leave>", on_leave)

    #Seseren_kr credits
    seseren_kr_img = Image.open('pics/seseren_kr.jpg')

    desired_width = 128
    desired_height = 128

    resized_seseren = seseren_kr_img.resize((desired_width, desired_height), Image.ANTIALIAS)

    seseren_photo = ImageTk.PhotoImage(resized_seseren)

    seseren_kr_btn = Button(w2, text="Seseren_kr\n\nArtist", image=seseren_photo, compound=LEFT, command=seseren_kr_link, bg="white", borderwidth=0)
    seseren_kr_btn.image = seseren_photo  # Keep a reference to the PhotoImage
    seseren_kr_btn.config(image=seseren_photo)
    seseren_kr_btn.place(x=250, y=80)

    #duiqt credits
    duiqt_img = Image.open('pics/duiqt.png')

    desired_width = 128
    desired_height = 128

    resized_duiqt = duiqt_img.resize((desired_width, desired_height), Image.ANTIALIAS)

    duiqt_photo = ImageTk.PhotoImage(resized_duiqt)

    duiqt_btn = Button(w2, text="duiqt (Phuc Duy)\n\nInspiration", image=duiqt_photo, compound=LEFT, command=duiqt_link, bg="white", borderwidth=0)
    duiqt_btn.image = duiqt_photo  # Keep a reference to the PhotoImage
    duiqt_btn.config(image=duiqt_photo)
    duiqt_btn.place(x=0, y=220)


    # Highlight colorbind functions
    shadowdrop_btn.bind("<Enter>", on_enter)
    shadowdrop_btn.bind("<Leave>", on_leave3)

    seseren_kr_btn.bind("<Enter>", on_enter)
    seseren_kr_btn.bind("<Leave>", on_leave3)

    duiqt_btn.bind("<Enter>", on_enter)
    duiqt_btn.bind("<Leave>", on_leave3)

    root.lift()


def shadowdrop_link():
    webbrowser.open("https://github.com/ShadowDroppy")

def seseren_kr_link():
    webbrowser.open("https://twitter.com/Seseren_kr")

def duiqt_link():
    webbrowser.open("https://github.com/duiqt")

def github_link():
    webbrowser.open("https://github.com/ShadowDroppy/Kuru-Kuru-App")

# Hightlight buttons functions -------------------------------------------------------------------------------------------------------------------------------------------------
# Highlight colorbind functions to reference to ANY BUTTON
def on_enter(e):
    e.widget['background'] = 'darkgrey'

def on_enter2(f):
    f.widget['background'] = "#4F335E"

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

def on_leave2(f):
    f.widget['background']= '#AB85A7'

def on_leave3(g):
    g.widget['background'] = 'white'

click_button1.bind("<Enter>", on_enter2)
click_button1.bind("<Leave>", on_leave2)

click_button2.bind("<Enter>", on_enter)
click_button2.bind("<Leave>", on_leave)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Quality of Life buttons
credits_button = Button(root, text="Credits",command=credits)
credits_button.place(x=650, y=625)

credits_button.bind("<Enter>", on_enter)
credits_button.bind("<Leave>", on_leave)

options_button = Button(root, text="Options", command=volume_control)
options_button.place(x=650, y=665)

options_button.bind("<Enter>", on_enter)
options_button.bind("<Leave>", on_leave)

github_button = Button(root, text="GitHub Respository\n-Kuru-Kuru-App", command=github_link)
github_button.place(x=650, y=700)

github_button.bind("<Enter>", on_enter)
github_button.bind("<Leave>", on_leave)

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
            
#version no. update ------------------------------------------------------------------------------------------------------------------------------------------------------------
version_lbl = Label(root, text="1.2.0", font= "Comic 10 bold italic", fg="black")
version_lbl.place(x=750, y=770)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

preload_gif_frames()

root.mainloop()

from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
import threading
from tkinter import messagebox
import random
import webbrowser
try:                                                  # For preventing crashes on MAC OS
    from ctypes import windll, byref, sizeof, c_int   # Will try to run this on Windows. If not windows then...
except:                                               # it will effectively ignore the stuff before to work on MAC OS
    pass

root = Tk()  # widget that functions as the window. Kinda cool I guess

root.title('Herta Kuru-Kuru!')  # title of application
root.iconbitmap('pics/hertaiCO.ico')  # icon of app
root.geometry("800x800")  # dimension tweak of the app window!

# change color of title bar
try:
    HWND = windll.user32.GetParent(root.winfo_id())
    title_bar_color = 0x644575  #This ends up being an int variable!
    title_text_color = 0xF7F3F9 #Same here!
    windll.dwmapi.DwmSetWindowAttribute(HWND,35,                        #attribute no.35 is targeting the title bar background color
                                        byref(c_int(title_bar_color)),
                                        sizeof(c_int)) 

    windll.dwmapi.DwmSetWindowAttribute(HWND,36,                        #attribute no.36 is targeting the title bar text color
                                        byref(c_int(title_text_color)),
                                        sizeof(c_int)) 
except:
    pass

# background image
c=Canvas(root,height=1, width=1)
chibi = Image.open("pics/herta chibi.png")
chibi = ImageTk.PhotoImage(file= "pics/herta chibi.png")
background_label = Label(root, image=chibi)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

root.config(background='#765873')

#root canvas interface
global welcome_message, flavor_text
welcome_message = Label(root, text = "Welcome to Kuru Kuru!", bg='SystemButtonFace', fg='black', font="Verdana 32 bold italic")
welcome_message.place(x=90, y=0)
flavor_text = Label(root, text= "Application for all of your Kuru Kuru needs! *genius noises intensifies*", bg='SystemButtonFace', fg='black', font= "Comic 14 bold italic")
flavor_text.place(x=60, y=63)

x_pos = 0
y_pos = 0


#Transparency hack?
#root.wm_attributes('-transparentcolor', 'red')  #Transparency that even goes through the window?

# leave global label out so it doesn't recuriveness what-evamabob for every frame. yuck...
gif_labels = [] # Store GIF labels

# preload Gif frames

gif_frames = []

def preload_gif_frames():
    global tk_image
    img = Image.open("pics/kurukuru-kururing.gif")
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert("RGBA")               
        tk_image = ImageTk.PhotoImage(frame)
        gif_frames.append(tk_image)

def add_gif():
    global gif_lbl
    bg_color = "SystemButtonFace" if light_dark_mode else "#26242f"
    gif_lbl = Label(root, bg=bg_color)
    gif_lbl.place(x=800,y=88)
    gif_labels.append(gif_lbl)
    thread = threading.Thread(target=play_gif, args=(gif_lbl,))
    thread.start()

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

def gif_2():
    global img2, img2_gif, img2_gif_lbl
    img2 = Image.open("pics/kurukuru-kururing.gif")
    desired_width = 80
    desired_height = 80
    resized_img2 = img2.resize((desired_width, desired_height), Image.ANTIALIAS)
    img2_gif = ImageTk.PhotoImage(resized_img2)

    img2_gif_lbl = Label(root, image=img2_gif)
    img2_gif_lbl.image = img2_gif

    img2_gif_lbl.place(x=700, y=-20)

   

# play Kuru Kuru

#Options window
def options_menu():
    global w3, lng_txt
    pygame.mixer.init()
    w3 = Toplevel()
    w3.title("Options")
    w3.geometry("500x500")
    w3.configure(bg="SystemButtonFace")
    lng_txt = Label(w3, text="Language Settings", bg="SystemButtonFace", fg="black", font="Verdana 10 bold italic")
    lng_txt.place(x=0, y=90)

    volume_control()
    light_dark_function()
    eng_lng_button()
    jpn_lng_button()
    chn_lng_button()
    kor_lng_button()

    root.lift()

# Set Languages
global w3
eng = True
jpn = True
chn = True
kor = True


def set_lng_eng():
    global eng, jpn, chn, kor
    pygame.mixer.init()
    random_sound2 = random.choice(english_list)
    pygame.mixer.music.load(random_sound2)
    pygame.mixer.music.play(loops=0)

    eng = False
    jpn = True
    chn = True
    kor = True


def eng_lng_button():
    global eng_btn
    eng_img = Image.open("pics/english.png")
    eng_photo = ImageTk.PhotoImage(eng_img)
    eng_btn = Button(w3, image=eng_photo,bg="SystemButtonFace",command=set_lng_eng, borderwidth=0)
    eng_btn.image = eng_photo
    eng_btn.place(x=0, y=110)
    eng_btn.bind("<Enter>", on_enter)
    eng_btn.bind("<Leave>", on_leave)

def set_lng_jpn():
    global jpn, eng, chn, kor
    pygame.mixer.init()
    random_sound1 = random.choice(japanese_list)
    pygame.mixer.music.load(random_sound1)
    pygame.mixer.music.play(loops=0)

    jpn = False
    eng = True
    chn = True
    kor = True


def jpn_lng_button():
    global jpn_btn
    jpn_img = Image.open("pics/japanese.png")
    jpn_photo = ImageTk.PhotoImage(jpn_img)
    jpn_btn = Button(w3, image=jpn_photo,bg="SystemButtonFace", command=set_lng_jpn, borderwidth=0)
    jpn_btn.Image = jpn_photo
    jpn_btn.place(x=120, y=110)
    jpn_btn.bind("<Enter>", on_enter)
    jpn_btn.bind("<Leave>", on_leave)

def set_lng_chn():
    global jpn, eng, chn, kor
    pygame.mixer.init()
    random_sound3 = random.choice(chinese_list)
    pygame.mixer.music.load(random_sound3)
    pygame.mixer.music.play(loops=0)

    chn = False
    eng = True
    jpn = True
    kor = True

def chn_lng_button():
    global chn_btn
    chn_img = Image.open("pics/chinese.png")
    chn_photo = ImageTk.PhotoImage(chn_img)
    chn_btn = Button(w3, image=chn_photo,bg="SystemButtonFace",command=set_lng_chn, borderwidth=0)
    chn_btn.image = chn_photo
    chn_btn.place(x=240, y=110)
    chn_btn.bind("<Enter>", on_enter)
    chn_btn.bind("<Leave>", on_leave)

def set_lng_kor():
    global jpn, eng, chn, kor
    pygame.mixer.init()
    random_sound4 = random.choice(korean_list)
    pygame.mixer.music.load(random_sound4)
    pygame.mixer.music.play(loops=0)

    kor = False
    chn = True
    eng = True
    jpn = True

def kor_lng_button():
    global kor_btn
    kor_img = Image.open("pics/korean.png")
    kor_photo = ImageTk.PhotoImage(kor_img)
    kor_btn = Button(w3, image=kor_photo,bg="SystemButtonFace",command=set_lng_kor, borderwidth=0)
    kor_btn.image = kor_photo
    kor_btn.place(x=360, y=110)
    kor_btn.bind("<Enter>", on_enter)
    kor_btn.bind("<Leave>", on_leave)

def play_sound():
    global japanese_list, english_list, chinese_list, korean_list, eng, jpn
    pygame.mixer.init()

    #List of Sounds

    japanese_list =["audio/Kuru kuru~ sound.mp3", "audio/Herta's Kururin (Sound Effect).mp3", "audio/Herta Kururin voice line _ Honkai Star Rail.mp3"]
    english_list = ["audio/eng1.mp3", "audio/eng2.mp3"]
    chinese_list = ["audio/chn1.mp3", "audio/chn2.mp3"]
    korean_list = ["audio/kor1.mp3", "audio/kor2.mp3"]

    #Choose a sound randomly (Japanese Default)

    random_sound = random.choice(japanese_list)
    pygame.mixer.music.load(random_sound)
    pygame.mixer.music.play(loops=0)

    if eng == False:
        set_lng_eng()

    if jpn == False:
        set_lng_jpn()

    if chn == False:
        set_lng_chn()

    if kor == False:
        set_lng_kor()

#Volume control & settings
def set_vol(val):
    global volume
    volume=int(val)/100
    pygame.mixer.music.set_volume(volume)

def volume_control():

    #volume control
    global vol_lbl
    vol_lbl = Label(w3, text="Volume", font="Verdana 10 bold italic")
    vol_lbl.place(x=0,y=0)

    global scale 
    scale=Scale(w3, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
    scale.set(70)
    pygame.mixer.music.set_volume(0.7)
    scale.place(x=0,y=20)


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
    global shadowdrop_img, seseren_kr_img, w2, shadowdrop_btn, seseren_kr_btn, duiqt_btn, duiqt_img
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

def on_enter4(h):
    h.widget['background'] = '#darkgrey'

def on_leave4(h):
    h.widget['background'] = '#26242f'

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

options_button = Button(root, text="Options", command=options_menu)
options_button.place(x=650, y=665)

options_button.bind("<Enter>", on_enter)
options_button.bind("<Leave>", on_leave)

github_button = Button(root, text="GitHub Respository\n-Kuru-Kuru-App", command=github_link)
github_button.place(x=650, y=700)

github_button.bind("<Enter>", on_enter)
github_button.bind("<Leave>", on_leave)

# Click Milestone comments! -----------------------------------------------------------------------------------------------------------------------------------------------------

def Milestone_Comments():
    global milestone_text
    if counter == 10:
        milestone_text = Label(root, text="10 Kurus! The spinning has only just begun!", fg='black', bg='#F9F3F7', font="Comic 12 bold italic")
        milestone_text.place(x=255, y= 645)
       
    if counter == 50:
        if milestone_text:
            milestone_text.config(text="50 kuru's is nothing for true bonafide geniuses!")

    if counter == 100:
        if milestone_text:
            milestone_text.config(text="100 Kuru's! Keep on spinning baby!")
            
#version no. update ------------------------------------------------------------------------------------------------------------------------------------------------------------
global version_lbl
version_lbl = Label(root, text="1.3.0", font= "Comic 10 bold italic", fg="black")
version_lbl.place(x=750, y=770)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


light_dark_mode = True
def light_dark_toggle():
    global light_img, light_dark_btn, light_dark_mode, dark_img, gif_lbl

    if light_dark_mode: #Changed to DARK MODE
        light_dark_btn.config(image=dark_photo, bg="#26242f", activebackground="#26242f")
        light_dark_btn.image = dark_photo

        #Root Changes
        background_label.config(bg="#26242f")
        welcome_message.config(bg='#26242f', fg='#A249A2')
        flavor_text.config(bg='#26242f', fg='#C87BC8')
        version_lbl.config(bg='#26242f', fg='#A249A2')
        img2_gif_lbl.config(bg="#26242f")

        if 'milestone_text' in globals():
            milestone_text.config(bg='#26242f', fg='#C87BC8')

        if 'w2' in globals() and w2.winfo_exists():
            w2.config(bg="#26242f")
            cred_lbl.config(bg="#26242f", fg="#A249A2")
            cred_lbl2.config(bg="#26242f", fg="#C87BC8")
            shadowdrop_btn.config(bg="#26242f", fg="#C87BC8")
            seseren_kr_btn.config(bg="#26242f", fg="#C87BC8")
            duiqt_btn.config(bg="#26242f", fg="#C87BC8")

            shadowdrop_btn.bind("<Leave>", on_leave4)
            seseren_kr_btn.bind("<Leave>", on_leave4)
            duiqt_btn.bind("<Leave>", on_leave4)
            

        #Options Menu Changes
        w3.config(bg="#26242f")
        vol_lbl.config(fg="white",bg="#26242f")
        scale.config(bg="#26242f", fg="white")
        lng_txt.config(bg="#26242f", fg="white")
        eng_btn.config(bg="#26242f")
        jpn_btn.config(bg="#26242f")
        chn_btn.config(bg="#26242f")
        kor_btn.config(bg="#26242f")

        eng_btn.bind("<Leave>", on_leave4)
        jpn_btn.bind("<Leave>", on_leave4)
        chn_btn.bind("<Leave>", on_leave4)
        kor_btn.bind("<Leave>", on_leave4)


        light_dark_mode = False
        
    
    else:
        light_dark_btn.config(image=light_photo, bg="SystemButtonFace", activebackground="SystemButtonFace")
        light_dark_btn.image = light_photo

        #Root Changes
        background_label.config(bg="SystemButtonFace")
        welcome_message.config(bg='SystemButtonFace', fg='black')
        flavor_text.config(bg='SystemButtonFace', fg='black')
        version_lbl.config(bg='SystemButtonFace', fg='black')
        img2_gif_lbl.config(bg="SystemButtonFace")

        if 'milestone_text' in globals():
            milestone_text.config(bg="SystemButtonFace", fg="black")

        if 'w2' in globals() and w2.winfo_exists():
            w2.config(bg="white")
            cred_lbl.config(bg="white", fg="black")
            cred_lbl2.config(bg="white", fg="black")
            shadowdrop_btn.config(bg="white", fg="black")
            seseren_kr_btn.config(bg="white", fg="black")
            duiqt_btn.config(bg="white", fg="black")

            shadowdrop_btn.bind("<Leave>", on_leave3)
            seseren_kr_btn.bind("<Leave>", on_leave3)
            duiqt_btn.bind("<Leave>", on_leave3)

        #Option Menu Changes
        w3.config(bg="SystemButtonFace")
        vol_lbl.config(fg="black",bg="SystemButtonFace")
        scale.config(bg="SystemButtonFace", fg="Black")
        lng_txt.config(bg="SystemButtonFace", fg="black")
        eng_btn.config(bg="SystemButtonFace")
        jpn_btn.config(bg="SystemButtonFace")
        chn_btn.config(bg="SystemButtonFace")
        kor_btn.config(bg="SystemButtonFace")

        eng_btn.bind("<Leave>", on_leave)
        jpn_btn.bind("<Leave>", on_leave)
        chn_btn.bind("<Leave>", on_leave)
        kor_btn.bind("<Leave>", on_leave)

        light_dark_mode = True
    

def light_dark_function():
    global desired_height, desired_width, resized_light, resized_dark, light_dark_btn, light_photo, dark_photo

    on = Image.open('pics/light mode button.png')
    off = Image.open('pics/dark mode button.png')
    desired_width = 200
    desired_height = 200

    resized_light = on.resize((desired_width, desired_height), Image.ANTIALIAS)
    resized_dark = off.resize((desired_width, desired_height), Image.ANTIALIAS)

    light_photo = ImageTk.PhotoImage(resized_light)
    dark_photo = ImageTk.PhotoImage(resized_dark)

    light_dark_btn = Button(w3, image=light_photo, command=light_dark_toggle, borderwidth=0)
    light_dark_btn.image = light_photo
    light_dark_btn.place(x=0, y=400)



preload_gif_frames()
gif_2()

root.mainloop()

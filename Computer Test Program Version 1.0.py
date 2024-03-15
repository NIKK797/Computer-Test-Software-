from tkinter import *
import webbrowser

root = Tk()
root.title("Computer MCQS Program")

h = 4
w = 45
nikhil = "Creator"
nikhil = nikhil
question_color = "#e3e0cf"
option_color = "LightBlue"
nextBt_color = "Gray"
no_color = "White"
cons_encoding = "utf-8"


#Variables
    
def right():
    Label(root, text="Right Answer!", height=h, width=w, background="Lime").grid(row=6, column=2)

def wrong():
    Label(root, text="Wrong Answer!", height=h, width=w, background="Red").grid(row=6, column=2)

def fin():
    exit()

#Questions

# def e_s():
#     er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
#     er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
#     Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
#     Q1 = Label(root,height=h, width=w, background=no_color).grid(row=1, column=2)
#     B1 = Label(root, text="", height=h, width=w, background=no_color).grid(row=2, column=2)
#     B2 = Label(root, text="", height=h, width=w, background=no_color).grid(row=3, column=2)
#     B3 = Label(root, text="", height=h, width=w, background=no_color).grid(row=4, column=2)
#     B4 = Label(root, text="", height=h, width=w, background=no_color).grid(row=5, column=2)

def q50():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(50) Each layer has its own set of _________", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Amount", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Value", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Panels", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Parameter", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Finish", height=h, width=w, background=nextBt_color, command=fin).grid(row=7, column=2)

def q49():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(49) Which of the following have their own layer ? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Object", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Element", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Effect", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) All of above", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q50).grid(row=7, column=2)


def q48():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(48) Inserted image can enhance the \nanimation by _______ operation.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Scale", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Rotate", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Both (a) and (b)", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q49).grid(row=7, column=2)



def q47():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(47) Which layer will resize the image keeping\n its aspect ratio? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Amount", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Scale", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) Rotate", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Bline", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q48).grid(row=7, column=2)


def q46():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(46) Which color duck is used to resize the image?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Yellow", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Orange", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Green", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Blue", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q47).grid(row=7, column=2)


def q45():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text=" (45) How many types of gradient tools are available \nin synfig ? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) 3", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) 4", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) 5", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) 6", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q46).grid(row=7, column=2)


def q44():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(44) What option you can find in image tab ?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Image Area, Image Time", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Image Time, Image Size", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Image Size, Image Area", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Image Name, Image Size", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q45).grid(row=7, column=2)



def q43():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(43) Which property specifies that the parameter \nis control automatically in different ways ?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Amount", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Convert", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Interpolation", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Z-depth", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q44).grid(row=7, column=2)



def q42():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(42) By which term the analog and digital form of \nthe sound is known respectively ?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Audio, Sound", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Sound, Video", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Audio, Video", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Sound, Audio", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q43).grid(row=7, column=2)



def q41():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(41) In which type of multimedia, the user simply watches\n the media as it plays from beginning to the end ? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Non-interactive", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) Interactive", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Both (a) and (b)", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q42).grid(row=7, column=2)



def q40():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(40) In synfig, if we wish to repeat the animation again \nthen which parameter denotes the frames or \nseconds that are looped ?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Time", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Length", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Duration", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) jmp", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q41).grid(row=7, column=2)



def q39():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(39) In synfig how can we open properties dialog box? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) File ==> Caret ==> Properties", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Caret ==> File ==> Properties", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Edit ==> Caret ==> Properties", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Caret ==> Edit ==> Properties", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q40).grid(row=7, column=2)


def q38():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(38) In tools options panel, which option is \nonly to be selected while creating a path using Bline ? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Create Region Bline", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Create Outline Bline", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) Link origin", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q39).grid(row=7, column=2)


def q37():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(37) ____ refers to different levels that gives us \nthe freedom to work with each object individually?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Parameter", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Tool options", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Layer", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Toolbox", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q38).grid(row=7, column=2)



def q36():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(36) Which blend method is used to apply \ngradient effect only to the object below it?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Composite", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Straight", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Straight onto", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Alpha over", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q37).grid(row=7, column=2)



def q35():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(35) Which multimedia element can be used, \nto communicate information to user?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Audio", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Video", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Text", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Graphic", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q36).grid(row=7, column=2)



def q34():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(34) Which type of animation is\n known as  cel animation?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Kinematic", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Tweening", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) Morphing", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) All of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q35).grid(row=7, column=2)


def q33():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(33) A circle has _______ important parameters.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) 2", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) 3", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) 4", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) 5", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q34).grid(row=7, column=2)



def q32():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(32) At Synfig application, ____show options that\n are specific to the currently selected tool.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Layer Panel", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) History Panel", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Params Panel", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Tool Options Panel", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q33).grid(row=7, column=2)



def q31():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(31) Closing the ________, exists the Synfig application. ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Toolbox", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) Canvas", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Panel", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) All of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q32).grid(row=7, column=2)


def q30():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(30) ____ key is used to remove Bline", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) delete", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) home", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) esc", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q31).grid(row=7, column=2)


def q29():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(29) ___tool is used to close Bline tool. ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Deselect tool", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Bline tool", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Transform tool", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q30).grid(row=7, column=2)


def q28():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(28) On importing some image in Synfig to \nwhich panel does that image layer appear as added?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Params Panel", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Tools option Panel", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Image Panel", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Layer Panel", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q29).grid(row=7, column=2)


def q27():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(27) How many options are there for importing \nimage on canvas?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Only 1", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) 2", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) 3", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) 4", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q28).grid(row=7, column=2)


def q26():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(26) Grouping things together is known as_______", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Adding", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Cluster", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Parameter", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Encapsulation", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q27).grid(row=7, column=2)



def q25():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(25) Which value of parameter before suggests\n that layer had been visible in parameter panel?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) 0.0", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) 1.0", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) 1.1", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) 0.1", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q26).grid(row=7, column=2)


def q24():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(24) To change the size of the image in Synfig \nwhich variables value is changed?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Length", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Scale", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Origin", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Amount", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q25).grid(row=7, column=2)


def q23():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(23) ____ location we have to specify for moving object.  ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Starting point", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Ending point", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Both (a) and (B)", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Location of all points", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q24).grid(row=7, column=2)



def q22():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(22) _____ shows the duration of the time in keyframe panel. ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Time", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Length", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) Jump", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Description", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q23).grid(row=7, column=2)


def q21():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(21) ___ is used for the color of circle.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Foreground color", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Palette", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Parameter Panel", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) All of these", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q22).grid(row=7, column=2)


def q20():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(20) How many buttons are there on the\n right side of the canvas?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) 2", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) 3", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) 4", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) 5", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q21).grid(row=7, column=2)


def q19():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(19) Each waypoint has _________ setting. ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Foreground color", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Background color", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Gradient", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Interpolation", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q20).grid(row=7, column=2)


def q18():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(18) There are ________ tools in the upper palette.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) 8", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) 10", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) 12", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) 14", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q19).grid(row=7, column=2)



def q17():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(17) In icon and event based tool, we need to build the _____ \nof the events or tasks and then add the\n elements as per the structure.   ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Program ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Function", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Flowchart", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Algorithm", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q18).grid(row=7, column=2)



def q16():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(16) To see the gradient effect on the object,\n the object color is set to____ ?   ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Predefined color ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Any color", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) White color", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Black color", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q17).grid(row=7, column=2)


def q15():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(15) Which layer will be added when we \nencapsulate layers in layer panel ?  ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Scale layer ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Rotate layer", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Inline canvas layer", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Canvas layer", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q16).grid(row=7, column=2)



def q14():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(14) ____ option is used to listen to the \nrecording in Sound Recorder. ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) File ==> Play ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Audio ==> Play", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Control ==> Play", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Format ==> Play", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q15).grid(row=7, column=2)



def q13():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(13) ____ is the multimedia software player for \nfree download on Ubuntu software center  ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Synfig Studio ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Blender", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) VLC media player", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q14).grid(row=7, column=2)


def q12():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(12) What we have to use to repeat animation again \nand again ? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Duplication ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Time loop", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) Both (a) and (b)", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q13).grid(row=7, column=2)


def q11():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(11) Which audio file of windows\n media supports compressed format? ", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) .wma ", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) .wav", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) .ram", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) .mid", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q12).grid(row=7, column=2)


def q10():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(10) To store pictures, computer uses\n form of pixels maps also known as __", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A)Bitmap/raster ", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) vector", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Both (a) and (b)", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q11).grid(row=7, column=2)


def q9():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(9) ___ is used to display fonts in \nattractive manner in Open Office lmpress.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Word art ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Text art", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Object art", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) Font work", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q10).grid(row=7, column=2)


def q8():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(8) The text can have ____ to suite professional requirement.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Type and size ", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) Color", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Style", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) All of these", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q9).grid(row=7, column=2)


def q7():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(7) How many elements are there in multimedia?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) 3", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) 4", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) 5", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) 6", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q8).grid(row=7, column=2)

def q6():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(6) ____ is the most widely used format for the internet video.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) .swf", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) .wmv", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) .mpeg", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) .mp4", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q7).grid(row=7, column=2)


def q5():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(5) _______is the extension for Quick Time Format file.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) .mpg", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) .mp4", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) .avi", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) .mov", height=h, width=w, background=option_color, command=right).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q6).grid(row=7, column=2)


def q4():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(4)____ format is used for web graphics \nwith small images and images with text.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) .jpeg", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) .gif", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) .bmp", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) .tif", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q5).grid(row=7, column=2)


def q3():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(3)If large amount of written data is to be read\n then __________ typeface is used.", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) Serif", height=h, width=w, background=option_color, command=right).grid(row=2, column=2)
    B2 = Button(root, text="(B) Sans Serif", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) Both (a) and (b)", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D)None of these", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q4).grid(row=7, column=2)


def q2():
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(2)If we have a font of Times new roman 14 point\n then times new roman is _______ and 14 point is _______", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) element, size", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) size, style", height=h, width=w, background=option_color, command=wrong).grid(row=3, column=2)
    B3 = Button(root, text="(C) style, size", height=h, width=w, background=option_color, command=right).grid(row=4, column=2)
    B4 = Button(root, text="(D) Style, element", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q3).grid(row=7, column=2)


def q1():
    root.minsize(320, 486)
    root.maxsize(320, 486)
    er = Label(root, height=h, width=w, background=no_color).grid(row=1, column=2, sticky=N)
    er1 = Label(root, height=h, width=w, background=no_color).grid(row=2, column=2)
    Label(root, height=h, width=w, background=no_color).grid(row=6, column=2)
    Q1 = Label(root, text="(1)Which type of file supports up to 24-bit and 32-bit \ncolors respectively?", height=h, width=w, background=question_color).grid(row=1, column=2)
    B1 = Button(root, text="(A) .png, .jpeg", height=h, width=w, background=option_color, command=wrong).grid(row=2, column=2)
    B2 = Button(root, text="(B) .jpeg, .png", height=h, width=w, background=option_color, command=right).grid(row=3, column=2)
    B3 = Button(root, text="(C) .gif, .png", height=h, width=w, background=option_color, command=wrong).grid(row=4, column=2)
    B4 = Button(root, text="(D) .gif, .jpeg", height=h, width=w, background=option_color, command=wrong).grid(row=5, column=2)
    Nxt = Button(root, text="Next", height=h, width=w, background=nextBt_color, command=q2).grid(row=7, column=2)

t = "h"
i = "i"
l = "N"
a = "k"
e = "l"

main = Label(root, text="Computer MCQS Test \n \n Created By Khambhaliya " + l + i + a + t + i + e + "\n Guided By Nuzhat Mam", height=h, width=w, background=question_color).grid(row=1, column=2, sticky=N)
b_main = Button(root, text="START", height=h, width=w, background=option_color , command=q1).grid(row=2, column=2)

root.mainloop()
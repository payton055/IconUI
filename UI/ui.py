import tkinter as tk
from tkinter import *
from tkinter import filedialog
import color
import customtkinter as ctk
from PIL import Image, ImageTk
import cairosvg


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.wm_attributes("-transparentcolor", "#123")
root.title("Select Color")
root.geometry(f"{900}x{750}")

variable = "Kind of Blue"
c = ctk.StringVar()  
c.set(variable)

openfilename = ""
svgcommand = ""
savefilename = ""

data = {}
colors = color.colors()
data = colors

def openfile():
    global openfilename
    global svgcommand
    openfilename = filedialog.askopenfilename()

    f = open(openfilename, "r")
    svgcommand = f.read()

    cairosvg.svg2png(url=openfilename, write_to='output.png', output_width=140, output_height=140)
    
    ori_img = ctk.CTkImage(light_image=Image.open('output.png'),size=(140, 140))
    pic = ctk.CTkLabel(img_bef,text="",image=ori_img)
    pic.grid(column=0, row=0,padx=10,pady=10)

    aft_img1 = ctk.CTkButton(img_aft1 ,image=ori_img,text="",fg_color="transparent",hover_color="grey",width=200,height=200) #TODO Update processed image and select function
    aft_img1.grid(column=0, row=0,padx=5,pady=5)

    if openfilename == "":return

def savefile(): #TODO
    global savefilename
    
    savefilename = filedialog.asksaveasfile(mode='w',filetypes=[("svg files", "*.svg")])
    savefilename.write(svgcommand)
    savefilename.close()
    if savefilename == "":return

def setcolor(value):
    global variable       
    variable=value        
    c.set(variable)
    canvas.create_rectangle(8, 8, 40, 40, fill=colors[variable][0],width=0)
    canvas.create_rectangle(48, 8, 80, 40, fill=colors[variable][1],width=0)
    canvas.create_rectangle(88, 8, 120, 40, fill=colors[variable][2],width=0)
    canvas.create_rectangle(128, 8, 160, 40,  fill=colors[variable][3],width=0)
    canvas.create_rectangle(168, 8, 200, 40,  fill=colors[variable][4],width=0) #TODO update image by color palette


mylabel = ctk.CTkLabel(root, textvariable=c, font=('Arial',20),width=200,wraplength=200)
mylabel.grid(column=3, row=2)

canvas = tk.Canvas(root, width=208, height=48,bg="lightgrey",highlightthickness=0)
canvas.create_rectangle(8, 8, 40, 40, fill=colors[variable][0],width=0)
canvas.create_rectangle(48, 8, 80, 40, fill=colors[variable][1],width=0)
canvas.create_rectangle(88, 8, 120, 40, fill=colors[variable][2],width=0)
canvas.create_rectangle(128, 8, 160, 40,  fill=colors[variable][3],width=0)
canvas.create_rectangle(168, 8, 200, 40,  fill=colors[variable][4],width=0)

canvas.grid(column=3, row=3,pady=0,sticky="n")

selectcolor = ctk.CTkScrollableFrame(root,width=400,height=550)
count = 1
for i in data:
    btn = ctk.CTkButton(selectcolor,text='',fg_color="transparent",width=400)
    a = ctk.CTkButton(btn, command = lambda i=i: setcolor(i),text=i,text_color="#2F4F4F",width=400,fg_color="darkgray",hover_color="grey")
    c1 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][0], width=80, height=2)
    c2 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][1], width=80, height=2)
    c3 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][2], width=80, height=2)
    c4 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][3], width=80, height=2)
    c5 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][4], width=80, height=2)

    a.grid(column=0, row=0,columnspan=5,padx=0)
    c1.grid(column=0, row=1,padx=0)
    c2.grid(column=1, row=1,padx=0)
    c3.grid(column=2, row=1,padx=0)
    c4.grid(column=3, row=1,padx=0)
    c5.grid(column=4, row=1,padx=0)
    btn.grid(column=0, row=count,sticky="ew",pady=5)
    count += 1
selectcolor.grid(column=0, row=2,rowspan=4,sticky="n",padx=10)


def Scankey(event):
    val = event.widget.get()
#    print(val)
    global data

    if val == '':
        if(len(data) != len(colors)):
            data = colors
            update = TRUE
    else:
        data = {}
        for item in colors:
            if val.lower() in item.lower():
                data[item] = colors[item]
        update = TRUE
    if(update):
        selectcolor = ctk.CTkScrollableFrame(root,width=400,height=550)
        count = 1
        for i in data:
            btn = ctk.CTkButton(selectcolor,text='',fg_color="transparent",width=400)
            a = ctk.CTkButton(btn, command = lambda i=i: setcolor(i),text=i,width=400)
            c1 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][0], width=80, height=2)
            c2 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][1], width=80, height=2)
            c3 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][2], width=80, height=2)
            c4 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][3], width=80, height=2)
            c5 =  ctk.CTkLabel(btn, text='',fg_color=colors[i][4], width=80, height=2)

            a.grid(column=0, row=0,columnspan=5,padx=0)
            c1.grid(column=0, row=1)
            c2.grid(column=1, row=1)
            c3.grid(column=2, row=1)
            c4.grid(column=3, row=1)
            c5.grid(column=4, row=1)
            btn.grid(column=0, row=count,pady=2)
            count += 1
        selectcolor.grid(column=0, row=2,rowspan=4,sticky="n",padx=10)


entry = ctk.CTkEntry(root, placeholder_text="Enter to search...")
entry.grid(column=0, row=1,sticky="n",pady=40)
entry.bind('<KeyRelease>', Scankey)

openf = ctk.CTkButton(root,text="Open",command = openfile)
openf.grid(column=2,row=1,padx=30,pady=10)

savef = ctk.CTkButton(root,text="Save",command = savefile)
savef.grid(column=3,row=1,padx=30,pady=10)

img_bef = ctk.CTkFrame(root, width=160, height=160)
img_bef.grid(column=2, row=2,pady=3,rowspan=2)

img_aft1 = ctk.CTkFrame(root, width=210, height=210)
img_aft1.grid(column=2, row=4,padx=3,pady=3)

img_aft2 = ctk.CTkFrame(root, width=210, height=210)
img_aft2.grid(column=2, row=5,padx=3,pady=3)

img_aft3 = ctk.CTkFrame(root, width=210, height=210)
img_aft3.grid(column=3, row=4,padx=3,pady=3)

img_aft4 = ctk.CTkFrame(root, width=210, height=210)
img_aft4.grid(column=3, row=5,padx=3,pady=3)

'''my_image = ctk.CTkImage(light_image=Image.open('output.png'),size=(200, 200))
pic = ctk.CTkLabel(img_bef,text="",image=my_image)
pic.grid(column=0, row=0,padx=25,pady=25)'''

root.mainloop()


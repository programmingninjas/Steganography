import cv2
from tkinter import filedialog, Tk, Button, Label, PhotoImage
from PIL import Image, ImageTk
import numpy as np

global image_path

image_display_size = 500, 350

def browse():
    global image_path
    image_path = filedialog.askopenfilename()

def decrypt():
    global image_path
    # load the image and convert it into a numpy array and display on the GUI.
    load = Image.open(image_path)
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(app, image=render)
    img.image = render
    img.place(x=100, y=100)

    # Algorithm to decrypt the data from the image
    img = cv2.imread(image_path)
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    # join all the bits to form letters (ASCII Representation)
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    # join all the letters to form the message.
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    message_label = Label(app, text=message, font=("Times New Roman", 20))
    message_label.place(x=30, y=500)


# Defined the TKinter object app with background lavender, title Decrypt, and app size 600*600 pixels.
app = Tk()
app.title("Decrypt")
app.geometry('600x600')
app.iconbitmap('unlock.ico')

#background
bg_image = PhotoImage(file='bg.png')
bg = Label(app,image=bg_image)
bg.place(x=0, y=0, relwidth=1, relheight=1)

# Add the button to call the function browse.
browse_button = Button(app, text="Load Image", bg='white', fg='black', font=("Times New Roman", 20,'bold'), command=browse)
browse_button.place(x=150, y=10)

# Add the button to call the function decrypt.
image = PhotoImage(file='unlock.png')
main_button = Button(app,image=image,width='128',height='128',bd=5,command=decrypt)
main_button.place(x=400, y=10)

label = Label(app, text='Decrypt', font=("Times New Roman", 20,'bold'))
label.place(x=420, y=160)
app.mainloop()

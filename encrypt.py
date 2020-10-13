from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math

global path_image

image_display_size = 300, 300

def on_click():
    # Step 2

    global path_image

    # use the tkinter filedialog library to open the file using a dialog box.
    # obtain the image of the path

    path_image = filedialog.askopenfilename()

    # load the image using the path

    load_image = Image.open(path_image)

    # set the image into the GUI using the thumbnail function from tkinter

    load_image.thumbnail(image_display_size, Image.ANTIALIAS)

    # load the image as a numpy array for efficient computation and change the type to unsigned integer

    np_load_image = np.asarray(load_image)

    np_load_image = Image.fromarray(np.uint8(np_load_image))

    render = ImageTk.PhotoImage(np_load_image)

    img = Label(app, image=render)

    img.image = render

    img.place(x=20, y=50)

def encrypt_data_into_image():

    # Step 3

    global path_image

    data = txt.get(1.0, "end-1c")

    # load the image

    img = cv2.imread(path_image)

    # break the image into its character level. Represent the characyers in ASCII.

    data = [format(ord(i), '08b') for i in data]

    _, width, _ = img.shape

    # algorithm to encode the image

    PixReq = len(data) * 3

    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0

    # Step 4

    for i in range(RowReq + 1):

        # Step 5
        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            # Step 6
            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    # Step 7
    # Write the encrypted image into a new file
    cv2.imwrite("encrypted_image.png", img)
    # Display the success label.
    success_label = Label(app, text="Encryption Successful!"
                , font=("Times New Roman", 20))
    success_label.place(x=160, y=300)

# Step 1
# Defined the TKinter object app with background lavender, title Encrypt, and app size 600*600 pixels.
app = Tk()
app.title("Encrypt")
app.geometry('600x600')
app.iconbitmap('lock.ico')

#background
bg_image = PhotoImage(file='bg.png')
bg_label = Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# create a button for calling the function on_click
on_click_button = Button(app,text="Choose Image",fg='black', font=("Times New Roman", 15,'bold'), command=on_click)
on_click_button.place(x=50, y=375)
# add a text box using tkinter's Text function and place it at (340,55). The text box is of height 165pixels.
txt = Text(app, wrap=WORD, width=30)
txt.place(x=340, y=55, height=165)

image=PhotoImage(file='lock.png')
encrypt_button = Button(app,image=image,width='128',height='128',command=encrypt_data_into_image,bd=5,bg='lavender')
encrypt_button.place(x=435, y=230)

encrypt_label = Label(app,text='Encrypt', font=("Times New Roman", 20,'bold'))
encrypt_label.place(x=460, y=375)


app.mainloop()

from tkinter import*

def change_img():
    path=inputBox.get()
    img=PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image=img

window = Tk()
photo=PhotoImage(file="우주소녀.gif")
imageLabel=Label(window,image=photo)
imageLabel.pack()
inputBox=Entry(window)
inputBox.pack()
button=Button(window,text="click",command=change_img)
button.pack()

#l1=Label(window, text="1번말",bg="red",fg="white")
#l2=Label(window, text="2번말",bg="green",fg="white")
#l3=Label(window, text="3번말",bg="blue",fg="white")

#l1.place(x=0,y=0)
#l2.place(x=100,y=30)
#l3.place(x=200,y=60)

window.mainloop()

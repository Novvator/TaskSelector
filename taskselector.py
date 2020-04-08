import random
import tkinter as tk

def handler(event):
    text=entry.get()
    tex = ""
    list1.append(text)
    for i in list1:
        tex = tex +str(i) + '\n' 
    changeText(listView,tex)
    entry.delete(0,tk.END)
    
def changeText(self,textt):
    self.configure(text=textt)

def choseTask():
    if(len(list1)!=0):
        changeText(label1,"The task you have to do is: " + list1[random.randint(0,len(list1)-1)])
    else:
        changeText(label1,"Not enough items in the To-do list")
        
def center_window(width=700, height=700):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

list1 = []

root = tk.Tk()
center_window(700, 700)

root.title('Task Selector')
        
root.bind("<Return>", handler)

canvas = tk.Canvas(root, height=700, width=700, bg="#809FFF")
canvas.pack()


    
label = tk.Label(canvas, text = "Write the tasks you have to do and press the button when you are finished", bg='white')
label.place(relwidth=0.57, relheight=0.03, relx=0.215, rely=0.035)

listView = tk.Label(canvas, bg='white', anchor= 'n')
listView.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.1)

label1 = tk.Label(canvas, text = "", bg="#809FFF")
label1.place(relwidth=0.7, relheight=0.03, relx=0.15, rely=0.815)

button = tk.Button(canvas, bg='gray', fg='red', text="Generate Selected Task", command= choseTask)
button.place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.86)

entry = tk.Entry(canvas, bg='white', justify= 'center')
entry.place(relwidth=0.5, relheight=0.05, relx=0.25, rely=0.92)
    






root.mainloop()

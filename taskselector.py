import random
import tkinter as tk

    
def changeText(self,textt):
    self.configure(text =textt)

def chooseMovie():
    list1.append(movielist[random.randint(0,len(movielist))])
    tex = ""
    for i in list1:
        tex = tex + str(i) + '\n' 
    changeText(listView,tex)
        
def center_window(width=700, height=700):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

list1 = []

#open file and export movies to a listt
file = open('watchlist.txt','r',encoding="utf8")
f = file.readlines()

movielist = []
for line in f:
    movielist.append(line.strip())
    

root = tk.Tk()
center_window(700, 700)

root.title('Movie Selector')

canvas = tk.Canvas(root, height=700, width=700, bg="#809FFF")
canvas.pack()


    
label = tk.Label(canvas, text = "Press the button to select a random movie from the list", bg='white')
label.place(relwidth=0.57, relheight=0.03, relx=0.215, rely=0.035)

listView = tk.Label(canvas, bg='white', anchor= 'n')
listView.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.1)

label1 = tk.Label(canvas, text = "", bg="#809FFF")
label1.place(relwidth=0.7, relheight=0.03, relx=0.15, rely=0.815)

button = tk.Button(canvas, bg='gray', fg='red', text="Movie time!", command= chooseMovie)
button.place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.86)
    






root.mainloop()

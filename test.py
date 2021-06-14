import random
import tkinter as tk

canvas = tk.Canvas()
canvas.pack()
root = tk.Tk()
canvas.config(width=1200, height=600)

def rect(lis):
    canvas.create_rectangle(lis[0], lis[1], lis[2], lis[3], fill="red")
def del_():
    canvas.delete("all")


h = [random.randint(20, 600) for n in range(60)] # generates a random set of numbers for heights of rectangles
n = len(h)
for i in range(n-1):
    for j in range(0, n-i-1):
        iter_ = 0
        if j < (n-i-2):
            canvas.after(50, del_)
            canvas.update()
        for item in h:
            x_1 = iter_*20
            y_1 = 600
            x_2 = iter_*20 + 20
            y_2 = 600 - item
            arguments = [x_1,y_1,x_2,y_2]
            canvas.after(50, rect, arguments)
            canvas.update()
            iter_+=1
        if h[j] > h[j+1]:
            h[j], h[j+1] = h[j+1], h[j]
print(h)

root.mainloop()


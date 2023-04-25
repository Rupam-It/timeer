from tkinter import * 
import time

timer=None
#this is for countdown the time 
def start_timer():
    count_down(5*60)


def count_down(count):
    
    sec=count%60
    Min=count//60
    if sec==0:
        canvas.itemconfig(timer_text,text=f"0{Min}:{sec}0")

    elif sec>=1 and sec<10:
        canvas.itemconfig(timer_text,text=f"0{Min}:0{sec}")
    else:
        canvas.itemconfig(timer_text,text=f"0{Min}:{sec}")
    if count>0:
       global timer
       timer= window.after(1000,count_down,count-1)



# this is reset methode
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f"05:00")





window=Tk()
window.title("tomato watch")
window.config(padx=100,pady=50,bg='black')


title_Label=Label(text="stopwatch", font='30')
title_Label.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg='black',highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(102,112,image=tomato_img)
timer_text=canvas.create_text(102,130,text="05:00",font=(40))
canvas.grid(row=1,column=1)




start_Label=Button(text="start",font=(45),command=start_timer)
start_Label.grid(row=2,column=0)

reset_label=Button(text="reset",font=(45),command=reset_time)
reset_label.grid(row=2,column=2)


window.mainloop()
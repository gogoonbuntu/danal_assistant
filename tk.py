import tkinter as tk
import tkinter.font
import main as m

# tkinter


# functions
def open_window():
    bgc = '#574c4f'
    ftc = '#efdab9'
    global check_mail
    global check_stretch

    w = tk.Tk()
    w.title('Settings')
    w.config(bg=bgc)
    w.geometry('400x400+100+100')
    w.resizable(False, False)

    font = tk.font.Font(family="맑은 고딕", size=16)

    
    lb = tk.Label(w, text="Hello Danal", height=5)
    lb.config(fg=ftc, bg=bgc, font=font)
    lb.pack()

    
    check_mail = tk.BooleanVar()
    check_stretch = tk.BooleanVar()
    
    c1 = tk.Checkbutton(w, text="Mail 자동응답", variable=check_mail, selectcolor="#000", bg=bgc, fg=ftc)
    c2 = tk.Checkbutton(w, text="스트레칭 알람", variable=check_stretch, selectcolor="#000", bg=bgc, fg=ftc)
    c1.pack()
    c2.pack()

    space = tk.Label(w, height=2, bg=bgc)
    space.pack()
    
    
    bt = tk.Button(w, width=10, height=1, fg='black', bg='yellow', text='bye', command=byebye)
    bt.pack()
    
    #w.after(500, lambda: w.focus_force())

    w.wm_attributes("-topmost",1)
    w.focus_force()
    
    w.mainloop()
    

from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import tkinter as tk
import tkinter.font
from threading import Thread

# pystray
img = Image.open('image.jpg')
myicon = icon('test', img,
              menu=menu(
                    item(
                        'With submenu',
                        menu(
                            item(
                                'Show message',
                                lambda icon, item: icon.notify('키워드 알림입니다.')
                                ),
                            item(
                                'Submenu item 2',
                                lambda icon, item: icon.remove_notification()
                                )
                            )
                        ),
                    item(
                        'Settings',
                        lambda icon, item: open_window()
                        ),
                    item(
                        'Quit',
                        lambda icon, item: byebye()
                        )
                    )
                )



# tkinter


# functions
def open_window():
    bgc = '#574c4f'
    ftc = '#efdab9'
    auto_mail = False
    stretch = True

    
    w = tk.Tk()
    w.title('Settings')
    w.config(bg=bgc)
    w.geometry('400x400+100+100')
    w.resizable(False, False)

    font = tk.font.Font(family="맑은 고딕", size=16)

    
    lb = tk.Label(w, text="Hello Danal", height=5)
    lb.config(fg=ftc, bg=bgc, font=font)
    lb.pack()

    c1 = tk.Checkbutton(w, text="Mail 자동응답", variable=auto_mail, bg=bgc, fg=ftc)
    c2 = tk.Checkbutton(w, text="스트레칭 알람", variable=stretch, bg=bgc, fg=ftc)
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
    

def byebye():
    myicon.stop()
    exit()

def init():
    t1 = Thread( target = myicon.run )
    t1.start()


open_window()
init()

from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
from threading import Thread, Timer
from multiprocessing import Process, Queue
import tkinter as tk
import tkinter.font
import time
from win10toast import ToastNotifier
import Outlook as ol
from selenium import webdriver as wd


############################ PYSTRAY

img = Image.open('image.jpg')

w = tk.Tk()

check_mail = tk.BooleanVar(w)
check_mail.set(False)
check_stretch = tk.BooleanVar(w)
check_stretch.set(False)
stretch_option=0

bgc = '#574c4f'
ftc = '#efdab9'

ts = ToastNotifier()

keywords = set()
with open('kw.txt', encoding='UTF8') as kw:
    for line in kw :
        keywords.add(line[0:-1])
print(keywords)

thread_outlook = Thread(target=ol.df, args=[keywords])

def cc():
    print('chmail:', check_mail.get())
    print('chstrt:' , check_stretch.get())
    print('strop:', stretch_option)


myicon = icon('test', img,
              menu=menu(
#                    item(
#                        'With submenu',
#                        menu(
#                            item(
#                                'Show message',
#                                lambda icon, item: icon.notify('키워드 알림입니다.')
#                                ),
#                            item(
#                                'Submenu item 2',
#                                lambda icon, item: icon.remove_notification()
#                                )
#                            )
#                        ),
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

def login_on():
    options = wd.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = wd.Chrome('chromedriver', chrome_options=options)
    driver.get('http://naver.com')
    driver.implicitly_wait(3)
    driver.get_screenshot_as_file('naver_main_headless.png')
    
    driver.quit()
    
login_on()

def kw_on():
    global keywords
    print(keywords)
    global thread_outlook
    t = thread_outlook
    print('#####################',t,'########################')
    t.start()

def stretch_on(second=60):
    global check_stretch, stretch_option, ts

    if stretch_option<1 :
        stretch_option = 1
    else :
        stretch_option = 0
    
    print("kkk")
    print('stop:', stretch_option)
    print(time.strftime('%H'))
    sched1 = ['10', '11', '14', '15', '16']
    sched2 = ['11', '15', '17']
    if stretch_option == 1 and time.strftime('%M')=='17' and time.strftime('%H') in sched1:
        ts.show_toast('스트레칭', '합시다~', icon_path='image.ico', duration=10, threaded=True)
    if stretch_option == 2 and time.strftime('%M')=='0' and time.strftime('%H') in sched2:
        ts.show_toast('스트레칭', '합시다~', icon_path='image.ico', duration=10, threaded=True)
    if stretch_option>0 :
        Timer(second, stretch_on, [second]).start()



############################ TKINTER

def open_window():
    global bgc, ftc
    global check_mail, check_stretch
    global w
    w.title('Settings')
    w.config(bg=bgc)
    w.geometry('400x400+100+100')
    w.resizable(False, False)

    font = tk.font.Font(family="맑은 고딕", size=16)

    
    lb = tk.Label(w, text="Hello Danal", height=5, fg=ftc, bg=bgc, font=font)
    lb.pack()    

    c1 = tk.Checkbutton(w, text="Mail 키워드알림", variable=check_mail,
                        selectcolor="#000", bg=bgc, fg=ftc, command=kw_on)
    c2 = tk.Checkbutton(w, text="스트레칭 알람", variable=check_stretch,
                        selectcolor="#000", bg=bgc, fg=ftc, command=stretch_on)
    c1.pack()
    c2.pack()

    space = tk.Label(w, height=2, bg=bgc)
    space.pack()
    


    bt_keyword = tk.Button(w, width=11, height=1, fg='black', bg='yellow', text='키워드설정', command=keywordFunc)
    bt_keyword.place(relx=0.29, rely=0.6)

    bt_stretch = tk.Button(w, width=11, height=1, fg='black', bg='yellow', text='스트레칭 주기', command=stretchFunc)
    bt_stretch.place(relx=0.51, rely=0.6)
    
    bt_quit = tk.Button(w, width=10, height=1, fg='black', bg='yellow', text='bye', command=byebye)
    bt_quit.place(relx=0.4, rely=0.9)
    

    w.wm_attributes("-topmost",1)
    w.focus_force()
    
    w.mainloop()


############################ FUNCTIONS

def byebye():
    myicon.stop()
    exit()

def init():
    t1 = Thread( target = myicon.run )
    t1.start()


    
############################# KEYWORD

def keywordFunc():
    
    global keywords, bgc, ftc
    keywords= set()
    with open('kw.txt', encoding='UTF8') as kw:
        for line in kw :
            keywords.add(line[0:-1])

    def save_kw():
        item_s=list(keywords)
        sorted(item_s)
        with open('kw.txt', 'w', encoding='UTF8') as kw:
            for i in keywords :
                kw.write(i)
                kw.write('\n')
    
    def kw_del():
        selection = listbox.curselection()
        if(len(selection) == 0):
            return

        value = listbox.get(selection[0])
        items.remove(value)
        listbox.delete(selection[0])
        save_kw()
    

    w2 = tk.Tk()
    w2.title('Keywords')
    w2.config(bg='#611')
    w2.geometry('200x220+100+100')
    w2.resizable(False, False)
    
    listbox = tk.Listbox(w2, bg='#333', fg='#EEE')
    listbox.pack()
    
    item_s=list(keywords)
    sorted(item_s)
    for i in item_s:
        listbox.insert(listbox.size(), i)

    bt_del = tk.Button(w2, width=19, text="선택항목 삭제", command=kw_del)
    bt_del.pack()

    entry = tk.Entry(w2, width=15)
    def add(event=None):
        new_kw = entry.get()
        if new_kw != '':
            items.add(new_kw)
            if new_kw not in listbox.get(0,listbox.size()):
                listbox.insert(listbox.size(), new_kw)
            else:
                listbox.SelectedIndex = listbox.get(0,listbox.size()).index(new_kw)
                listbox.index(5)
                listbox.focus()
            entry.delete(0, 'end')
            save_kw()
        
    entry.bind("<Return>", add)
    entry.place(relx=0.1, rely=0.9)
    
    bt_entry = tk.Button(w2, width=8, text="추가", command=add)
    bt_entry.place(relx=0.65, rely=0.9)

    w2.wm_attributes("-topmost",1)
    w2.focus_force()
    print(keywords)
    w2.mainloop()


############################### STRETCH

def stretchFunc():   
    global check_stretch, stretch_option

    w3 = tk.Tk()
    bgc = '#161'
    ftc = '#eee'
    w3.title('stretching')
    w3.config(bg=bgc)
    w3.geometry('200x220+100+100')
    w3.resizable(False, False)
    
    indicator = "10시, 11시.."
    
    lbl = tk.Label(w3, text=indicator, bg=bgc, fg=ftc)
    lbl.pack()
    
    def check1():
        indicator="10시, 11시.."
        lbl.config(text=indicator)
        global check_stretch, stretch_option
        check_stretch.set(True)
        stretch_option=1
        cc()
        
    def check2():
        indicator="11시, 3시, 5시"
        lbl.config(text=indicator)
        global check_stretch, stretch_option
        check_stretch.set(True)
        stretch_option=2
        cc()

    def checkno():
        indicator="몸을 풀어주세요ㅠ"
        lbl.config(text=indicator)
        global check_stretch, stretch_option
        check_stretch.set(False)
        stretch_option=0
        cc()
        
    if(stretch_option<2):
        check1()
    else:
        check2()

    cc()    

    bt_1 = tk.Radiobutton(w3, width=8, text="1시간 주기", value=0, selectcolor='#000',
                          variable=stretch_option, bg=bgc, fg=ftc, command=check1)
    bt_2 = tk.Radiobutton(w3, width=8, text="2시간 주기", value=1, selectcolor='#000',
                          variable=stretch_option, bg=bgc, fg=ftc, command=check2)
    bt_3 = tk.Radiobutton(w3, width=8, text="끄기", value=2, selectcolor='#000',
                          variable=stretch_option, bg=bgc, fg=ftc, command=checkno)


    bt_1.pack()
    bt_2.pack()
    bt_3.pack()
    bt_1.select()
    
    w3.wm_attributes("-topmost",1)
    w3.focus_force()
    
    w3.mainloop()

    

def auto_reply():
    pass

init()
open_window()


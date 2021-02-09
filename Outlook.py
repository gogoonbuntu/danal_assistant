import re, io
import win32com.client as win32
from win32com.client import Dispatch
import inspect
from pythoncom import CoInitialize, CoUninitialize
from win10toast import ToastNotifier


def df(keywords):
    CoInitialize()
    count = 0
    print('키워드 : ',list(keywords))
    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
    # 5 : 내가 보낸 메일
    # 6 : 내가 받은 메일
    inbox = outlook.GetDefaultFolder("6")

    allBox = list(filter(lambda x: x.UnRead==True, inbox.Items))
    # 몇 통의 메일이 있는지 확인
    print ('총 ',len(allBox),' 통의 이메일')

    for msg in allBox:
    # msg.Subject : 메일 제목
    # SenderName : 보낸 사람 이름
    # SenderEmailAddress : 보낸 사람 이메일
        print(msg)
        for a in keywords:
            if a in msg.Subject:
                count+=1
    CoUninitialize()
    print('검색 끝.')
    ts = ToastNotifier()
    ts.show_toast('Hello Danal', '총'+str(count)+'개의 안읽은 키워드 메일', icon_path='image.ico', duration=10, threaded=True)
    return 

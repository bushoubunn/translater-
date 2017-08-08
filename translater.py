import requests
import json
import time
import hashlib
from tkinter import *

def youdao(event=None):
    md=hashlib.md5()
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    content=textSrc.get(1.0,END)
    textDct.delete(1.0,END)
    if '\n'==content[0]:
        content=''
    client='fanyideskweb'
    cstr= "rY0D^0'nM0}g5Mm1z%1G4"
    timestamp=str(int(time.time()*1000))
    md.update((client+content+timestamp+cstr).encode('utf-8'))
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
        +'Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'X-Requested-With':'XMLHttpRequest'}
    data={
        'i':content,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':client,
        'salt':timestamp,
        'sign':md.hexdigest(),
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_ENTER',
        'typoResult':'true'}
    response=requests.post(url,headers=header,data=data).json()
    target=response['translateResult'][0][0]['tgt']
    comment=response['smartResult']['entries']
    textDct.insert(END,str(target)+'\n'.join(comment))
root=Tk()
root.geometry('600x500+300+100')
textSrc=Text(root,width=100,height=10,font=('romam',15,'bold'))
textDct=Text(root,width=100,height=10,font=('romam',15,'bold'))
textDct.insert(END,'please input something:')
#button=Button(root,text='translate',command=youdao)
textSrc.bind('<Return>',youdao)
textSrc.pack()
textDct.pack()
root.mainloop()
              

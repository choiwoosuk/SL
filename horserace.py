# -*- coding: utf-8 –*-
import urllib
import urllib.request
import urllib.parse
import codecs
import json
import webbrowser
from http.client import HTTPConnection
from xml.dom.minidom import *
from xml.etree import ElementTree
from tkinter import*
from tkinter import font

window=Tk()
window.title("경주마 추천기")
canvas=Canvas(window,width=400,height=650)
canvas.pack()

conn = None
server = ""
global horse_data
global inputLabel
global rankSelectBox

class data:
    def __init__(self, hrNm, mhrNm, fhrNm, color, owNm, sex):
        self.hrNm = hrNm
        self.mhrNm = mhrNm
        self.fhrNm = fhrNm
        self.color = color
        self.owNm = owNm
        self.sex = sex
    def __repr__(self):
        return repr((self.hrNm, self.mhrNm, self.fhrNm, self.color, self.owNm, self.sex))



def openAPItoXML(server):
    key = "yPEfTxYymBO7jo1T3JRIU0ogHLDMnloSB0Y6eqRctG3K9m6S99Fa0qjarEIjVhxrakbQ2VUoeLy2911PZO%2F4jQ%3D%3D"
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
    # ↑ User-Agent를 입력하지 않을경우 naver.com 에서 정상적인 접근이 아닌것으로 판단하여 차단을 한다.
    data = ""
    urldata = server + key 
    with opener.open(urldata) as f:
        data = f.read(30000000).decode('utf-8') # 30000000bytes 를 utf-8로 변환하여 읽어온다.  변환이 없을경우 unicode로 받아온다.
    return data

def addParsingDicList(xmlData, motherData, childData):
    # 파싱된 데이터를 리스트에 넣어서 리턴 한다.
    doc = parseString(xmlData)
    siGunGuList = doc.getElementsByTagName(motherData)
    signguCdSize = len(siGunGuList)
    list = []
    for index in range(signguCdSize):
        mphms = siGunGuList[index].getElementsByTagName(childData)
        list.append(str(mphms[0].firstChild.data))
    return list

def mainLogo():
    TempFont = font.Font(window, size=30, family = 'HanS CalliPunch')
    MainText = Label(window,font=TempFont,text="경주마 추천기")
    MainText.pack()
    MainText.place(x=25,y=25)

def raceTest():
    race=Button(window,text="모의경마",height=2,width=12,command=newWindow)
    #race.config(height=100,width=200)
    race.place(x=290,y=145)

def rankSelect():
    global rankSelectBox
    rankSelectBar=Scrollbar(window)
    rankSelectBar.pack()
    rankSelectBar.place(x=190,y=140)

    TempFont = font.Font(window, size=15, family='HY견고딕')
    rankSelectBox=Listbox(window,font=TempFont, activestyle='none',width=10,height=1,borderwidth=10,relief='ridge',yscrollcommand=rankSelectBar.set)
    
    rankSelectBox.insert(1,"혈통")
    rankSelectBox.insert(2,"모마명")
    rankSelectBox.insert(3,"부마명")
    rankSelectBox.pack()
    rankSelectBox.place(x=40,y=145)

    rankSelectBar.config(command=rankSelectBox.yview)

def searchHorse():
    global inputLabel
    TempFont = font.Font(window, size=12, family='맑은 고딕')
    inputLabel=Entry(window,font=TempFont,width=15,borderwidth=5,relief='ridge')
    inputLabel.pack()
    inputLabel.place(x=180,y=610)

def showList():
    global rankSelectBox
    global resultBox
    global horse_data
    global inputLabel
    resultBox.delete(0,END)
    horse_data = sorted(horse_data, key=lambda data: data.hrNm)   
    for data in horse_data:
        if ( rankSelectBox.get(ANCHOR) == "혈통"):
            if ( data.hrNm == inputLabel.get()):
                resultBox.insert(0, data.hrNm + " | " + data.mhrNm + " | " + data.fhrNm)
        elif ( rankSelectBox.get(ANCHOR) == "모마명"):
            if ( data.mhrNm == inputLabel.get()):
                resultBox.insert(0, data.hrNm + " | " + data.mhrNm + " | " + data.fhrNm)
        elif ( rankSelectBox.get(ANCHOR) == "부마명"):
            if ( data.fhrNm == inputLabel.get()):
                resultBox.insert(0, data.hrNm + " | " + data.mhrNm + " | " + data.fhrNm)

def showInfo(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print(value)
    pass

def nameLabel():
    global resultBox
    TempFont = font.Font(window, size=10, family = 'HY견고딕')
    MainText = Label(window,font=TempFont,text="이름")
    MainText.pack()
    MainText.place(x=60,y=220)
    
    MainText = Label(window,font=TempFont,text="모마명")
    MainText.pack()
    MainText.place(x=178,y=220)


    MainText = Label(window,font=TempFont,text="부마명")
    MainText.pack()
    MainText.place(x=313,y=220)

    
    resultBox = Listbox(window,font=TempFont, activestyle='none',width=38,height=22,borderwidth=10,relief='ridge')
    resultBox.bind('<<ListboxSelect>>', showInfo)
    resultBox.pack()
    resultBox.place(x=40,y=240)

def showHorseRank():
    pass

def searchLogo():
    TempFont = font.Font(window, size=15, family = 'HY견고딕')
    MainText = Label(window,font=TempFont,text="말 이름 검색")
    MainText.pack()
    MainText.place(x=25,y=615)

def searchButton():
    TempFont=font.Font(window, size=12, weight='bold', family='맑은 고딕')
    SearchButton=Button(window, font=TempFont,text="검색", command = showList)
    SearchButton.pack()
    SearchButton.place(x=340,y=607)

def mainFrame():
    labelframe=LabelFrame(window,text="랭크",width=350,height=375)
    labelframe.pack()
    labelframe.place(x=30,y=200)

def newWindow():
    global popup
    popup=Toplevel()
    popup.title("모의 경마")
    canvas=Canvas(popup,width=800,height=500)
    canvas.pack()
    canvas.create_line(180, 0, 180, 500)
    canvas.create_line(750, 0, 750, 450)
    canvas.create_line(755, 0, 755, 450)
    canvas.create_line(180, 450, 800, 450)
    startRace()
    insertName()

def startRace():
    race = Button(popup, text="시작", height=2, width=12)
    # race.config(height=100,width=200)
    race.place(x=40, y=450)

def insertName():
    h1=Entry(popup)
    h1.place(x=20,y=40)
    h2 = Entry(popup)
    h2.place(x=20,y=80)
    h3 = Entry(popup)
    h3.place(x=20,y=120)
    h4 = Entry(popup)
    h4.place(x=20,y=160)
    h5 = Entry(popup)
    h5.place(x=20,y=200)
    h6 = Entry(popup)
    h6.place(x=20,y=240)
    h7 = Entry(popup)
    h7.place(x=20,y=280)
    h8 = Entry(popup)
    h8.place(x=20,y=320)
    h9 = Entry(popup)
    h9.place(x=20,y=360)
    h10 = Entry(popup)
    h10.place(x=20,y=400)

mainLogo()

photo=PhotoImage(file="말.GIF")
imageLabel=Label(window,image=photo)
imageLabel.pack()
imageLabel.place(x=275,y=0)

canvas.create_line(0,125,400,125)
canvas.create_line(265,0,265,125)

#----------------------------------------------------------------------------------------------------------------------------------
# 미리 말에 대한 리스트를 만든다.
horse_data = []
# string 변수에 데이터를 파싱해서 가져온다.
dataString = openAPItoXML("http://data.kra.co.kr/publicdata/service/hrReg/getHrReg?meet=1&serviceKey=")
# 각각의 List에 파싱을 해온다.
colorList = []
hrNmList = []
mhrNmList = []
fhrNmList = []
owNmList = []
sexList = []
colorList = addParsingDicList(dataString, "item", "color")
hrNmList = addParsingDicList(dataString, "item", "hrNm")
mhrNmList = addParsingDicList(dataString, "item", "mhrNm")
fhrNmList = addParsingDicList(dataString, "item", "fhrNm")
owNmList = addParsingDicList(dataString, "item", "owNm")
sexList = addParsingDicList(dataString, "item", "sex")
# 파싱해온 List를 미리 정의해둔 data클래스 List horse_data에 추가해준다.
for value in range(0, len(colorList)):
    horse_data.insert(value, data(hrNmList[value],mhrNmList[value], fhrNmList[value], colorList[value],owNmList[value],sexList[value]))
#----------------------------------------------------------------------------------------------------------------------------------
#searchRankList()
raceTest()
rankSelect()
searchLogo()
searchHorse()
searchButton()
mainFrame()

nameLabel()

canvas.create_line(0,600,400,600)
window.mainloop()

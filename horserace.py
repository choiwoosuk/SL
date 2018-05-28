from tkinter import*
from tkinter import font

window=Tk()
window.title("경주마 추천기")
canvas=Canvas(window,width=400,height=600)
canvas.pack()

def mainLogo():
    TempFont = font.Font(window, size=30, family = 'HanS CalliPunch')
    MainText = Label(window,font=TempFont,text="경주마 추천기")
    MainText.pack()
    MainText.place(x=25,y=25)

def raceTest():
    race=Button(window,text="모의경마",height=2,width=12)
    #race.config(height=100,width=200)
    race.place(x=290,y=145)

def rankSelect():
    global rankSelectBox
    rankSelectBar=Scrollbar(window)
    rankSelectBar.pack()
    rankSelectBar.place(x=190,y=140)

    TempFont = font.Font(window, size=15, family='HY견고딕')
    rankSelectBox=Listbox(window,font=TempFont, activestyle='none',width=10,height=1,borderwidth=10,relief='ridge',yscrollcommand=rankSelectBar.set)
    
    rankSelectBox.insert(1,"종합랭킹")
    rankSelectBox.insert(2,"경기성적")
    rankSelectBox.insert(3,"체격")
    rankSelectBox.insert(4,"혈통")
    rankSelectBox.pack()
    rankSelectBox.place(x=40,y=145)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화시설")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

def showHorseRank():
    pass

def searchLogo():
    TempFont = font.Font(window, size=15, family = 'HY견고딕')
    MainText = Label(window,font=TempFont,text="말 랭킹 검색")
    MainText.pack()
    MainText.place(x=25,y=565)

def searchHorse():
    global inputLabel
    TempFont = font.Font(window, size=12, family='맑은 고딕')
    inputLabel=Entry(window,font=TempFont,width=15,borderwidth=5,relief='ridge')
    inputLabel.pack()
    inputLabel.place(x=180,y=560)

def searchButton():
    TempFont=font.Font(window, size=12, weight='bold', family='맑은 고딕')
    SearchButton=Button(window, font=TempFont,text="검색")
    SearchButton.pack()
    SearchButton.place(x=340,y=557)

mainLogo()

photo=PhotoImage(file="말.GIF")
imageLabel=Label(window,image=photo)
imageLabel.pack()
imageLabel.place(x=275,y=0)

canvas.create_line(0,125,400,125)
canvas.create_line(265,0,265,125)

raceTest()
rankSelect()
searchLogo()
searchHorse()
searchButton()
InitSearchListBox()

canvas.create_line(0,550,400,550)
window.mainloop()

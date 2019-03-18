from tkinter import*
from random import choice
from tkinter import filedialog as fd
import tkinter.messagebox
import math


listOfBool = []     #List untuk menyimpan boolean dari setiap elemen , mulainya dari 0(A) sampai 12(K)
chosenCard = []     #List untuk menyimpan kartu yang dipilih, mulainya dari 1(A) sampai 13 (K)
randNum = []        #List untuk menyimpan angka random
listJawaban = []    #List untuk menyimpan jawaban jawaban dalam satu game
listScore = []      #List yang digunakan untuk menyimpan score sebelum export
totalScore = 0.0    #Inisialisasi nilai total score

for i in range (52):
    listOfBool.insert(i, False)

def onImport():#Prosedur untuk memasukan file eksternal
        global chosenCard
        chosenCard.clear()
        card.config(text="")
        pic1.config(image="")
        pic2.config(image="")
        pic3.config(image="")
        pic4.config(image="")
        try:
            tipeFile = fd.askopenfilename(filetypes = (("TEXT files","*.txt"),("All files","*.*")))
            openFile = open(tipeFile,"r")
            a,b,c,d = [int(x) for x in next(openFile).split()]
            cardDataInt = [a,b,c,d]
            chosenCard = cardDataInt.copy()

            tkinter.messagebox.showinfo("Notification!","Import Succeed")
            openFile.close()
            
            if (len(chosenCard)>=1):
                card.config(text="Cards :")
                updatePic(pic1,(chosenCard[0] % 13),math.floor(chosenCard[0]/13)+1)
            if (len(chosenCard)>=2):
                updatePic(pic2,(chosenCard[1] % 13),math.floor(chosenCard[1]/13)+1)
            if (len(chosenCard)>=3):
                updatePic(pic3,(chosenCard[2] % 13),math.floor(chosenCard[2]/13)+1)
            if (len(chosenCard)>=4):
                updatePic(pic4,(chosenCard[3] % 13),math.floor(chosenCard[3]/13)+1)
        except IOError:
            tkinter.messagebox.showwarning("Warning!","Import canceled")
        except:
            tkinter.messagebox.showwarning("Warning!","File doesn't match")

def onExport():#Prosedur untuk melakukan export ke txt
    global totalScore

    try:
        FOutput = open("output.txt","w")
        for i in range (len(listJawaban)):
            FOutput.write(listJawaban[i])
            FOutput.write("   Score : ")
            FOutput.write(listScore[i])
            FOutput.write("\n")
        FOutput.write("\n")
        FOutput.write("Total Score : ")
        FOutput.write(str(totalScore))
        FOutput.write("\n")
        FOutput.close()
        tkinter.messagebox.showinfo("Notification!","Export Succeed")
    except IOError:
        tkinter.messagebox.showwarning("Warning!","Export canceled")
    except:
        tkinter.messagebox.showwarning("Warning!","File doesn't match")

def onExit():#Prosedur untuk melakukan exit
        if tkinter.messagebox.askyesno("Warning!", "Are you sure to exit?"):
            quit()
        else:
            tkinter.messagebox.showinfo("Notification!","Exit canceled")

def randomCard():#Prosedur untuk melakukan random kartu
    finished = True
    for i in range (52):
        if (listOfBool[i]==False):
            finished = False
    if (finished):
        tkinter.messagebox.showwarning("Game has finised!","The game has finished. All cards has already been picked. Please restart the game.")
    else:
        chosenCard.clear()
        randNum.clear()
        for j in range (52):
            if (not(listOfBool[j])):
                randNum.append(j)
        chosenCard.insert(0,choice(randNum)+1)
        randNum.remove(chosenCard[0]-1)
        chosenCard.insert(1,choice(randNum)+1)
        randNum.remove(chosenCard[1]-1)
        chosenCard.insert(2,choice(randNum)+1)
        randNum.remove(chosenCard[2]-1)
        chosenCard.insert(3,choice(randNum)+1)
        randNum.remove(chosenCard[3]-1)
        card.config(text="Cards :")
        updatePic(pic1,(chosenCard[0] % 13),math.floor(chosenCard[0]/13)+1)
        updatePic(pic2,(chosenCard[1] % 13),math.floor(chosenCard[1]/13)+1)
        updatePic(pic3,(chosenCard[2] % 13),math.floor(chosenCard[2]/13)+1)
        updatePic(pic4,(chosenCard[3] % 13),math.floor(chosenCard[3]/13)+1)

def updatePic(pic,column,row):#Prosedur untuk meng-update gambar
    if (column == 1):
        if (row == 1):
            pic.config(image = photodA)
        elif (row == 2):
            pic.config(image = photocA)
        elif (row == 3):
            pic.config(image = photohA)
        else :
            pic.config(image = photosA)
    elif (column == 2):
        if (row == 1):
            pic.config(image = photod2)
        elif (row == 2):
            pic.config(image = photoc2)
        elif (row == 3):
            pic.config(image = photoh2)
        else :
            pic.config(image = photos2)
    elif (column == 3):
        if (row == 1):
            pic.config(image = photod3)
        elif (row == 2):
            pic.config(image = photoc3)
        elif (row == 3):
            pic.config(image = photoh3)
        else :
            pic.config(image = photos3)
    elif (column == 4):
        if (row == 1):
            pic.config(image = photod4)
        elif (row == 2):
            pic.config(image = photoc4)
        elif (row == 3):
            pic.config(image = photoh4)
        else :
            pic.config(image = photos4)
    elif (column == 5):
        if (row == 1):
            pic.config(image = photod5)
        elif (row == 2):
            pic.config(image = photoc5)
        elif (row == 3):
            pic.config(image = photoh5)
        else :
            pic.config(image = photos5)
    elif (column == 6):
        if (row == 1):
            pic.config(image = photod6)
        elif (row == 2):
            pic.config(image = photoc6)
        elif (row == 3):
            pic.config(image = photoh6)
        else :
            pic.config(image = photos6)
    elif (column == 7):
        if (row == 1):
            pic.config(image = photod7)
        elif (row == 2):
            pic.config(image = photoc7)
        elif (row == 3):
            pic.config(image = photoh7)
        else :
            pic.config(image = photos7)
    elif (column == 8):
        if (row == 1):
            pic.config(image = photod8)
        elif (row == 2):
            pic.config(image = photoc8)
        elif (row == 3):
            pic.config(image = photoh8)
        else :
            pic.config(image = photos8)
    elif (column == 9):
        if (row == 1):
            pic.config(image = photod9)
        elif (row == 2):
            pic.config(image = photoc9)
        elif (row == 3):
            pic.config(image = photoh9)
        else :
            pic.config(image = photos9)
    elif (column == 10):
        if (row == 1):
            pic.config(image = photod10)
        elif (row == 2):
            pic.config(image = photoc10)
        elif (row == 3):
            pic.config(image = photoh10)
        else :
            pic.config(image = photos10)
    elif (column == 11):
        if (row == 1):
            pic.config(image = photodJ)
        elif (row == 2):
            pic.config(image = photocJ)
        elif (row == 3):
            pic.config(image = photohJ)
        else :
            pic.config(image = photosJ)
    elif (column == 12):
        if (row == 1):
            pic.config(image = photodQ)
        elif (row == 2):
            pic.config(image = photocQ)
        elif (row == 3):
            pic.config(image = photohQ)
        else :
            pic.config(image = photosQ)
    elif (column == 0):
        if (row == 2):
            pic.config(image = photodK)
        elif (row == 3):
            pic.config(image = photocK)
        elif (row == 4):
            pic.config(image = photohK)
        else :
            pic.config(image = photosK)

def clickButton(angka,lambang):#Prosedur untuk mendefinisikan aksi aksi apa saja yang dilakukan jika suatu button ditekan
    global listOfBool
    global chosenCard
    if len(chosenCard) == 4 and not ((angka+((lambang-1)*13)) in chosenCard):
        tkinter.messagebox.showwarning("Chosen Card Limit","You can only choose 4 cards")
    elif (listOfBool[(angka-1)+((lambang-1)*13)] == True):
        tkinter.messagebox.showwarning("Card has been chosen","You had picked this card")
    elif (angka+((lambang-1)*13)) in chosenCard:
        chosenCard.remove((angka)+((lambang-1)*13))
    else:
        chosenCard.append(angka+((lambang-1)*13))
    if (len(chosenCard)>=1):
        card.config(text="Cards :")
        updatePic(pic1,(chosenCard[0] % 13),math.floor(chosenCard[0]/13)+1)
    if (len(chosenCard)>=2):
        updatePic(pic2,(chosenCard[1] % 13),math.floor(chosenCard[1]/13)+1)
    if (len(chosenCard)>=3):
        updatePic(pic3,(chosenCard[2] % 13),math.floor(chosenCard[2]/13)+1)
    if (len(chosenCard)>=4):
        updatePic(pic4,(chosenCard[3] % 13),math.floor(chosenCard[3]/13)+1)
    if (len(chosenCard)==0):
        card.config(text="")
        pic1.config(image="")
        pic2.config(image="")
        pic3.config(image="")
        pic4.config(image="")
    if (len(chosenCard)==1):
        pic2.config(image="")
        pic3.config(image="")
        pic4.config(image="")
    if (len(chosenCard)==2):
        pic3.config(image="")
        pic4.config(image="")
    if (len(chosenCard)==3):
        pic4.config(image="")

def count(x,y,i):#Prosedur untuk menghitung suatu ekspresi
	if(i == 3):
		return(x+y)
	elif (i == 2):
		return(x-y)
	elif (i == 1):
		return(x*y)
	else:
		return(x/y)	

def convert(i):#Prosedur untuk mengonversi suatu operator menjadi nilai poinnya
	if(i == 0):
		return("/")
	elif(i == 1):
		return("*")
	elif(i == 2):
		return("-")
	else:
		return("+")

def tulis(arrO,arrt,nilai):#Prosedur untuk menuliskan hasil jawaban
	if(arrO[1] < 2 and arrO[0] >1): # operasi berbentuk (a opr1 b) opr2 c opr3 d
		jawaban = "("+str(arrt[3])+convert(arrO[0])+str(arrt[2])+")"+convert(arrO[1])+str(arrt[1])+convert(arrO[2])+str(arrt[0])+" = "+str(nilai)
	elif (arrO[2] < 2 and arrO[1] > 1): # operasi berbentuk (a opr1 b opr2 c) opr3 d
		jawaban = "("+str(arrt[3])+convert(arrO[0])+str(arrt[2])+convert(arrO[1])+str(arrt[1])+")"+convert(arrO[2])+str(arrt[0])+" = "+str(nilai)
	else :
		jawaban = str(arrt[3])+convert(arrO[0])+str(arrt[2])+convert(arrO[1])+str(arrt[1])+convert(arrO[2])+str(arrt[0])+" = "+str(nilai)		
	return jawaban

def total(arrO,nilai,kurung):#Menuliskan score point dari suatu ekspresi dalam bentuk string

	if (kurung):
		total = str(-abs(24-nilai)+sum(arrO)+6-1)
	else :
		total = str(-abs(24-nilai)+sum(arrO)+6)
	return total

def poin(arrO,nilai,kurung):#Menuliskan score point dari suatu ekspresi dalam bentuk integer
	if(kurung):
		return(-abs(24-nilai)+sum(arrO)+6-1)
	else :
		return(-abs(24-nilai)+sum(arrO)+6)

def solveProblem(): #Prosedur untuk mencari solusi terbaik dari 4 kartu yang telah diinput
    global totalScore

    finished = True
    for i in range (52):
        if (listOfBool[i]==False):
            finished = False
    if (finished):
        tkinter.messagebox.showwarning("Game has finised!","The game has finished. All cards has already been picked. Please restart the game.")
    elif (len(chosenCard)<4):
        tkinter.messagebox.showwarning("Pick 4 Cards!","You must pick 4 card or you can press random button below.")
    else:
        arr = []
        for i in range (4):
            arr.append(((chosenCard[i]-1)%13)+1)
        arr.sort()
        arrs = arr.copy()
        arrs.reverse()
        arrt2 = arrs.copy()
        arrt = arr.copy() # menampung isi array original
        operatorSebelum = 0
        arrO = []
        nilai = 0.0
        kurung = False
        for i in range(3):
            point = -100
            for j in range (3,-1,-1):
                kurungTemp = False
                x = count(arr[3-i],arr[2-i],j)
                temp = j-abs(24-x)+2 
                if((j == 0 or j == 1) and (operatorSebelum >1)):
                    temp = temp - 1
                    kurungTemp = True
                if (x == 24 and i == 2):
                    point = temp
                    nilai = x
                    operator = j
                    if(kurungTemp):
                        kurung = True
                        break
                elif((temp)>point):
                    point = temp
                    nilai = x
                    operator = j
                    if(kurungTemp):
                        kurung = True
            operatorSebelum = operator
            arr[2-i] = nilai
            arrO.append(operator)			
        operatorSebelum = 0
        arrO2 = []
        nilai2 = 0.0
        kurung2 = False
        for i in range(3):
            point2 = -100
            for j in range (3,-1,-1):
                kurungTemp = False
                x = count(arrs[3-i],arrs[2-i],j)
                temp = j-abs(24-x)+2 
                if((j == 0 or j == 1) and (operatorSebelum >1)):
                    temp = temp - 1
                    kurungTemp = True
                if (x == 24 and i == 2):
                    point2 = temp
                    nilai2 = x
                    operator = j
                    if(kurungTemp):
                        kurung2 = True
                        break
                elif((temp)>point2):
                    point2 = temp
                    nilai2 = x
                    operator = j
                    if(kurungTemp):
                        kurung2 = True
            operatorSebelum = operator
            arrs[2-i] = nilai2
            arrO2.append(operator)	
        point = poin(arrO,nilai,kurung)
        point2 = poin(arrO2,nilai2,kurung2)		
        if(nilai == 24 and nilai2 == 24):
            if(point > point2):
                jawaban = tulis(arrO,arrt,nilai)
                hasil = total(arrO,nilai,kurung)
            else :
                jawaban = tulis(arrO2,arrt2,nilai2)
                hasil = total(arrO2,nilai2,kurung2)
        elif(nilai == 24):
            jawaban = tulis(arrO,arrt,nilai)
            hasil = total(arrO,nilai,kurung)
        elif(nilai2 == 24):
            jawaban = tulis(arrO2,arrt2,nilai2)
            hasil = total(arrO2,nilai2,kurung2)
        else :
            if(point > point2):
                jawaban = tulis(arrO,arrt,nilai)
                hasil = total(arrO,nilai,kurung)
            else:	
                jawaban = tulis(arrO2,arrt2,nilai2)
                hasil = total(arrO2,nilai2,kurung2)
        listJawaban.append(jawaban)
        listScore.append(hasil)
        hasilSolve.config(text=jawaban)
        scorePoint.config(text=str(float(hasil)))
        totalScore = float(hasil) + totalScore
        totalPoint.config(text = str(totalScore))
        for i in range(4):
            listOfBool[chosenCard[i]-1] = True
        chosenCard.clear()
        updateStatusBool()
        card.config(text="")
        pic1.config(image="")
        pic2.config(image="")
        pic3.config(image="")
        pic4.config(image="")

def updateStatusBool(): #Prosedur untuk mengupdate status dari list of boolean yang menandakan apakah kartu ini sudah dipilih atau belum.
    #Jika kartus sudah dipilih, maka tidak bisa dipilih kembali
    if (listOfBool[0]):
        bdA.config(state = DISABLED)
    else:   
        bdA.config(state = NORMAL)
    
    if (listOfBool[13]):
        bcA.config(state = DISABLED)
    else:
        bcA.config(state = NORMAL)

    if (listOfBool[26]):
        bhA.config(state = DISABLED)
    else:
        bhA.config(state = NORMAL)
    
    if (listOfBool[39]):
        bsA.config(state = DISABLED)
    else:
        bsA.config(state = NORMAL)

    if (listOfBool[1]):
        bd2.config(state = DISABLED)
    else:
        bd2.config(state = NORMAL)

    if (listOfBool[14]):
        bc2.config(state = DISABLED)
    else:
        bc2.config(state = NORMAL)

    if (listOfBool[27]):
        bh2.config(state = DISABLED)
    else:
        bh2.config(state = NORMAL)

    if (listOfBool[40]):
        bs2.config(state = DISABLED)
    else:
        bs2.config(state = NORMAL)

    if (listOfBool[2]):
        bd3.config(state = DISABLED)
    else:
        bd3.config(state = NORMAL)

    if (listOfBool[15]):
        bc3.config(state = DISABLED)
    else:
        bc3.config(state = NORMAL)

    if (listOfBool[28]):
        bh3.config(state = DISABLED)
    else:
        bh3.config(state = NORMAL)

    if (listOfBool[41]):
        bs3.config(state = DISABLED)
    else:
        bs3.config(state = NORMAL)

    if (listOfBool[3]):
        bd4.config(state = DISABLED)
    else:
        bd4.config(state = NORMAL)

    if (listOfBool[16]):
        bc4.config(state = DISABLED)
    else:
        bc4.config(state = NORMAL)

    if (listOfBool[29]):
        bh4.config(state = DISABLED)
    else:
        bh4.config(state = NORMAL)

    if (listOfBool[42]):
        bs4.config(state = DISABLED)
    else:
        bs4.config(state = NORMAL)

    if (listOfBool[4]):
        bd5.config(state = DISABLED)
    else:
        bd5.config(state = NORMAL)

    if (listOfBool[17]):
        bc5.config(state = DISABLED)
    else:
        bc5.config(state = NORMAL)

    if (listOfBool[30]):
        bh5.config(state = DISABLED)
    else:
        bh5.config(state = NORMAL)

    if (listOfBool[43]):
        bs5.config(state = DISABLED)
    else:
        bs5.config(state = NORMAL)

    if (listOfBool[5]):
        bd6.config(state = DISABLED)
    else:
        bd6.config(state = NORMAL)

    if (listOfBool[18]):
        bc6.config(state = DISABLED)
    else:
        bc6.config(state = NORMAL)

    if (listOfBool[31]):
        bh6.config(state = DISABLED)
    else:
        bh6.config(state = NORMAL)

    if (listOfBool[44]):
        bs6.config(state = DISABLED)
    else:
        bs6.config(state = NORMAL)

    if (listOfBool[6]):
        bd7.config(state = DISABLED)
    else:
        bd7.config(state = NORMAL)

    if (listOfBool[19]):
        bc7.config(state = DISABLED)
    else:
        bc7.config(state = NORMAL)

    if (listOfBool[32]):
        bh7.config(state = DISABLED)
    else:
        bh7.config(state = NORMAL)

    if (listOfBool[45]):
        bs7.config(state = DISABLED)
    else:
        bs7.config(state = NORMAL)

    if (listOfBool[7]):
        bd8.config(state = DISABLED)
    else:
        bd8.config(state = NORMAL)

    if (listOfBool[20]):
        bc8.config(state = DISABLED)
    else:
        bc8.config(state = NORMAL)

    if (listOfBool[33]):
        bh8.config(state = DISABLED)
    else:
        bh8.config(state = NORMAL)

    if (listOfBool[46]):
        bs8.config(state = DISABLED)
    else:
        bs8.config(state = NORMAL)

    if (listOfBool[8]):
        bd9.config(state = DISABLED)
    else:
        bd9.config(state = NORMAL)

    if (listOfBool[21]):
        bc9.config(state = DISABLED)
    else:
        bc9.config(state = NORMAL)

    if (listOfBool[34]):
        bh9.config(state = DISABLED)
    else:
        bh9.config(state = NORMAL)

    if (listOfBool[47]):
        bs9.config(state = DISABLED)
    else:
        bs9.config(state = NORMAL)

    if (listOfBool[9]):
        bd10.config(state = DISABLED)
    else:
        bd10.config(state = NORMAL)

    if (listOfBool[22]):
        bc10.config(state = DISABLED)
    else:
        bc10.config(state = NORMAL)

    if (listOfBool[35]):
        bh10.config(state = DISABLED)
    else:
        bh10.config(state = NORMAL)

    if (listOfBool[48]):
        bs10.config(state = DISABLED)
    else:
        bs10.config(state = NORMAL)

    if (listOfBool[10]):
        bdJ.config(state = DISABLED)
    else:
        bdJ.config(state = NORMAL)

    if (listOfBool[23]):
        bcJ.config(state = DISABLED)
    else:
        bcJ.config(state = NORMAL)

    if (listOfBool[36]):
        bhJ.config(state = DISABLED)
    else:
        bhJ.config(state = NORMAL)

    if (listOfBool[49]):
        bsJ.config(state = DISABLED)
    else:
        bsJ.config(state = NORMAL)

    if (listOfBool[11]):
        bdQ.config(state = DISABLED)
    else:
        bdQ.config(state = NORMAL)

    if (listOfBool[24]):
        bcQ.config(state = DISABLED)
    else:
        bcQ.config(state = NORMAL)

    if (listOfBool[37]):
        bhQ.config(state = DISABLED)
    else:
        bhQ.config(state = NORMAL)

    if (listOfBool[50]):
        bsQ.config(state = DISABLED)
    else:
        bsQ.config(state = NORMAL)

    if (listOfBool[12]):
        bdK.config(state = DISABLED)
    else:
        bdK.config(state = NORMAL)

    if (listOfBool[25]):
        bcK.config(state = DISABLED)
    else:
        bcK.config(state = NORMAL)

    if (listOfBool[38]):
        bhK.config(state = DISABLED)
    else:
        bhK.config(state = NORMAL)

    if (listOfBool[51]):
        bsK.config(state = DISABLED)
    else:
        bsK.config(state = NORMAL)

def resetGame():#Prosedur untuk melakukan reset game
    global totalScore

    totalScore = 0
    chosenCard.clear()
    for i in range(52):
        listOfBool[i] = False
    updateStatusBool()
    hasilSolve.config(text="---")
    scorePoint.config(text="0")
    totalPoint.config(text ="0")
    listJawaban.clear()
    listScore.clear()

#Definisi Window Permainan
root = Tk()
root.config(bg = "green")
root.title("24 Solver with Greedy Algorithm")
root.iconbitmap("../resources/ico/honor_heart-14.ico")
root.resizable(False,False)

#Definisi Menu Bar
menu = Menu(root)
root.config(menu = menu)

submenu = Menu(menu)
menu.add_cascade(label ="File", menu = submenu)
submenu.add_command(label = "Import File",command = onImport)
submenu.add_command(label = "Export File",command = onExport)
submenu.add_command(label="Exit",command = onExit)

#Definisi label title
title = Label(root, text="    24 CARD GAME SOLVER", fg ="red",bg="green",font = "Verdana 30 bold")
title.grid(column =3, columnspan=7)

card = Label(root,fg ="white",bg="green",font = "Verdana 20 bold")
card.grid(column = 13, row = 0 )

#Definisi button untuk kartu AS

bdA = Button(root)
photodA = PhotoImage(file="../resources/PNG/AD.png")
bdA.config(image=photodA,width="79",height="120",command=lambda: clickButton(1,1))
bdA.grid(column = 0, row = 1)

bcA = Button(root)
photocA = PhotoImage(file="../resources/PNG/AC.png")
bcA.config(image=photocA,width="79",height="120",command=lambda: clickButton(1,2))
bcA.grid(column = 0, row = 2)

bhA = Button(root)
photohA = PhotoImage(file="../resources/PNG/AH.png")
bhA.config(image=photohA,width="79",height="120",command=lambda: clickButton(1,3))
bhA.grid(column = 0, row = 3)

bsA = Button(root)
photosA = PhotoImage(file="../resources/PNG/AS.png")
bsA.config(image=photosA,width="79",height="120",command=lambda: clickButton(1,4))
bsA.grid(column = 0, row = 4)

#2

bd2 = Button(root)
photod2 = PhotoImage(file="../resources/PNG/2D.png")
bd2.config(image=photod2,width="79",height="120",command=lambda: clickButton(2,1))
bd2.grid(column = 1, row = 1)

bc2 = Button(root)
photoc2 = PhotoImage(file="../resources/PNG/2C.png")
bc2.config(image=photoc2,width="79",height="120",command=lambda: clickButton(2,2))
bc2.grid(column = 1, row = 2)

bh2 = Button(root)
photoh2 = PhotoImage(file="../resources/PNG/2H.png")
bh2.config(image=photoh2,width="79",height="120",command=lambda: clickButton(2,3))
bh2.grid(column = 1, row = 3)

bs2 = Button(root)
photos2 = PhotoImage(file="../resources/PNG/2S.png")
bs2.config(image=photos2,width="79",height="120",command=lambda: clickButton(2,4))
bs2.grid(column = 1, row = 4)

#3

bd3 = Button(root)
photod3 = PhotoImage(file="../resources/PNG/3D.png")
bd3.config(image=photod3,width="79",height="120",command=lambda: clickButton(3,1))
bd3.grid(column = 2, row = 1)

bc3 = Button(root)
photoc3 = PhotoImage(file="../resources/PNG/3C.png")
bc3.config(image=photoc3,width="79",height="120",command=lambda: clickButton(3,2))
bc3.grid(column = 2, row = 2)

bh3 = Button(root)
photoh3 = PhotoImage(file="../resources/PNG/3H.png")
bh3.config(image=photoh3,width="79",height="120",command=lambda: clickButton(3,3))
bh3.grid(column = 2, row = 3)

bs3 = Button(root)
photos3 = PhotoImage(file="../resources/PNG/3S.png")
bs3.config(image=photos3,width="79",height="120",command=lambda: clickButton(3,4))
bs3.grid(column = 2, row = 4)

#4

bd4 = Button(root)
photod4 = PhotoImage(file="../resources/PNG/4D.png")
bd4.config(image=photod4,width="79",height="120",command=lambda: clickButton(4,1))
bd4.grid(column = 3, row = 1)

bc4 = Button(root)
photoc4 = PhotoImage(file="../resources/PNG/4C.png")
bc4.config(image=photoc4,width="79",height="120",command=lambda: clickButton(4,2))
bc4.grid(column = 3, row = 2)

bh4 = Button(root)
photoh4 = PhotoImage(file="../resources/PNG/4H.png")
bh4.config(image=photoh4,width="79",height="120",command=lambda: clickButton(4,3))
bh4.grid(column = 3, row = 3)

bs4 = Button(root)
photos4 = PhotoImage(file="../resources/PNG/4S.png")
bs4.config(image=photos4,width="79",height="120",command=lambda: clickButton(4,4))
bs4.grid(column = 3, row = 4)


#5

bd5 = Button(root)
photod5 = PhotoImage(file="../resources/PNG/5D.png")
bd5.config(image=photod5,width="79",height="120",command=lambda: clickButton(5,1))
bd5.grid(column = 4, row = 1)

bc5 = Button(root)
photoc5 = PhotoImage(file="../resources/PNG/5C.png")
bc5.config(image=photoc5,width="79",height="120",command=lambda: clickButton(5,2))
bc5.grid(column = 4, row = 2)

bh5 = Button(root)
photoh5 = PhotoImage(file="../resources/PNG/5H.png")
bh5.config(image=photoh5,width="79",height="120",command=lambda: clickButton(5,3))
bh5.grid(column = 4, row = 3)

bs5 = Button(root)
photos5 = PhotoImage(file="../resources/PNG/5S.png")
bs5.config(image=photos5,width="79",height="120",command=lambda: clickButton(5,4))
bs5.grid(column = 4, row = 4)

#6

bd6 = Button(root)
photod6 = PhotoImage(file="../resources/PNG/6D.png")
bd6.config(image=photod6,width="79",height="120",command=lambda: clickButton(6,1))
bd6.grid(column = 5, row = 1)

bc6 = Button(root)
photoc6 = PhotoImage(file="../resources/PNG/6C.png")
bc6.config(image=photoc6,width="79",height="120",command=lambda: clickButton(6,2))
bc6.grid(column = 5, row = 2)

bh6 = Button(root)
photoh6 = PhotoImage(file="../resources/PNG/6H.png")
bh6.config(image=photoh6,width="79",height="120",command=lambda: clickButton(6,3))
bh6.grid(column = 5, row = 3)

bs6 = Button(root)
photos6 = PhotoImage(file="../resources/PNG/6S.png")
bs6.config(image=photos6,width="79",height="120",command=lambda: clickButton(6,4))
bs6.grid(column = 5, row = 4)


#7

bd7 = Button(root)
photod7 = PhotoImage(file="../resources/PNG/7D.png")
bd7.config(image=photod7,width="79",height="120",command=lambda: clickButton(7,1))
bd7.grid(column = 6, row = 1)

bc7 = Button(root)
photoc7 = PhotoImage(file="../resources/PNG/7C.png")
bc7.config(image=photoc7,width="79",height="120",command=lambda: clickButton(7,2))
bc7.grid(column = 6, row = 2)

bh7 = Button(root)
photoh7 = PhotoImage(file="../resources/PNG/7H.png")
bh7.config(image=photoh7,width="79",height="120",command=lambda: clickButton(7,3))
bh7.grid(column = 6, row = 3)

bs7 = Button(root)
photos7 = PhotoImage(file="../resources/PNG/7S.png")
bs7.config(image=photos7,width="79",height="120",command=lambda: clickButton(7,4))
bs7.grid(column = 6, row = 4)

#8

bd8 = Button(root)
photod8 = PhotoImage(file="../resources/PNG/8D.png")
bd8.config(image=photod8,width="79",height="120",command=lambda: clickButton(8,1))
bd8.grid(column = 7, row = 1)

bc8 = Button(root)
photoc8 = PhotoImage(file="../resources/PNG/8C.png")
bc8.config(image=photoc8,width="79",height="120",command=lambda: clickButton(8,2))
bc8.grid(column = 7, row = 2)

bh8 = Button(root)
photoh8 = PhotoImage(file="../resources/PNG/8H.png")
bh8.config(image=photoh8,width="79",height="120",command=lambda: clickButton(8,3))
bh8.grid(column = 7, row = 3)

bs8 = Button(root)
photos8 = PhotoImage(file="../resources/PNG/8S.png")
bs8.config(image=photos8,width="79",height="120",command=lambda: clickButton(8,4))
bs8.grid(column = 7, row = 4)

#9

bd9 = Button(root)
photod9 = PhotoImage(file="../resources/PNG/9D.png")
bd9.config(image=photod9,width="79",height="120",command=lambda: clickButton(9,1))
bd9.grid(column = 8, row = 1)

bc9 = Button(root)
photoc9 = PhotoImage(file="../resources/PNG/9C.png")
bc9.config(image=photoc9,width="79",height="120",command=lambda: clickButton(9,2))

bc9.grid(column = 8, row = 2)

bh9 = Button(root)
photoh9 = PhotoImage(file="../resources/PNG/9H.png")
bh9.config(image=photoh9,width="79",height="120",command=lambda: clickButton(9,3))
bh9.grid(column = 8, row = 3)

bs9 = Button(root)
photos9 = PhotoImage(file="../resources/PNG/9S.png")
bs9.config(image=photos9,width="79",height="120",command=lambda: clickButton(9,4))
bs9.grid(column = 8, row = 4)

#10

bd10 = Button(root)
photod10 = PhotoImage(file="../resources/PNG/10D.png")
bd10.config(image=photod10,width="79",height="120",command=lambda: clickButton(10,1))
bd10.grid(column = 9, row = 1)

bc10 = Button(root)
photoc10 = PhotoImage(file="../resources/PNG/10C.png")
bc10.config(image=photoc10,width="79",height="120",command=lambda: clickButton(10,2))
bc10.grid(column = 9, row = 2)

bh10 = Button(root)
photoh10 = PhotoImage(file="../resources/PNG/10H.png")
bh10.config(image=photoh10,width="79",height="120",command=lambda: clickButton(10,3))
bh10.grid(column = 9, row = 3)

bs10 = Button(root)
photos10 = PhotoImage(file="../resources/PNG/10S.png")
bs10.config(image=photos10,width="79",height="120",command=lambda: clickButton(10,4))
bs10.grid(column = 9, row = 4)

#J

bdJ = Button(root)
photodJ = PhotoImage(file="../resources/PNG/JD.png")
bdJ.config(image=photodJ,width="79",height="120",command=lambda: clickButton(11,1))
bdJ.grid(column = 10, row = 1)

bcJ = Button(root)
photocJ = PhotoImage(file="../resources/PNG/JC.png")
bcJ.config(image=photocJ,width="79",height="120",command=lambda: clickButton(11,2))
bcJ.grid(column = 10, row = 2)

bhJ = Button(root)
photohJ = PhotoImage(file="../resources/PNG/JH.png")
bhJ.config(image=photohJ,width="79",height="120",command=lambda: clickButton(11,3))
bhJ.grid(column = 10, row = 3)

bsJ = Button(root)
photosJ = PhotoImage(file="../resources/PNG/JS.png")
bsJ.config(image=photosJ,width="79",height="120",command=lambda: clickButton(11,4))
bsJ.grid(column = 10, row = 4)

#Q

bdQ = Button(root)
photodQ = PhotoImage(file="../resources/PNG/QD.png")
bdQ.config(image=photodQ,width="79",height="120",command=lambda: clickButton(12,1))
bdQ.grid(column = 11, row = 1)

bcQ = Button(root)
photocQ = PhotoImage(file="../resources/PNG/QC.png")
bcQ.config(image=photocQ,width="79",height="120",command=lambda: clickButton(12,2))
bcQ.grid(column = 11, row = 2)

bhQ = Button(root)
photohQ = PhotoImage(file="../resources/PNG/QH.png")
bhQ.config(image=photohQ,width="79",height="120",command=lambda: clickButton(12,3))
bhQ.grid(column = 11, row = 3)

bsQ = Button(root)
photosQ = PhotoImage(file="../resources/PNG/QS.png")
bsQ.config(image=photosQ,width="79",height="120",command=lambda: clickButton(12,4))
bsQ.grid(column = 11, row = 4)

#K

bdK = Button(root)
photodK = PhotoImage(file="../resources/PNG/KD.png")
bdK.config(image=photodK,width="79",height="120",command=lambda: clickButton(13,1))
bdK.grid(column = 12, row = 1)

bcK = Button(root)
photocK = PhotoImage(file="../resources/PNG/KC.png")
bcK.config(image=photocK,width="79",height="120",command=lambda: clickButton(13,2))
bcK.grid(column = 12, row = 2)

bhK = Button(root)
photohK = PhotoImage(file="../resources/PNG/KH.png")
bhK.config(image=photohK,width="79",height="120",command=lambda: clickButton(13,3))
bhK.grid(column = 12, row = 3)

bsK = Button(root)
photosK = PhotoImage(file="../resources/PNG/KS.png")
bsK.config(image=photosK,width="79",height="120",command=lambda: clickButton(13,4))
bsK.grid(column = 12, row = 4)

#ChosenCard

pic1 = Label(root,bg = "green")
pic2 = Label(root,bg = "green")
pic3 = Label(root,bg = "green")
pic4 = Label(root,bg = "green")
pic1.grid(column = 13, row = 1)
pic2.grid(column = 13, row = 2)
pic3.grid(column = 13, row = 3)
pic4.grid(column = 13, row = 4)

#Button Solve, Random, dan Reset
solveButton = Button(root)
photoSolve = PhotoImage(file="../resources/solveButton.png")
solveButton.config(image = photoSolve, width = "158", height = "70",command=solveProblem)
solveButton.grid(column = 0, row = 5, columnspan = 2,rowspan = 2)

randButton = Button(root)
photoRand = PhotoImage(file="../resources/diceButton.png")
randButton.config(image = photoRand, width = "79", height = "70",command=randomCard)
randButton.grid(column = 2, row = 5,rowspan = 2)

resetButton = Button(root)
photoReset = PhotoImage(file="../resources/resetButton.png")
resetButton.config(image = photoReset, width = "79", height="70",command=resetGame)
resetButton.grid(column = 12, row = 5, rowspan = 2)


#Label Hasil
textHasil = Label(root,text = "Result :", bg = "green", fg = "white",font = "Verdana 13 bold")
textHasil.grid(column=3, row= 5,rowspan = 2)


hasilSolve = Label(root,text = "---", bg = "green", fg = "white",font = "Verdana 20 bold")
hasilSolve.grid(column =4, row = 5, columnspan = 6,rowspan = 2)

#Label Score dan Total Score
score = Label(root,text = "Score :", bg = "green", fg = "white",font = "Verdana 13 bold")
score.grid(column = 10, row = 5)
totalP = Label(root,text = "Total :", bg = "green", fg = "white",font = "Verdana 13 bold")
totalP.grid(column = 10, row = 6)

scorePoint = Label(root,text = "0", bg = "green", fg = "white",font = "Verdana 13 bold")
scorePoint.grid(column = 11, row = 5)
totalPoint = Label(root,text = "0", bg = "green", fg = "white",font = "Verdana 13 bold")
totalPoint.grid(column = 11, row = 6)

root.mainloop()

import sys
import math

#Program ini bisa dipanggil dan menampilkan hasil hanya dengan menuliskan py main2.py <namaFileInput.txt> <namaFileOutput.txt> pada command prompt

def count(x,y,i):#Prosedur untuk menghitung suatu ekspresi
	if(i == 3):
		return(x+y)
	elif (i == 2):
		return(x-y)
	elif (i == 1):
		return(x*y)
	else:
		return(x/y)	

def convert(i):#Prosedur untuk mengonversi suatu operator menjadi nilainya
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
        FInput = open(sys.argv[1],"r")
        a,b,c,d = [int(x) for x in next(FInput).split()]
        arr = [a,b,c,d]
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
        FOutput = open(sys.argv[2],"w")
        FOutput.write(jawaban)
        FOutput.write("\nScore : ")
        FOutput.write(hasil)
        FOutput.write("\n")
        FInput.close()
        FOutput.close()

def main():
    solveProblem()

if __name__ == '__main__':
	main()

import math
plik = open('figura.txt', "w+")
def caleczka(x, dokladnosc):
    pole = 0
    n = dokladnosc
    i = round(x/n)
    for j in range(i):
        pole += ((1 + ((j*n)**2)/100 - (j*n)/200) - (-((j*n)**2)/50))*n
    return round(pole, 3)

print("pole: ", caleczka(10,0.0001))

def szukaj():
    def gora(j):
        up = (1 + (j ** 2) / 100 - (j) / 200)
        return up
    def dol(j):
        down = abs(-((j)**2)/50)
        return down
    for i in range(30000):
        x = math.ceil(i/1000)
        temp = gora(i/1000)+dol(i/1000)
        ceil_gora = math.floor(gora(i/1000))
        ceil_dol = math.floor(dol(i/1000))
        #print(ceil_gora, ceil_dol, temp, x)
        if temp>=26 and ceil_gora+ceil_dol == 26:
            print("wartosc C: ", x+100)
            plik.write("wartosc C: "+str(x+100)+'\n')

            print("gorny-lewy-rog: ",x,str(ceil_gora))
            plik.write("gorny-lewy-rog: " + str(x)+" "+ str(ceil_gora) + '\n')

            print("dolny-lewy-rog: ",x,str(ceil_dol))
            plik.write("dolny-lewy-rog: " + str(x) + " " + str(ceil_dol) + '\n')

            print("gorny-prawy-rog: ",x+100,str(ceil_gora+100))
            plik.write("gorny-prawy-rog: " + str(x+100) + " " + str(ceil_gora) + '\n')

            print("dolny-prawy-rog: ",x+100,str(ceil_dol))
            plik.write("dolny-prawy-rog: " + str(x+100) + " " + str(ceil_dol) + '\n')
            return 0




szukaj()
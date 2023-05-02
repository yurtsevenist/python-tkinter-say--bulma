import random
import os
from time import sleep
print("Sayı Bulma Oyunu Version:1.0")
cevap="e"
oyun=0
toplampuan=0
print("*****************************")
while cevap.upper()=="E":
    oyunpuan=100
    oyun+=1
    tut=random.randint(0,100)
    tahmin=-1
    sayac=0
    print("{0}. OYUN: 0-100 Arasında bir sayı tuttum, bil bakalım" .format(oyun))
    while tahmin!=tut:
        try:
            tahmin=int(input("Tahmin ettiğiniz sayıyı giriniz..:"))
            sayac+=1 
            if(tahmin>tut):
                print("Daha Küçük bir sayı giriniz !")
                oyunpuan-=10
                if(oyunpuan<=0):
                    print("Bu oyunda {0} kez tahminde bulundunuz ve tahmin hakkınız kalmadı".format(sayac))
                    break
            elif(tahmin<tut):
                print("Daha Büyük bir sayı giriniz !")
                oyunpuan-=10
                if(oyunpuan<=0):
                    print("Bu oyunda {0} kez tahminde bulundunuz ve tahmin hakkınız kalmadı".format(sayac))
                    break
            else:
                print("Tebrikler {0} kez tahminde bulunudunuz ve dogru sayıyı buldunuz" .format(sayac))
                print("Oyun Puanınız : {0}" .format(oyunpuan))
                toplampuan+=oyunpuan
                print("Toplam Puanınız :{0}" .format(toplampuan))
        except:
            print("Hatalı veri girişi..")    
    sleep(1)
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
       os.system('ls')
    cevap=input("Tekrar Oynamak istermisiniz ? (E/H)")    
    

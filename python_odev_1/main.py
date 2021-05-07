#1 - Kullanıcıdan alacağınız bir sayının çift sayı olup olmadığını kontrol edip ekrana sayı çiftse çift, çift değilse tek yazdırın.
while True:
    sayi = int(input("sayi giriniz:"))
    if sayi<0:
      print("negatif sayinin asallik kontrolu yoktur donguden ciktiniz!")
      break
    elif sayi%2==0:
     print("girilen {} sayisi asaldir".format(sayi))
    elif sayi%2!=0:
     print("girilen {} sayisi asal degildir".format(sayi))
#2 - Kullanıcıdan alacağınız 5 tane sayının asal olup olmadığını kontrol edip, her bir sayı için ekrana sayı asalsa asal, asal değilse asal değil yazdırın.
sayilar = []
for sayi in range(5):
    deger = int(input("sayi giriniz:"))
    sayilar.append(deger)
kntrl=0
for i in range(5):
    if sayilar[i]<2:
        print(i + 1, ". sayı(", sayilar[i], ") asal değildir.")
        continue
    for j in range(2,sayilar[i]):
        if sayilar[i] % j == 0:
             print(i+1, ". sayı(", sayilar[i], ") asal değildir.")
             kntrl=1
             break
    if kntrl==0:
        print(i + 1, ". sayı(", sayilar[i], ") asaldır.")
        kntrl=0
#Elimizdeki üç adet string içerisindeki rakamlar temizlenip (sadece harfler kalacak) temiz
#halleri bir listede tutulacaktır. Temiz halde listede bulunan isimlerin hepsi yan yana bir
#string değişkeninde birleştirilecek ve aralarında (-) işareti olacaktır.
def TemizVeri(s1, s2, s3):
    temizVeri = ""
    for i in range(len(s1)):
        if not s1[i].isdigit():
            temizVeri += s1[i]
    temizVeri += "-"

    for i in range(len(s2)):
        if not s2[i].isdigit():
            temizVeri += s2[i]
    temizVeri += "-"

    for i in range(len(s3)):
        if not s3[i].isdigit():
            temizVeri += s3[i]

    return temizVeri

print("\n", TemizVeri("Ah5me4t", "M9eHm4eT", "Ha3K5a1n"))







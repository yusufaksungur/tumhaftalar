import sys


def uret(str):

    dizi = []
    sayac=0
    for i in str:
        if sayac>1:
            k= str[sayac].split('=')
            dizi.append(k[1])
        else:
            pass
        sayac+=1
    return dizi[0],dizi[1]


ali=sys.argv
x,y=uret(ali)
print(x,y)
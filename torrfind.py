#! /usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
import datetime
import time
from bs4 import BeautifulSoup
import webbrowser
import urllib.request
from darkhold import convert
resp = "y"
while resp == "y":
    lf0 = input("Buscar: ")
    lf1 = lf0.split(' ')
    if len(lf1) > 1:
        a = 0
        lf2 = convert(lf1,"+")
        lf3 = convert(lf1,' ')
        string0 = "https://1337x.to/search/%s/1/" % (lf2,)
        string1 = "https://thepiratebay.org/search/%s/0/99/0" % (lf3,)
    else:
        string0 = "https://1337x.to/search/%s/1/" % (lf1,)
        string1 = "https://thepiratebay.org/search/%s/0/99/0" % (lf1,)
    hist = open("history.txt", "a+")
    hist.write("\n" + lf0 + " " + str(datetime.datetime.now(tz=None)))
    hist.close()
    print("Historial guardado. Podes acceder al mismo en el directorio del programa.\n")

    opener1 = urllib.request.build_opener()
    opener1.addheaders = [('User-agent', 'Mozilla/5.0')]
    response1 = opener1.open(string0)

    opener2 = urllib.request.build_opener()
    opener2.addheaders = [('User-agent', 'Mozilla/5.0')]
    response2 = opener2.open(string1)

    pag1 = response1.read()
    pag2 = response2.read()

    soup1 = BeautifulSoup(pag1, 'html.parser')
    pTitle1 = soup1.find_all("a")
    target1 = pTitle1[31]
    targetString1 = pTitle1[31].string
    targetLink1 = pTitle1[31].get('href')

    soup2 = BeautifulSoup(pag2, 'html.parser')
    pTitle2 = soup2.find_all("a")
    target2 = pTitle2[19]
    targetString2 = pTitle2[19].string
    targetLink2 = pTitle2[19].get('href')

    print("")
    print("1)" + pTitle1[31].string)
    print("")
    print("2)" + pTitle2[19].string)
    print("")
    check = input("¿Acceder a 1 o 2? ")

    if check == "1": # Levanta 1337x
        link1 = "https://1337x.to" + targetLink1
        print(link1)
        webbrowser.get().open(link1)

    elif check == "2": # Levanta TPB
        link2 = "https://thepiratebay.org" + targetLink2
        print(link2)
        webbrowser.get().open(link2)

    else:
        print("Bye!")
        exit()

    print("Abriendo navegador...")
    time.sleep(1)

    resp = input("Para realizar otra busqueda presione 'y' de lo contrario cualquier tecla: ")

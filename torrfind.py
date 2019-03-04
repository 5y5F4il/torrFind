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
    print("")
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
    targetString1 = target1.string
    targetLink1 = target1.get('href')

    soup2 = BeautifulSoup(pag2, 'html.parser')
    pTitle2 = soup2.find_all("a")
    target2 = pTitle2[19]
    targetString2 = target2.string
    targetLink2 = target2.get('href')

    print("")
    print("1)" + targetString1)
    print("")
    print("2)" + targetString2)
    print("")
    check = input("¿Acceder a 1 o 2? ")
    print("")

    if check == "1": # Levanta 1337x
        link1 = "https://1337x.to" + targetLink1
        print(link1)
        print("Abriendo magnet en navegador...")
        print("")
        time.sleep(1)
        opener3 = urllib.request.build_opener()
        opener3.addheaders = [('User-agent', 'Mozilla/5.0')]
        response3 = opener3.open(link1)
        pag3 = response3.read()
        soup3 = BeautifulSoup(pag3, 'html.parser')
        pTitle3 = soup3.find_all('a')
        targetLink3 = pTitle3[32].get('href')
        webbrowser.get().open(targetLink3)

    elif check == "2": # Levanta TPB
        link2 = "https://thepiratebay.org" + targetLink2
        print(link2)
        print("")
        print("Abriendo magnet en navegador...")
        print("")
        time.sleep(1)
        opener4 = urllib.request.build_opener()
        opener4.addheaders = [('User-agent', 'Mozilla/5.0')]
        response4 = opener4.open(link2)
        pag4 = response4.read()
        soup4 = BeautifulSoup(pag4, 'html.parser')
        pTitle4 = soup4.find_all('a')
        targetLink4 = pTitle4[10].get('href')
        webbrowser.get().open(targetLink4)

    else:
        print("Bye!")
        exit()

        print("")
        resp = input("Para realizar otra busqueda presione 'y' de lo contrario cualquier tecla: ")

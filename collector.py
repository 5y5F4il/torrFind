from bs4 import BeautifulSoup
import webbrowser
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open("https://1337x.to/search/mr+robot/1/")
pag1 = response.read()

soup1 = BeautifulSoup(pag1, 'html.parser')
pTitle1 = soup1.find_all("a")
target1 = pTitle1[31]
targetString1 = pTitle1[31].string
targetLink1 = pTitle1[31].get('href')

pag2 = open("pagina_2.txt", 'r')

soup2 = BeautifulSoup(pag2, 'html.parser')
pTitle2 = soup2.find_all("a")
target2 = pTitle2[19]
targetString2 = pTitle2[19].string
targetLink2 = pTitle2[19].get('href')
print(pTitle2[19].string)

# -----------------------------------------

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
    link2 = "https://1337x.to" + targetLink2
    print(link2)
    webbrowser.get().open(targetLink2)

else:
    print("Bye!")
    exit()

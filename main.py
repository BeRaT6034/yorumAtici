import keyboard
import time
#33 defa tab tuşuna basarak yorum ekle butonuna gidiyor
#6 defa tab tuşuna basarak 5. yıldızı seçiyor
#1 tane tab ile yorum kısmına geliyor
#2 tane tab ile de yayınla butonuna basıyor
linkler = []
tekrar = int(input("Lutfen kaç link olduğunu yazın..:"))
for i in range(tekrar):
    link = input("Link URL' sini girin..:")    
    linkler.append(link)


def openChrome():
    keyboard.press("win+r")
    time.sleep(1)
    keyboard.write("chrome.exe")
    time.sleep(0.5)
    keyboard.release("r")
    keyboard.release("win")
    time.sleep(1)
    keyboard.press("enter")


def openPage(link):
    keyboard.write(link)
    time.sleep(0.5)
    keyboard.press("enter")
    time.sleep(0.5)



def writeComment():    
    time.sleep(3)
    
    for i in range (28):
        time.sleep(0.05)
        keyboard.press("tab")
        keyboard.release("tab")
    time.sleep(0.5)
    keyboard.press("enter")
    time.sleep(0.5)

    for i in range (6):
        time.sleep(0.5)
        keyboard.press("tab")
        keyboard.release("tab")

    keyboard.press("enter")
    time.sleep(0.5)
    keyboard.press("tab")
    keyboard.write("aposjdoağosdfjğoasfmnasmnfoasnfmoiğlaslnfaolsnfpşaısnfpaısınfşanşpşsf")
    time.sleep(0.5)
    keyboard.release("enter")
    keyboard.release("tab")

    for i in range(2):
        keyboard.press("tab")
        time.sleep(0.05)
        keyboard.release("tab")
    keyboard.press("enter")
    time.sleep(0.05)
    keyboard.release("enter")

for j in range(tekrar):
    time.sleep(3)
    openChrome()

    time.sleep(3)
    openPage(linkler[j])
    time.sleep(3)
    writeComment()
    time.sleep(3)

    time.sleep(0.5)
    keyboard.press("alt+f4")
    time.sleep(0.5)
    keyboard.release("alt")
    keyboard.release("f4")


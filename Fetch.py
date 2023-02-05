import requests
import os
from PIL import Image as img

def Image(img_width, img_height):
    try: 
        global imgUrl
        global expl
        global date
        global title
        os.makedirs('marsImages',exist_ok=True)
        path = os.path.join(os.getcwd(),'marsImages')

        api_key = 'MyG8gwSTFPwax20aBofVEvR1mP2hwCgW8l60RM0C'
        res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}").json()
        print(res)
        url = res['url']
        expl = res['explanation']
        date = res['date']
        title = res['title']
        imgUrl = url
        print()
        print(f'Downloading Image from: \n{url}')
        print()

        length = len(os.listdir(path))
        num = length + 1
        imgRes = requests.get(url)

        marsImg = open(os.path.join(path,os.path.basename(url)), 'wb')

        for chunk in imgRes.iter_content(100000):
            
            marsImg.write(chunk)
        marsImg.close()

        resizeImg = img.open(os.path.join(path,os.path.basename(url)))
        resizeImg.resize((int(img_width),int(img_height)))
        resizeImg.save(os.path.join(path,os.path.basename(url)))

        print('Image Download Succesful!')
        print()
    except KeyError:
        print("----------------------")
        print(res)
    return 0

def Name():
    return os.path.basename(imgUrl)

def Description():
    return expl

def Date():
    return date

def Title():
    return title

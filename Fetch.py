import requests
import os
from PIL import Image as img

photos = []

def Image(nameRover='curiosity', solYear='1000', cameraName='fhaz', earthDate='2015-6-3', img_width=350, img_height=350):

    try: 
        global imgUrl
        global sol
        global date
        global roverName
        global numPhotos
        os.makedirs('marsImages',exist_ok=True)
        path = os.path.join(os.getcwd(),'marsImages')

        api_key = 'MyG8gwSTFPwax20aBofVEvR1mP2hwCgW8l60RM0C'
        res = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{nameRover}/photos?sol={solYear}&camera={cameraName}&earth_date={earthDate}&api_key={api_key}").json()

        numPhotos = len(res['photos'])
        print("Number Of Photos: ", numPhotos)
        for i in range(numPhotos):

            url = res['photos'][i]['img_src']
            imgUrl = url
            sol = res['photos'][i]['sol']
            date = res['photos'][i]['earth_date']
            roverName = res['photos'][i]['rover']['name']

            print()
            print(f'Downloading Image from: \n{url}')
            print()
            imgRes = requests.get(url)

            marsImg = open(os.path.join(path,os.path.basename(url)), 'wb')

            for chunk in imgRes.iter_content(100000):
                marsImg.write(chunk)
            marsImg.close()

            imgPath = os.path.join(path,os.path.basename(url))
            resizeImg = img.open(imgPath)
            resizeImg.thumbnail((img_width,img_height))
            resizeImg.save(os.path.join(path,os.path.basename(url)))
            photos.append(os.path.join(path,os.path.basename(url)))
            print('Image Download Succesful!')
            print()
    except KeyError:
        print("----------------------")
        print(res['photos'])
    return 0

def numPhotos():
    return numPhotos


def Name():
    return photos

def Sol():
    return sol

def Date():
    return date

def roverName():
    return roverName

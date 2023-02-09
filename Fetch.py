import requests
import os
from PIL import Image as img

photos = []

def Image(nameRover='curiosity', solYear='1000', cameraName='fhaz', earthDate='2015-6-3', img_width=500, img_height=500):

    try: 
        global imgUrl
        global sol
        global date
        global roverName
        global numPhotos
        os.makedirs('marsImages',exist_ok=True)
        path = os.path.join(os.getcwd(),'marsImages')

        # stRE2d9R0wIxVfFzV05MUjqJ1m3k3AJ2pOw6nx1W
        # MyG8gwSTFPwax20aBofVEvR1mP2hwCgW8l60RM0C
        # 07OpzC4a1zoNdt0PDDPnoDJOJbA6EETPbAbl8WsZ

        api_key = '07OpzC4a1zoNdt0PDDPnoDJOJbA6EETPbAbl8WsZ'
        
        res = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{nameRover}/photos?sol={solYear}&camera={cameraName}&?earth_date={earthDate}&api_key={api_key}").json()
        # print(res)
        numPhotos = len(res['photos'])
        print()
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
        print(res)

    except KeyboardInterrupt:
        print("Fetch Terminated...")
        pass

    return 0

def numbPhotos():
    return numPhotos


def Name():
    return photos

def Sol():
    return int(sol)

# def Date():
#     print(date)

# def roverName():
#     print(roverName)

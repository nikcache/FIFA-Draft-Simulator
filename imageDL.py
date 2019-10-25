#image downloader

#importing modules
import requests
from PIL import Image as PImage

def faceDL(url, idNum):

    try:
        img_data = requests.get(url).content
        with open("pics/players/" + str(idNum) + ".png", 'wb') as handler:
            handler.write(img_data)

        img = PImage.open("pics/players/" + str(idNum) + ".png")
        new_img = img.resize((150,150))
        new_img.save("pics/players/" + str(idNum) + ".png", "PNG", optimize=True)
    except:
        return -1

def flagDL(url, nation):

    try:
        img_data = requests.get(url).content
        with open("pics/flags/" + nation + ".png", 'wb') as handler:
            handler.write(img_data)

        img = PImage.open("pics/flags/" + nation + ".png")
        new_img = img.resize((46,34))
        new_img.save("pics/flags/" + nation + ".png", "PNG", optimize=True)
    except:
        return -1

def clubDL(url, club):

    try:
        img_data = requests.get(url).content
        with open("pics/clubs/" + club + ".png", 'wb') as handler:
            handler.write(img_data)

        img = PImage.open("pics/clubs/" + club + ".png")
        new_img = img.resize((36,36))
        new_img.save("pics/clubs/" + club + ".png", "PNG", optimize=True)
        
    except:
        return -1

from PIL import Image
filn= "postcard.jpg"
with Image.open(filn) as img:
    img.load()
cropp_img= img.crop((110, 210, 640, 470))
cropp_img.save("crop.postc.jpg")
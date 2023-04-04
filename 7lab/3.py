from PIL import Image, ImageFilter

filename=["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
for file in filename:
    with Image.open(file) as img:
        img.load()
        new_img=img.filter(ImageFilter.CONTOUR)
        new_img.save("new_" + file)

from PIL import Image

filename="1.jpg"
with Image.open(filename) as img:
    img.load()

img.show()
widht, height = img.size

format=img.format

mode=img.mode

print("Ширина: ", widht)
print("Высота: ", height)
print("Формат: ", format)
print("Цветовая модель: ", mode)




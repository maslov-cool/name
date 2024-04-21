from PIL import Image, ImageDraw


# создаём изображение
name = Image.new('RGB', (1000, 400), (0, 0, 0))

# ставим фон для каждый буквы
draw = ImageDraw.Draw(name)
draw.rectangle((0, 0, 250, 400), (255, 0, 0))
draw.rectangle((251, 0, 500, 400), (0, 255, 0))
draw.rectangle((501, 0, 750, 400), (0, 191, 255))
draw.rectangle((751, 0, 1000, 400), (255, 255, 128))

# 1 буква
draw.arc((0, 0, 500, 400), start=90, end=270, fill=(128, 64, 48), width=75)

# 2 буква
draw.polygon(((291, 400), (354, 200), (398, 200), (461, 400), (500, 400), (376, 0), (251, 400)), (128, 64, 48))
draw.polygon(((394, 160), (358, 160), (376, 70)), (0, 255, 0))

# 3 буква
draw.polygon(((501, 0), (501, 400), (750, 400), (750, 0),
              (710, 0), (710, 360), (646, 360), (646, 0), (606, 0), (606, 360), (541, 360), (541, 0)), (128, 64, 48))

# 4 буква
draw.polygon(((791, 400), (854, 200), (898, 200), (961, 400), (1000, 400), (876, 0), (751, 400)), (128, 64, 48))
draw.polygon(((894, 160), (858, 160), (876, 70)), (255, 255, 128))


name.save('name.png')


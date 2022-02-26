from PIL import Image, ImageDraw, ImageFont

# create an image
out = Image.new("L", (150, 100), 255)

# get a font
# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10, 10), "Hello\nWorld", fill=0)

out.show()
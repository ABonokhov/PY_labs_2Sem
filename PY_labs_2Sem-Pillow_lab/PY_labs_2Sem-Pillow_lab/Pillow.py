from PIL import Image, ImageDraw, ImageFont
import sys
from PIL import ImageOps
import qrcode

try:
    bon = Image.open("tree1.jpg")
except:
    print("Unable to load image")
    sys.exit(1)

def get_date_taken(bon):
    return bon.getexif()[306]
print (get_date_taken(bon))

idraw = ImageDraw.Draw(bon)
text = "Artemiy Bonokhov " + get_date_taken(bon)
font = ImageFont.truetype("arial.ttf", size=126)
idraw.text((1000, 2800), text, fill='pink', font=font)
bon.save('tree1_watermarked.jpg')


def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.save(output_image_path)


if __name__ == '__main__':
    img = 'tree1_watermarked.jpg'
    watermark_photo(img, 'logo_tree1.jpg',
                         'logo1.jpg', position=(3500, 0))

img_bg = Image.open('logo_tree1.jpg')
qr = qrcode.QRCode(box_size=14, border=2)
qr.add_data('https://vk.com/therealbons')
qr.make()
img_qr = qr.make_image()
#pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
img_bg.paste(img_qr)
img_bg.save('qr_tree1.jpg')
image = Image.open('qr_tree1.jpg')

image.show()







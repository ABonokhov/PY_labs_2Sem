from PIL import Image, ImageDraw, ImageFont
import sys
from PIL import ImageOps
import qrcode
import os


for k in os.listdir('photos'):
   if k.endswith('.jpg'):
        i = Image.open(os.path.join('photos', k))
        kn, kext = os.path.splitext(k)
        print(kn)                 # выводит  названия всех изображений в папке


try:
    bon = Image.open("photos/tree1.jpg")
    bon2 = Image.open("photos/sky.jpg")
except:
    print("Unable to load image")
    sys.exit(1)

def get_date_taken(bon):
    return bon.getexif()[306]
#print (get_date_taken(bon))

idraw = ImageDraw.Draw(bon)
text = "Artemiy Bonokhov " + get_date_taken(bon)
font = ImageFont.truetype("arial.ttf", size=126)
idraw.text((1000, 2800), text, fill='pink', font=font)
bon.save('photos/tree1_watermarked.jpg')


def get_date_taken(bon2):
    return bon2.getexif()[306]
#print (get_date_taken(bon2))
idraw = ImageDraw.Draw(bon2)
text = "Artemiy Bonokhov " + get_date_taken(bon2)
font = ImageFont.truetype("arial.ttf", size=126)
idraw.text((1000, 2800), text, fill='purple', font=font)
bon2.save('photos/sky_watermarked.jpg')


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
    img = 'photos/tree1_watermarked.jpg'
    watermark_photo(img, 'photos/logo_tree1.jpg',
                          'photos/logo1.jpg', position=(3500, 0)),

    img2 = 'photos/sky_watermarked.jpg'
    watermark_photo(img2, 'photos/logo_sky.jpg',
                          'photos/logo1.jpg', position=(3500, 0))



img_bg = Image.open('photos/logo_tree1.jpg')
img2_bg = Image.open('photos/logo_sky.jpg')
qr = qrcode.QRCode(box_size=14, border=2)
qr.add_data('https://vk.com/therealbons')
qr.make()
img_qr = qr.make_image()
img2_qr = qr.make_image()
#pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
img_bg.paste(img_qr)
img2_bg.paste(img2_qr)
img_bg.save('photos/qr_tree1.jpg')
image = Image.open('photos/qr_tree1.jpg')
img2_bg.save('photos/qr_logo_sky.jpg')
image2 = Image.open('photos/qr_logo_sky.jpg')

image.show()
image2.show()








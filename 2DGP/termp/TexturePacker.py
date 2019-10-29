#needed install pillow
from PIL import Image
#import matplotlib.pyplot as plt
import os;


class TexturePacker:
    pass;


def crop(file_path:str, height:int, width:int):
    im = Image.open(file_path);
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

def resize_multiple(img:Image, multiple:int, save_name:str, in_quality = 100):
    resize_image = img.resize((img.width * multiple, img.height * multiple));
    #print("이미지 resize 한 후 : {0}x{1} - {2} ".format(width, height, test_img));
    resize_image.save(save_name, quality=in_quality);



if __name__=='__main__':
    #print("test");
    #tt = Image.open('assets/tiles.png');
    #print("test");
    #tt.show();
    #height = 90;
    #width = 90;
    #for k, piece in enumerate(crop('assets/tiles.png', height, width), 0):
    #    print("frist");        
    #    img=Image.new('RGBA', (height,width), 255)
    #    img.paste(piece)
    #    path = os.path.join('',"IMG-%s.png" % k);
    #    img.save(path)
    #    print("done");

    img = Image.open('logo (2).png');
    resize_multiple(img, 5, "logo.png");

    #crop(img,90, 90 );

#needed install pillow
from PIL import Image
#import matplotlib.pyplot as plt
import os;


def crop_wrapper(file_path:str, width:int,height:int, save_path:str):
    for k, piece in enumerate(crop(file_path, height, width), 0):
        img=Image.new('RGBA', (width, height), 255)
        img.paste(piece);
        path = os.path.join(save_path,"IMG-%s.png" % k);
        img.save(path);

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


def bmp_to_png(file_path:str, width:int,height:int, save_path:str, file_type:str):
    from PIL import Image;
    img = Image.open(file_path);
    new_img = img.resize( (img.width, img.height) );
    new_img.save( save_path, file_type);


if __name__=='__main__':
    #print("test");
    #tt = Image.open('assets/tiles.png');
    #print("test");
    #tt.show();

    height = 224 // 8;
    width = 28;
    for k, piece in enumerate(crop('D:\\_git\\2dgp\\2DGP\\assets\\Monster\\Coin\\coin.png', height, width), 0):
        print("frist");        
        img=Image.new('RGBA', (width, height), 255)
        img.paste(piece)
        path = os.path.join('',"IMG-%s.png" % k);
        img.save(path)
        print("done");

    #img = Image.open('D:\\_git\\2dgp\\2DGP\\assets\\Monster\\Coin\\coin(56x7)8x1.png');
    #resize_multiple(img, 4, "coin.png");

    #crop(img,90, 90 );

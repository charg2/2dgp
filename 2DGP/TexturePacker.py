#needed install pillow
from PIL import Image
#import matplotlib.pyplot as plt
import os;


def crop_wrapper(file_path:str, width_count, height_count:int, save_path:str):
    src_img = Image.open(file_path);
    width = src_img.width // width_count;
    height = src_img.height // height_count;
    for k, piece in enumerate(crop( file_path, height , width), 0):
        print(k);
        img=Image.new('RGBA', (width, height), 255);
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


def bmp_to_png(file_path:str, width:int, height:int, save_path:str):
    from PIL import Image;
    img = Image.open(file_path);
    new_img = img.resize( (img.width, img.height) );
    new_img.save( save_path, "png");

def resize_png(file_path:str, width:int, height:int, save_path:str):
    from PIL import Image;
    img = Image.open(file_path);
    new_img = img.resize( (width, height) );
    new_img.save( save_path, "png");

def bmp_to_png_multiple(file_path:str, width_multiple:int, height_multiple:int):
    from PIL import Image;
    img = Image.open(file_path);
    new_img = img.resize( (int(img.width * width_multiple), int(img.height * height_multiple)) );
    path = os.path.join(os.path.dirname(file_path),"img.png");
    new_img.save(path, "png");


if __name__=='__main__':
    #tt = Image.open('assets/tiles.png');
    #tt.show();
    #file_path = "C:\\Users\\지환\\Desktop\\던그리드\\OcO-master\\OcO-master\\던그리드\\image\\npc\\inn(420x140)6x2.png";
    #origin_path = os.path.dirname(file_path);
    #destination_path = origin_path + str("\\dest");


    file_path = "D:/_git/2dgp/2DGP/assets/UI/complete.png";
    save_path = "C:/";
    #save_path = "D:/_git/2dgp/2DGP/assets/";
    #save_path = "D:\\_git\\2dgp\\2DGP\\assets\\Weapon\\";

    #crop_wrapper(file_path, 5, 1, save_path);

    #리사이즈 png 

    resize_png(file_path, 1280, 200, save_path);
    #bmp_to_png_multiple(file_path, 4, 4.5);


#Image.open("sample1.bmp").save("sample1.png");
    #img = Image.open(file_path);
    #resize_multiple(img, 3, "coin.png");

    #crop(img,90, 90 );

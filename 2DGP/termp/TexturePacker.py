#needed install pillow
from PIL import Image
#import matplotlib.pyplot as plt
import os;


class TexturePacker:
    

    pass;


def crop(infile, height, width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

def resize(tx, ty):
    test_img = test_img.resize((tx, ty));
    plt.subplot(1, 2, 2);
    plt.imshow(test_img, cmap='Greys');
    plt.show();
    print("이미지 resize 한 후 : {0}x{1} - {2} ".format(tx, ty, test_img));



if __name__=='__main__':
    print("test");
    img = Image.open('assets/player.png');
    print("test");
    img.show();
    height = 90;
    width = 80;
    for k, piece in enumerate(crop('assets/player.png', height, width), 0):
        print("frist");        
        img=Image.new('RGBA', (height,width), 255)
        img.paste(piece)
        path = os.path.join('',"IMG-%s.png" % k);
        img.save(path)
        print("done");
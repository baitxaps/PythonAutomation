#! /usr/bin/env python3
# coding: utf-8

# https://blog.csdn.net/weixin_44037416/article/details/96842058

import os
from PIL import Image
from PIL import ImageColor

def PILTest():
    os.chdir('/Users/jishuyanfa-ios/Desktop/vcode/PythonAutomation/project/automate_online-materials')
    catIm = Image.open('zophie.png')
    print(catIm.size)
    width, height = catIm.size
    print(catIm.filename,catIm.format,catIm.format_description)
    catIm.save('zophie.jpg')
    im = Image.new('RGBA',(100, 200),'purple')
    im.save('purpleImage.png')
    im2 = Image.new('RGBA', (20, 20))
    im2.save('transparentImage.png')

    #crop
    croppedIm = catIm.crop((335, 345, 565, 560))
    croppedIm.save('cropped.png')
    # copy
    catIm = Image.open('zophie.png')
    catCopyIm = catIm.copy()

    #paste
    faceIm = catIm.crop((335, 345, 565, 560))
    print(faceIm.size)
    catCopyIm.paste(faceIm, (0, 0))
    catCopyIm.paste(faceIm, (400, 500))
    catCopyIm.save('pasted.png')

    catImWidth, catImHeight = catIm.size
    faceImWidth, faceImHeight = faceIm.size
    catCopyTwo = catIm.copy()
    for left in range(0, catImWidth, faceImWidth):
        for top in range(0, catImHeight, faceImHeight):
            print(left, top)
            catCopyTwo.paste(faceIm, (left, top))
    catCopyTwo.save('tiled.png')


    # resize
    width, height = catIm.size
    quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
    quartersizedIm.save('quartersized.png')
    svelteIm = catIm.resize((width, height + 300))
    svelteIm.save('svelte.png')
    
    # rotate
    catIm.rotate(90).save('rotated90.png')
    catIm.rotate(180).save('rotated180.png') 
    catIm.rotate(270).save('rotated270.png')
    catIm.rotate(6).save('rotated6.png')
    catIm.rotate(6, expand=True).save('rotated6_expanded.png')

    #transpose 镜像翻转
    catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

    # putpixel
    im = Image.new('RGBA', (100, 100))
    im.getpixel((0, 0))
    for x in range(100):
        for y in range(50):
           im.putpixel((x, y), (210, 210, 210))
    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
    im.getpixel((0, 0))
    im.getpixel((0, 50))
    im.save('putPixel.png')

PILTest()
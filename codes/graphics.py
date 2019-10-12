#! /usr/bin/env python3
# coding: utf-8

# https://blog.csdn.net/weixin_44037416/article/details/96842058

import os
from PIL import Image

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
    

PILTest()
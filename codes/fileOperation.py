#! /usr/bin/env python3
# coding: utf-8


import shutil
import os
import zipfile
import send2trash


def test1():
    # 复制文件和文件夹
    os.chdir('/Users/jishuyanfa-ios/Desktop/语音视频调研')
    # shutil.copy(source, destination)，将路径 source 处的文件复制到路径 destination 处的文件夹(source 和 destination 都是字符串)。
    # 如果 destination 是一个文件名，它将 作为被复制文件的新名字。该函数返回一个字符串，表示被复制文件的路径
    #shutil.copy('音视频调研.xlsx', '/Users/jishuyanfa-ios/Desktop')

    #shutil.copytree('/Users/jishuyanfa-ios/Desktop/语音视频调研', '/Users/jishuyanfa-ios/desktop/bacon_backup')

    # 文件和文件夹的移动与改名
    #shutil.move('/Users/jishuyanfa-ios/Desktop/语音视频调研', '/Users/jishuyanfa-ios/desktop/vcCode')

    # 永久删除文件和文件夹
    for filename in os.listdir():
        if filename.endswith('.rxt'):
            # 用 os.unlink(path)将删除 path 处的文件
            # 调用 os.rmdir(path)将删除 path 处的文件夹
            # 调用 shutil.rmtree(path)将删除 path 处的文件夹，它包含的所有文件和文件夹都会被删除
            os.unlink(filename)
            print(filename)


    # 用 send2trash 模块安全地删除 pip3 install send2trash

    # baconFile = open('bacon.txt', 'a') # creates the file
    # baconFile.write('Bacon is not a vegetable.')
    # baconFile.close()
    # send2trash.send2trash('bacon.txt')


    # 遍历目录树
    for folderName, subfolders, filenames in os.walk('.'):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
        print('')


def test2():
    # 读取 ZIP 文件
    exampleZip = zipfile.ZipFile('example.zip')
    print(exampleZip.namelist())
    spamInfo = exampleZip.getinfo('example/video&audio.xlsx')
    print(spamInfo.file_size)
    print(spamInfo.compress_size)
    print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo .compress_size, 2)))
    exampleZip.close()

    # 从 ZIP 文件中解压缩
    # exampleZip = zipfile.ZipFile('example.zip')
    # exampleZip.extractall()
    # exampleZip.close()

    # 创建和添加到 ZIP 文件
    newZip = zipfile.ZipFile('new.zip', 'w')
    newZip.write('音视频调研.xlsx', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

# test1()
# test2()

# 查找特定扩展名的文件(诸如.pdf 或.jpg),不论这些文件的位置在哪里,将它们拷贝到一个新的文件夹中


def copyPDFOrJPGFile(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
    
            # (fname,extension) = filename.split('.');
            # ext = extension.lower()

            ext = filename.endswith('.pdf')
            if ext:  # #ext == 'pdf' or ext == 'jpg':
                path = os.path.join(folderName, filename)
                shutil.copy(path, '/Users/jishuyanfa-ios/Desktop/Payload')

        print('')

#copyPDFOrJPGFile('/Users/jishuyanfa-ios/Desktop/Text')    



# 查找特别大的文件或文件夹 超过 100MB 的文件,将这些文件的绝对路径打印到屏幕上



def getMaxSizeFiel(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            #pass
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            path = os.path.join(folderName, filename)
            sizes = os.path.getsize(path)
            print(folderName + ': ' + filename + " size:" + str(sizes))

        print("")

        
getMaxSizeFiel('/Users/jishuyanfa-ios/Desktop/Text')


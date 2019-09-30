#! /usr/bin/env python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
import zipfile
import os


def backupToZip(folder):
    #os.chdir('/Users/jishuyanfa-ios/Desktop/语音视频调研')
    # Backup the entire contents of "folder" into a ZIP file.
    # make sure folder is absolute

    folder = os.path.abspath(folder)

    # 返回一个字符串，它包含path参数中最后一个斜杠 之前的所有内容
    # print(os.path.basename('/Applications/Microsoft')):Microsoft
    # 将返回一个字符串，它包含 path 参数 中最后一个斜杠之后的所有内容
    # print(os.path.dirname('/Applications/Microsoft')) :/Applications

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))

        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')


backupToZip('/Users/jishuyanfa-ios/Desktop/语音视频调研')

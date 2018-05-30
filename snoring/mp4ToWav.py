import os


sourceFolder = "./video"
destFolder = "./audio"
fileNameList = os.listdir(sourceFolder)

for fileName in fileNameList:
    sourceFilePath = os.path.join(sourceFolder, fileName)
    destFilePath = os.path.join(destFolder, fileName.replace(".mp4", ".wav"))
    cmd = 'ffmpeg.exe -i %s %s'%(sourceFilePath, destFilePath)
    os.system(cmd)
from scipy.io import wavfile
import os

entryMap = {}

fd = open("unbalanced_snoring_segments.csv", "r")

while 1:
	line = fd.readline()
	if not line:
		break
	tmp = line.split(", ")
	entryMap[tmp[0]] = [int(float(tmp[1])), int(float(tmp[2])), tmp[3]]
fd.close()


sourceFolder = "./audio"
destFolder = "./audioTrimed"

fileNames = os.listdir(sourceFolder)

for fileName in fileNames:
	sourceFileName = os.path.join(sourceFolder,fileName)
	destFileName = os.path.join(destFolder,fileName)

	filePrefix = fileName.split(".")[0]



	sampFreq, snd = wavfile.read(sourceFileName)
	startTime = entryMap[filePrefix][0]
	endTime = entryMap[filePrefix][1]

	startSample = startTime * sampFreq
	endSample = endTime * sampFreq

	targetSignal = snd[startTime*sampFreq:endTime*sampFreq]

	wavfile.write(destFileName, sampFreq, targetSignal)
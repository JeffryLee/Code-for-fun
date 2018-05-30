import pafy
from Tkinter import Tk

r = Tk()
r.withdraw()

fd = open("unbalanced_snoring_segments.csv", "r")

while 1:
    try:
        line = fd.readline()
        if not line:
            break
        tmp = line.split(", ")

        url = "https://www.youtube.com/watch?v=%s" % tmp[0]
        video = pafy.new(url)
        best = video.streams
        index= 0
        for b in best:
            if "mp4" == b.extension:
                break
            index += 1

        filename = video.streams[index]
        print tmp[0]
        x = filename.download(filepath="./video/" + tmp[0] + "." + filename.extension)
    except:
        print "error"
fd.close()
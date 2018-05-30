import sys, getopt
from scipy.io import wavfile
import snoringDetectionModule
def main(argv):
    inputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:", ["infile="])
    except getopt.GetoptError:
        print 'Error: test_arg.py -i <inputfile>'
        print '   or: test_arg.py --infile=<inputfile> --outfile=<outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print 'test_arg.py -i <inputfile>'
            print 'or: test_arg.py --infile=<inputfile>'

            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
    if inputfile.endswith(".wav"):
        sampFreq, snd = wavfile.read(inputfile)
        detectModule = snoringDetectionModule.snoringDetection()
        print detectModule.detect(sampFreq, snd)
    else:
        print 'Error: please input a wav file'


if __name__ == "__main__":
    main(sys.argv[1:])
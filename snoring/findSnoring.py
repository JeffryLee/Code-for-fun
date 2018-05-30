fd = open("unbalanced_train_segments.csv", "r")

targetArr = []
keyId = "/m/01d3sd"

while 1:
    line = fd.readline()
    if not line:
        break
    tmp = line.split(", ")
    if len(tmp)==4 and keyId in tmp[3]:
        targetArr.append(line)
    # pass # do something

fd.close()

fd = open("unbalanced_snoring_segments.csv", "w")
for line in targetArr:
    fd.write(line)
fd.close()
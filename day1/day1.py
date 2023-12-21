str2num = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "t3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9n"
}

def replace_text(stream):
    for k, v in str2num.items():
        stream = stream.replace(k,v)
    return stream

def calibration(stream):
    sum = 0
    text = stream.split("\n")
    for line in text:
        first_found = False
        last_found = False
        for i in range(len(line)):
            if line[i].isdigit() and not first_found:
                sum += int(line[i])*10
                first_found = True
            if line[len(line)-i-1].isdigit() and not last_found:
                sum += int(line[len(line)-i-1])
                last_found = True
    return sum

stream = open("input.txt","r").read()

print(calibration(stream))
print(calibration(replace_text(stream)))
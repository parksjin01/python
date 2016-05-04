fileName=raw_input()
key=input()
oper=raw_input()
pw=input()
tmp=0
filePass=open("res.txt", "r")
if(pw==123654):
    files=open(fileName, "rb")
    tmp=list(files.read())
    #print tmp
    files.close()
    files=open(fileName, "wb")
    files.write('')
    files.close()
    files=open(fileName, "ab")
    if oper=="d":
        for i in tmp:
            if ord(i)-key>=0:
                files.write(chr(ord(i)-key))
            else:
                files.write(chr(ord(i)-key+256))

    elif oper=="e":
        #print tmp
        for i in tmp:
            if ord(i)+key<256:
                files.write(chr(ord(i)+key))
            else:
                files.write(chr(ord(i)+key-256))

    else:
        print "Error"

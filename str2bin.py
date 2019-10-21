import re
import os

def string2bin(strBin):
    #strSub = re.findall("[0-9a-fA-F]+",strBin)
    #listSub = strBin.split()
    strBin = re.sub("\s",'',strBin)
    hexSub = bytes.fromhex(strBin)
    #hexSub = int.from_bytes(hexSub,'big')
    #hexSub = int(strBin,16)
    return(hexSub)
            

if __name__ == "__main__":
    with open("data.txt") as f:
        lisStrbin = f.readlines()
        for strbin in lisStrbin:
            hexSub = string2bin(strbin)
            binFile = open("data.bin",'ab+')
            binFile.write(hexSub)
            binFile.close()
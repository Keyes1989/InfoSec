import zipfile
import optparse
from threading import Thread


def extractFile(zf, pWord):
    try:
        zf.extractall(pwd=bytes(pWord, 'utf-8'))
        print ("\n-------------------------------")
        print ("[+] Password = " + pWord)
        print ("-------------------------------\n")
    except:
        pass

def main():
    parser = optparse.OptionParser("\nSpecify: "+"-f <zipfile> -d <dictionary>\n")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file/word list')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print (parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    passFile = open(dname)
    zf = zipfile.ZipFile(zname)
    for line in passFile.readlines():
        pWord = line.strip('\n')
        t = Thread(target=extractFile, args=(zf, pWord))
        t.start()


if __name__ == '__main__':
    main()

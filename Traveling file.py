import os.path
import os

def traveling_file(path):
    try:
        for i in os.listdir(path):
            if os.path.isfile(path+'/'+i)==True:
                print i
            elif os.path.isdir(path+'/'+i)==True:
                traveling_file(path+'/'+i)

    finally:
        return

traveling_file('/Users/Knight')

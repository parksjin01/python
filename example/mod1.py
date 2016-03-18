import shutil
import os
import time

def show_file_nfo(filename):
    stat_info=os.stat(filename)
    print 'Mode: ', stat_info.st_mode
    print 'Created: ', time.ctime(stat_info.st_ctime)
    print 'Accessed: ', time.ctime(stat_info.st_atime)
    print 'Modified: ', time.ctime(stat_info.st_mtime)


os.mkdir('example')
print 'Source: '
show_file_nfo('mod1.py')
shutil.copy('mod1.py', 'example')
print 'DEST:'
show_file_nfo('example/mod1.py')
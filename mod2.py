import shutil
import glob

print 'Before: ', glob.glob('mod*.*')
shutil.copyfile('mod1.py', 'mod2.py')
print 'After: ', glob.glob('mod*.*')
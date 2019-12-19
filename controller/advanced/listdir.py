import os

print([d for d in os.listdir('../../')])
try:
    os.mkdir('./os.test')
except IOError as e:
    print(e)


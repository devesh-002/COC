import sys
import time
import os
speed = float(input("Enter playback speed: "))
if(speed < 0):
    print("Enter valid speed")
DIR = 'replays'

file_num = len([name for name in os.listdir(
    DIR) if os.path.isfile(os.path.join(DIR, name))])
if(file_num == 0):
    print("No replays")
    exit(0)
print(("There are ", file_num,
      " files so select a number between 1 and ", file_num), end=": ")
file_to_run = int(input())
if(file_to_run < 1 or file_to_run > (file_num)):
    print("Enter valid file")
    exit(0)
script_dir = os.path.dirname(__file__)
rel_path = "replays/"+str(file_to_run)+".txt"
abs_file_path = os.path.join(script_dir, rel_path)
print(abs_file_path)
f = open(abs_file_path, "r")
char = ""
for i, line in enumerate(f):
    if(i % 17 == 0):
        sys.stdout.write(char)
        time.sleep(1/speed)
    else:
        char += line
with open(abs_file_path) as file:
    for line in (file.readlines()[-17:]):
        print(line, end='')
# Implement spawn points, rage spell(will leave this bs)

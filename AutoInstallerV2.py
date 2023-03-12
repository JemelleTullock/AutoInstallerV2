import os
import time

os.system("title AutoInstallerV2")

import os

os.system("color 0C")

app_dirs = input("Please enter the paths to the directories containing the applications (separated by commas): ").split(",")

for app_dir in app_dirs:
    app_dir = app_dir.strip()
    if not os.path.exists(app_dir):
        print(f"\033[31mError:\033[0m Directory '{app_dir}' does not exist.")
        continue
        
    for filename in os.listdir(app_dir):
        filepath = os.path.join(app_dir, filename)
        if os.path.isfile(filepath) and filename.endswith(".exe"):
            print(f"\033[31mInstalling {filename}...\033[0m")
            os.system(filepath)
        else:
            print(f"\033[31mSkipping {filename} (not an executable file)\033[0m")

countdown_time = 5
for i in range(countdown_time, 0, -1):
    print(f"\033[31mProgram will close in {i} seconds...\033[0m", end='\r')
    time.sleep(1)

os.system("exit")

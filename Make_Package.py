import shutil
from tkinter.filedialog import askdirectory
import tkinter
import os
from time import sleep
import sys


os.system("")
BRed = "\033[1;31m"  # Red
Color_Off = "\033[0m"  # Text Reset
BBlue = "\033[1;34m"  # Blue


# Copy New project folder(Empty folder)
root = tkinter.Tk()
root.withdraw()
dst = askdirectory(parent=root, initialdir="./..", title="select dir for copy template")

if dst == os.getcwd():
    print(BRed + "현재 폴더와 동일하므로 복사할 수 없습니다." + Color_Off)
    sleep(2)
    sys.exit()
elif len(os.listdir(dst)):
    print(
        BRed + "해당 폴더에 폴더 또는 파일이 존재하므로 복사할 수 없습니다." + Color_Off
    )
    sleep(2)
    sys.exit()


src = "./Template"
shutil.copytree(src=src, dst=dst, dirs_exist_ok=True)

os.chdir(dst)
package_name = os.path.basename(dst)
package_name = package_name[package_name.find("_") + 1 :]
os.rename("__PackageName__", package_name)


def replace_text(file_path, old_text, new_text):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    data = data.replace(old_text, new_text)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data)


# Replace __PackageName__ to package_name in Main.py
init_file_path = os.path.join(package_name, "__init__.py")
replace_text(init_file_path, "srtest-python", package_name)

# Replace __PackageName__ to package_name in info.py
info_file_path = os.path.join(package_name, "info.py")
replace_text(info_file_path, "__PackageName__", package_name)

# Rename Main.py to package_name
os.rename(
    os.path.join(package_name, "Main.py"),
    os.path.join(package_name, package_name + ".py"),
)

print(BBlue + "Done!" + Color_Off)
sleep(2)

import subprocess
import re

# Main.py 입력
package_path = "./Main.py"


# Main_Widget.py 에서 version과 deploy 여부를 리턴
def get_develop_info():
    global package_path
    with open(package_path, "r", encoding="utf-8") as f:
        contents = f.read()

    program_name = re.search(r'__program_name__ = "(.*)"', contents).group(1)
    versions = re.findall(r"__version__ = .*", contents)

    last_version = versions[-1]
    version = re.search(r"\d+.\d+.\d+", last_version)[0]

    return program_name, version


# cmd에서 pyinstaller 실행
def run_pyinstaller_with_version():
    program_name, version = get_develop_info()
    #     cmd = f'pyinstaller --clean --onefile --icon=..\..\Ico\Read_hwp_x.ico \
    # --noconsole --name "HWPX-EXCEL 변환기 - {version} 🚗" ..\Main_Widget.py'
    cmd = f'pyinstaller --clean --onefile --name "{program_name}-ver_{version}" {package_path}'

    print(cmd)
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    print(get_develop_info())

    run_pyinstaller_with_version()
    print("~~~~~~~~~~~~~~")
    print("     Done     ")
    print("~~~~~~~~~~~~~~")

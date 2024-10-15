# name - 해당 파이썬 패키지의 이름
# version - 해당 패키지의 배포 버전
# description (한줄) / long_description (README.md) - 패키지에 대한 설명
# packages - 프로젝트에 포함되는 패키지 리스트 (find_packages 함수로 __init__.py가 포함 된 모든 폴더 탐색)
# install_requires - 해당 패키지를 설치할 때 필요한 패키지 목록 (requirements.txt 활용)
# setup_requires - python setup.py를 실행할때 먼저 설치되어 있어야 하는 패키지 목록 (즉, 빌드에 필요한 패키지 목록) 
# tests_require - 테스트에 사용하는 패키지 목록
# python_requires - 해당 패키지를 실행하기 위해 필요한 파이썬의 최소 버전
# entry_points - 해당 패키지 설치 후 쉘 (Shell) 에서 실행 가능한 명령어와 실행할 함수 지정
# classifiers - PyPi (또는 사설 PyPi)에 등록될 메타 데이터를 설정한다. (실행 환경, 버전, GUI 여부 등)from setuptools import setup, find_packages

# name, version
    # __PackageName__ 폴더의 info.py에 정의 된 __package_name__과 __version__을 import하여 name과 version을 지정했다.
    # 소스 코드에서 해당 패키지 이름과 버전 정보를 사용해야 하는 경우에는 이러한 구조가 편리하다.
    # 소스코드에서 사용할 일이 없다면 name과 version에 직접 기입하는 것이 가독성, 직관성에 더 좋다.

# entry_points
    # entry_points 옵션에 console_scripts로 srtest-python=srtest.main:main으로 지정했다.
    # 해당 패키지를 설치하면 명령창에서 srtest-python으로 실행할 수 있다.
    # srtest-python 명령을 실행하면 srtest 폴더의 main.py 내에 정의 된 main 함수가 실행된다.


from setuptools import setup
from setuptools import find_packages
from __PackageName__.info import __package_name__, __version__


with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = f.read().splitlines()
with open("test_requirements.txt", "r", encoding="utf-8") as f:
    test_requires = f.read().splitlines()

setup(
    name=__package_name__,
    version=__version__,
    long_description=readme,
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    package_data={'': ['*.yaml', '*.yml']},
    # install_requires=requires,
    setup_requires=[
        "pytest-runner",
    ],
    # tests_require=test_requires,
    python_requires=">3.8",
    entry_points={
        "console_scripts": ["__PackageName__-python=__PackageName__.Main:main"]
    },
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: MacOS',
        'Programming Language :: Python :: 3.10'
    ]
)


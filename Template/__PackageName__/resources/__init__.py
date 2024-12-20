# 해당 프로그램의 기능을 작성하면서 사전에 정의한 기본 설정 값이나 데이터를 사용할 때 유용하다.

# 소스 코드와 설정 파일들을 분리하기 위해 resources라는 폴더로 분리한다.

 
# 일반적으로 실행에 필요한 설정 값은 명령창에서 --옵션 설정값 형태로 전달한다.

$ python train.py --epochs 50 --batch-size 64 --save-dir weights
 

# 하지만, 옵션이 많은 경우 모두 기입하기에는 불편한 경우가 많다.


# resource에 기본 설정 값을 사전에 정의하여 사용하면 불편함을 최소화 할 수 있다.

# 코드 작성할때 시작 부분에 실행 초기에 yml 파일에 정의한 값들을 기본 값으로 설정하도록 한다.
# 사용자가 직접 입력한 설정 값들을 파싱하여 해당 항목의 값을 변경한다.
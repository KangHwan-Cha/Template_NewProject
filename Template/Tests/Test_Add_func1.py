# 해당 프로그램의 기능을 작성하면서 특정 부분 또는 세부 기능을 별도의 py 파일로 분리한 경우에 해당한다.
# 별도로 분리한 기능이 정상적으로 작동하는지 테스트 하기 위한 파일이다.

# 파일명은 test_를 prefix로 지정하고, 테스트 대상이 되는 파일의 이름을 추가한다.

# pytest의 경우 다음과 같은 형식으로 테스트 코드를 작성한다.



# -*- coding: utf-8 -*-#

import pytest
from freezegun import freeze_time  # 테스트를 위해 고정 된 시간 값 사용


class Test부가기능:
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self, request):
        # 테스트에 필요한 변수 (경로, 초기값 등) 정의
        # 아래는 예제 코드
        test_folder = os.path.dirname(os.path.realpath(__file__))
        self.test_conf_file = os.path.join(test_folder, "resources", "config.yml")
        with open(self.test_conf_file, 'r', encoding='utf-8') as yaml_file:
            self.yaml_dict = yaml.load(yaml_file, Loader=yaml.Loader)
        # 테스트가 종료 된 이후 수행 될 코드 정의 (teardown)
        # fixture의 scope가 function이므로 각 테스트 함수가 종료될때마다 실행
        # 테스트를 종료할 때 수행하는 작업이 없으면 포함하지 않아도 됨
        def teardown():
            print('Function Tear down - - - - ')
        request.addfinalizer(teardown)
        
    def test_함수1(self):
        # 정상 조건 또는 예외 조건에 대한 변수 정의
        # 정의한 변수를 부가기능의 해당 함수에 인자로 전달하여 호출
        # 결과값 비교 (논리연산자는 >, <, ==, >=, <= 등)
        assert 결과값 논리연산자 기대값
        
        # 정상 조건, 예외 조건 케이스별로 반복
        
    ### 테스트 하려는 함수에 대한 테스트 추가
    
    # 아래는 예제 코드
    @freeze_time(datetime(2020, 3, 25, 10, 25, 22))
    def test_set_curr_time(self):
        """
        set_curr_time을 통해 현재 시각을 제대로 기록하는지 확인한다.
        """
        test_cls = EmailClient()
        test_cls.set_curr_time()
       
        assert str(test_cls.curr_time)[0:19] == "2020-03-25 10:25:22"
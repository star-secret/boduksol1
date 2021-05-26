
'''
    [모듈과 패키지]

        모듈(module)
            - 변수, 함수, 클래스 등을 모아 놓은 소스 파일(.py 파일)
            - 간단한 기능을 담을 때 사용
            - 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만들어진 소스 파일

        패키지(package)
            - 여러 모듈을 묶은 것
            - 코드가 많고 복잡할 때 사용(모듈에 비해서)
            - 관련 모듈들 끼리 한 폴더에 넣어 놓은 상태(폴더 = 패키지)

            - 폴더 안에 __init__.py 파일이 있어야 패키지가 됐었다. (없으면 패키지x)
                파이썬 3.3 버전 부터는 없어도 패키지로 인식된다.
                (하위 버전 호환을 위해 가급적 만들어 두는게 좋다.)

            - 폴더 안에 또 다른 폴더가 있는 하위 구성일 때도 동일
        * 파이썬 표준 라이브러리 : 파이썬에 기본으로 설치된 모듈과 패키지, 내장함수를 통칭
'''

'''
모듈을 가져 오는 방법 : import module1, module2
가져온 모듈을 이용하는법 : module.변수, module.함수(), module.클래스()

가져온 모듈을 이용할 때 모듈이름을 자기가 원하는대로 변경할 수 있다. 
import math로 수학 모듈 math를 가져왔다고 가정.
import math as m 이라는 코드를 치면 math.sqrt()가 아닌 m.sqrt()로 모듈을 이용할 수 있다
형식 : import module as name

*from module import * vs from module import 변수/함수/클래스
    만약 module에 속한 일부만을 사용하고 싶을 때는 
    from module import 변수,함수,클래스         라는 코드를 이용하면 된다. 
    module의 모든 변수, 함수, 클래스를 불러오고 싶을 때는 from module import * 이라는 코드를 이용하면 된다
    import math와 from math import * 의 차이점 : import math는 이용할 때 math.변수/함수()/클래스() 이런식으로 이용하여야 
    하지만 from math import * 는 그저 변수/함수()/클래스() 코드만 치면 이용할 수 있다.

*from module import 변수 as name
    import module as name과 from module import 변수,함수,클래스를 같이 이용하면
    from module import 변수 as name1, 함수 as name2, 클래스 as name3 가 된다..

*pip로 패키지설치하기
    pip install 패키지          (이 코드는 명령 프롬포트, 콘솔, 터미널에 입력해야한다)
    python -m install 패키지

*import로 패키지 가져오기
    import 패키지
    import 패키지.모듈
'''

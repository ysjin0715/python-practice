# pygame 설치 시 오류 해결법
## 에러의 발생
1. terminal에서 "pip install pygame"을 입력하자 오류코드 발생
2. 오류코드 정보 : Command "python setup.py egg_info" failed with error code 1 ...(파일경로로 추측)

## 해결법
1. 우선 아래의 코드를 입력 
- 참고링크 : <http://melonicedlatte.com/android/2018/05/21/221524.html>
```
# pycharm에서 입력 시
pip install --upgrade --ignore-installed pip setuptools

# 리눅스 환경에서 발생 시
sudo -H pip install --upgrade --ignore-installed pip setuptools
```
2. "Failed to write executable - trying to use .deleteme logic"라는 노란색 표시가 출력되나, 무시할 것.
3. terminal에서 "pip install pygame"를 입력
4. 정상적으로 pygame이 설치되는 것을 확인할 수 있음.
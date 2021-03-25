# Django Basic

## 개요

### 학습 목적
Django의 기본 구조와 Django에서 html을 어떻게 랜더링 하고 html form을 python으로 다루는 방법 및 데이터를 어떻게 관리하는지
에 대한 전반적인 구조 이해와 sqlite의 모델 작성법 등을 배운다

### Djnago의 기본 구조
Django는 FrameWork로써 
```bash
$ django-admin startproject {folderName} .
```
으로 기본 골자를 구성한다.

기본 골자를 구성하게되면 
- asgi.py
- settings.py
- urls.py
- wsgi.py

4가지 python 파일이 생성이되며 각각의 역할은 settings를 통해 app 등록 및 third party라이브러리 등록 static file 관리 등
  서버 전반적인 앱을 등록 및 관리를 한다.
  
**urls.py**는 앱의 전반적인 api 경로 및 rendering 경로 등을 등록하는 root url 관리 파일 이며
각 app들은 각각의 api를 등록하는 url.py를 가지고 있다.


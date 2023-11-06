# capture-lecture

> 강의 자료를 캡처하고, PDF로 변환하는 프로그램입니다.

MacBook Pro 14인치 1352 * 878 해상도에서 테스트했습니다.

이외 환경에서는 캡쳐 영역이 달라질 수 있습니다.

각자 환경에 맞게 수정하시면 됩니다.

## 설치

```bash
$ git clone https://github.com/ks1ksi/capture-lecture.git
$ cd capture-lecture
$ pip install -r requirements.txt
```

> ***시스템 권한이 필요할 수 있습니다.***

## 캡쳐

```bash
$ sudo python3 main.py
```

디렉토리가 생성되고, 그 안에 캡처된 이미지가 저장됩니다.

기본 단축키는 Tab입니다. 종료하려면 Ctrl + C를 누르세요.

## PDF 변환

```bash
$ sudo python3 converter.py
```

전체 디렉토리에 대해, 이미지를 PDF로 변환합니다.

PDF 파일 이름은 디렉토리 이름과 같습니다.
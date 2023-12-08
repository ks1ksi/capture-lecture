import os
import sys

import keyboard
import pyautogui
import pyscreeze

# 현재 사용 중인 운영체제를 출력합니다. darwin은 Mac OS를 의미합니다.
print(f"OS: {sys.platform}")

# For Mac OS
# TypeError: '<' not supported between instances of 'str' and 'int' 오류를 피하기 위해 버전을 튜플로 변경합니다.
# 추후 pyscreeze 버전이 올라가면서 이 부분이 수정되면 삭제해도 됩니다.
if (sys.platform == 'darwin'):
    pyscreeze.PIL__version__ = (0, 0, 0)

# 스크린샷 파일 이름에 붙일 번호입니다.
num = 1

# 스크린샷을 저장할 디렉토리 이름입니다.
dirname = 'computer_network_14_2'

# 스크린샷을 저장할 디렉토리를 생성합니다.
if not os.path.exists(dirname):
    os.mkdir(dirname)

print('Lecture %s' % dirname)

# 특정 영역의 스크린샷을 찍습니다. 디렉토리에 이름을 붙여 저장합니다.
# 스크린샷은 tab 키를 누를 때마다 찍습니다.
# Ctrl + C를 눌러 종료할 수 있습니다.
print('Press Ctrl-C to quit.')
while True:
    print('Waiting for tab key...')
    keyboard.wait('tab')
    pyautogui.screenshot(
        # 맥북 프로 14인치 3024 x 1964
        # 디스플레이 기본 설정 1512 x 982
        # 픽셀 찍은 숫자의 2배로 설정해야 정확한 위치에 스크린샷을 찍습니다.
        # (190, 85) ~ (1320, 930)
        f'{dirname}/screenshot{num}.png', region=(380, 170, 2260, 1690))  # x, y, width, height
    print(f'screenshot{num}.png saved!')
    num += 1

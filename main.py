import os

import keyboard
import pyautogui
import pyscreeze

# For Mac OS
# TypeError: '<' not supported between instances of 'str' and 'int' 오류를 피하기 위해 버전을 튜플로 변경합니다.
# 추후 pyscreeze 버전이 올라가면서 이 부분이 수정되면 삭제해도 됩니다.
# Windows에서 오류가 발생하면 이 부분을 주석처리하고 실행해보세요.
pyscreeze.PIL__version__ = (0, 0, 0)

# 스크린샷 파일 이름에 붙일 번호입니다.
num = 1

# 스크린샷을 저장할 디렉토리 이름입니다.    
dirname = 'computer_network_5_1'

# 스크린샷을 저장할 디렉토리를 생성합니다.
if not os.path.exists(dirname):
    os.mkdir(dirname)

print('Lecture %s' % dirname)

# 특정 영역의 스크린샷을 찍습니다. 디렉토리에 이름을 붙여 저장합니다.
# 스크린샷은 tab 키를 누를 때마다 찍습니다.
# Ctrl + C를 눌러 종료할 수 있습니다.
print ('Press Ctrl-C to quit.')
while True:
    print('Waiting for tab key...')
    keyboard.wait('tab')
    pyautogui.screenshot(
        f'{dirname}/screenshot{num}.png', region=(340, 140, 2030, 1530))
    print(f'screenshot{num}.png saved!')
    num += 1

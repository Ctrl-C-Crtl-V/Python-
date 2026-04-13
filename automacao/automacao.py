import pyautogui as py
import time as t

##M.pos

py.press('winleft')
t.sleep(0.5)
py.write('edge')
t.sleep(0.5)
py.press('enter')
t.sleep(0.5)
py.write('https://www.oul.com.br,' interval=0.05)
t.sleep(0.5)
py.press('enter')
t.sleep(0.5)
py.press('F11')
t.sleep(0.5)
py.moveTo(1911,55)
t.sleep(0.5)
py.click()
t.sleep(0.5)
py.scroll(-1000)
t.sleep(0.5)
py.moveTo(951,360)
t.sleep(0.5)
py.click()
t.sleep(8)
py.hotkey('alt''F4')
py.alert('Fim do Script')
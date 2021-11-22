import numpy as np
import matplotlib.pyplot as plt
import subprocess
import pyautogui as gui
import pyperclip
from time import sleep
from PIL import Image, ImageGrab

def nox_open():
  p = "/Applications/NoxAppPlayer.app"
  q = "osascript -e 'quit app \"/Applications/NoxAppPlayer.app\"'"
  nox_close_p = "./nox_close.png"
  proc = subprocess.Popen(["open", p])
  sleep(30)
  
  print("ok")
  gui.moveTo(320, 260)

  subprocess.Popen(q, shell=True)
  sleep(3)

  pos = gui.locateCenterOnScreen(nox_close_p, grayscale=True, confidence=0.8)
  print(pos)
  gui.click(pos.x, pos.y)
  sleep(3)
  proc.terminate()


def dmm_open():

  dmm_icon = "./dmm.png"
  page_icon = "./mypage.png"
  dsks_icon = "./dstationks.png"
  data_icon = "./show_data.png"
  search_icon = "./search_no.png"
  star_icon = "./star.png"
  next_icon = "./next.png"

  p = "/Applications/NoxAppPlayer.app"
  proc = subprocess.Popen(["open", p])
  sleep(20)
  
  dmm = None
  while dmm is None:
    sleep(1)
    dmm = gui.locateCenterOnScreen(dmm_icon, confidence=0.8)
  gui.click(dmm)

  page = None
  while page is None:
    sleep(1)
    page = gui.locateCenterOnScreen(page_icon, confidence=0.8)
  gui.click(page)

  sleep(5) # 広告

  dsks = None
  while dsks is None:
    sleep(1)
    dsks = gui.locateCenterOnScreen(dsks_icon, confidence=0.8)
  gui.click(dsks)

  data = None
  while data is None:
    sleep(1)
    data = gui.locateCenterOnScreen(data_icon, confidence=0.8)
  gui.click(data)

  search = None
  while search is None:
    sleep(1)
    search = gui.locateCenterOnScreen(search_icon, confidence=0.8)
  gui.click(search)

  sleep(1)
  no = 723
  pyperclip.copy(no)
  gui.hotkey("command", "v")
  sleep(1)
  gui.hotkey("return")

  star = None
  while star is None:
    sleep(1)
    star = gui.locateCenterOnScreen(star_icon, confidence=0.9)
  
  sleep(5)
  print(star)
  gui.moveTo(star.x + 100, star.y + 500)
  sleep(1)
  gui.dragRel(0, -350, duration=3, button='left')

  sleep(1)

  next_ = None
  while next_ is None:
    sleep(1)
    next_ = gui.locateCenterOnScreen(next_icon, confidence=0.9)
  gui.click(next_)

  sleep(5)
  print(star)
  gui.moveTo(star.x + 100, star.y + 500)
  sleep(1)
  gui.dragRel(0, -350, duration=3, button='left')

  sleep(1)

  next_ = None
  while next_ is None:
    sleep(1)
    next_ = gui.locateCenterOnScreen(next_icon, confidence=0.9)
  gui.click(next_)

if __name__ == '__main__':
  
  dmm_open()
  # rect = 0., 0., 400., 400.
  # img = ImageGrab.grab(rect)
  
  # plt.imshow(img)
  # plt.show()

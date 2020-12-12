from python_imagesearch.imagesearch import imagesearch, region_grabber, imagesearcharea
import pyautogui
import time
import os
import cv2
import numpy as np

vuota = './vuota.png'


def myimagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    ret, img_threshold = cv2.threshold(img_gray, 220, 255, cv2.THRESH_BINARY_INV)
    template = cv2.imread(image, 0)
    ret, template = cv2.threshold(template, 220, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow('img_rgb', img_rgb)
    # cv2.imshow('template', template)
    # cv2.imshow('img_threshold', img_threshold)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    res = cv2.matchTemplate(img_threshold, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

#r = (00, 00, 1900, 1024)
#im = region_grabber(r)
#
#aaa = pyautogui.screenshot(region=(850,278,1302,555))

#imPresente = region_grabber(region=(850,278,1302,555))
#imImperfetto = region_grabber((1375,278,1822,555))
#imPassRem = region_grabber((850,683,1302,959))
#imFuturo = region_grabber((1375,683,1822,956))

#pyautogui.displayMousePosition()

# Presente

images = ['./img/presente/' + x for x in os.listdir('./img/presente')]
for img in images:
    pos = myimagesearcharea(img, 100, 200, 900, 1150, 0.8)
    im1 = pyautogui.screenshot(region=(850,278,490,320))
    posVuota = imagesearcharea(vuota, 0, 0, 0, 0, 0.8, im1)
    print(f"{img}")
    if pos[0] == -1:
        print(f"{img} not found")
        continue
    if posVuota[0] == -1:
        print("posVuota not found")
        continue
    pyautogui.moveTo(pos[0]+100+30, pos[1]+200+30)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(posVuota[0]+850+30, posVuota[1]+278+30, 0.01)
    pyautogui.mouseUp()
    #pyautogui.mouseUp(posVuota[0]+850+30, posVuota[1]+278+30)
    time.sleep(0.1)
   
# imperfetto

images = ['./img/imperfetto/' + x for x in os.listdir('./img/imperfetto')]
for img in images:
    pos = myimagesearcharea(img, 100, 200, 900, 1150, 0.8)
    im1 = pyautogui.screenshot(region=(1350,278,490,320))
    # img_rgb = np.array(im1)
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('img_gray', img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    posVuota = imagesearcharea(vuota, 0, 0, 0, 0, 0.8, im1)
    print(f"{img}")
    if pos[0] == -1:
        print(f"{img} not found")
        continue
    if posVuota[0] == -1:
        print("posVuota not found")
        continue
    pyautogui.moveTo(pos[0]+100+30, pos[1]+200+30)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(posVuota[0]+1350+30, posVuota[1]+278+30, 0.01)
    pyautogui.mouseUp()
    #pyautogui.mouseUp(posVuota[0]+850+30, posVuota[1]+278+30)
    time.sleep(1.5)


# http://wordwall.net/play/320/710/5523

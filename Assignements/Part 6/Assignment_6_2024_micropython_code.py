############################################
# Assignment 6
# Instructions:
# 1. Create a new project in UIFlow.
# 2. Copy the code below and paste it into the UIFlow editor.
# 3. Run the code on your M5Stack device.
############################################


from m5stack import *
from m5stack_ui import *
from uiflow import *
import urequests
from libs.json_py import *
import json



screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


userID = None
deviceID = None
deviceIDResponse = None



SIMF = M5Label('SIMF signal interceptor', x=33, y=23, color=0x000, font=FONT_MONT_22, parent=None)
Connect = M5Btn(text='Connect', x=112, y=111, w=95, h=38, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
DeviceFromID = M5Btn(text='Get user device from ID', x=45, y=78, w=230, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
LogDevice = M5Btn(text='Track device from ID', x=65, y=164, w=190, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
B2 = M5Btn(text='2', x=85, y=59, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B1 = M5Btn(text='1', x=33, y=59, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B3 = M5Btn(text='3', x=133, y=59, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B4 = M5Btn(text='4', x=33, y=105, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B5 = M5Btn(text='5', x=85, y=105, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B6 = M5Btn(text='6', x=133, y=105, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B7 = M5Btn(text='7', x=33, y=151, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B8 = M5Btn(text='8', x=85, y=151, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
GetDeviceID = M5Btn(text='Get device ID', x=186, y=66, w=100, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B9 = M5Btn(text='9', x=133, y=151, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
backtomain = M5Btn(text='Go back', x=186, y=134, w=100, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B0 = M5Btn(text='0', x=85, y=196, w=30, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
StartLog = M5Btn(text='Curent connection', x=175, y=66, w=140, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Userid = M5Label('User ID', x=33, y=25, color=0x000, font=FONT_MONT_18, parent=None)
IDVisible = M5Label('Text', x=156, y=23, color=0x000, font=FONT_MONT_22, parent=None)
IPinfo = M5Label('IP adress found,', x=15, y=82, color=0x000, font=FONT_MONT_14, parent=None)
IPinfo2 = M5Label('You can check the origin', x=15, y=113, color=0x000, font=FONT_MONT_14, parent=None)
IPinfo3 = M5Label('here: iplocation.net', x=15, y=135, color=0x000, font=FONT_MONT_14, parent=None)


# Describe this function...
def start():
  global userID, deviceID, deviceIDResponse
  hideAll()
  SIMF.set_hidden(False)
  Connect.set_hidden(False)

# Describe this function...
def show_numpad():
  global userID, deviceID, deviceIDResponse
  B1.set_hidden(False)
  B2.set_hidden(False)
  B3.set_hidden(False)
  B4.set_hidden(False)
  B5.set_hidden(False)
  B6.set_hidden(False)
  B7.set_hidden(False)
  B8.set_hidden(False)
  B9.set_hidden(False)
  B0.set_hidden(False)

# Describe this function...
def hide_numpad():
  global userID, deviceID, deviceIDResponse
  B1.set_hidden(True)
  B2.set_hidden(True)
  B3.set_hidden(True)
  B4.set_hidden(True)
  B5.set_hidden(True)
  B6.set_hidden(True)
  B7.set_hidden(True)
  B8.set_hidden(True)
  B9.set_hidden(True)
  B0.set_hidden(True)

# Describe this function...
def connect():
  global userID, deviceID, deviceIDResponse
  hide_numpad()

# Describe this function...
def hideAll():
  global userID, deviceID, deviceIDResponse
  hide_numpad()
  DeviceFromID.set_hidden(True)
  LogDevice.set_hidden(True)
  Connect.set_hidden(True)
  GetDeviceID.set_hidden(True)
  backtomain.set_hidden(True)
  StartLog.set_hidden(True)
  SIMF.set_hidden(True)
  Userid.set_hidden(True)
  IDVisible.set_hidden(True)
  IPinfo.set_hidden(True)
  IPinfo2.set_hidden(True)
  IPinfo3.set_hidden(True)

# Describe this function...
def GetDeviceIDFromUserID():
  global userID, deviceID, deviceIDResponse
  try:
    req = "TODO"
    deviceID = "TODO"
    deviceIDResponse = "TODO"
    gc.collect()
    req.close()
  except:
    IDVisible.set_text('Error!')
  return get_json_key(deviceIDResponse, 'deviceID')

# Describe this function...
def getLogsFromDeviceID():
  global userID, deviceID, deviceIDResponse
  try:
    req = "TODO"
    deviceID = "TODO"
    deviceIDResponse = "TODO"
    IPinfo.set_hidden(False)
    IPinfo2.set_hidden(False)
    IPinfo3.set_hidden(False)
    gc.collect()
    req.close()
  except:
    IDVisible.set_text('Fail')
  return get_json_key(deviceIDResponse, 'ConnectedIP')


def B1_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('1'))
  IDVisible.set_text(str(userID))
  pass
B1.pressed(B1_pressed)

def Connect_pressed():
  global userID, deviceID, deviceIDResponse
  hideAll()
  SIMF.set_hidden(False)
  DeviceFromID.set_hidden(False)
  LogDevice.set_hidden(False)
  pass
Connect.pressed(Connect_pressed)

def B2_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('2'))
  IDVisible.set_text(str(userID))
  pass
B2.pressed(B2_pressed)

def backtomain_pressed():
  global userID, deviceID, deviceIDResponse
  hideAll()
  SIMF.set_hidden(False)
  DeviceFromID.set_hidden(False)
  LogDevice.set_hidden(False)
  pass
backtomain.pressed(backtomain_pressed)

def B3_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('3'))
  IDVisible.set_text(str(userID))
  pass
B3.pressed(B3_pressed)

def B4_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('4'))
  IDVisible.set_text(str(userID))
  pass
B4.pressed(B4_pressed)

def B5_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('5'))
  IDVisible.set_text(str(userID))
  pass
B5.pressed(B5_pressed)

def B6_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('6'))
  IDVisible.set_text(str(userID))
  pass
B6.pressed(B6_pressed)

def DeviceFromID_pressed():
  global userID, deviceID, deviceIDResponse
  Userid.set_text('UserID')
  hideAll()
  show_numpad()
  GetDeviceID.set_hidden(False)
  backtomain.set_hidden(False)
  IDVisible.set_hidden(False)
  Userid.set_hidden(False)
  userID = ''
  IDVisible.set_text(str(userID))
  pass
DeviceFromID.pressed(DeviceFromID_pressed)

def B7_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('7'))
  IDVisible.set_text(str(userID))
  pass
B7.pressed(B7_pressed)

def LogDevice_pressed():
  global userID, deviceID, deviceIDResponse
  hideAll()
  show_numpad()
  StartLog.set_hidden(False)
  backtomain.set_hidden(False)
  IDVisible.set_hidden(False)
  Userid.set_hidden(False)
  userID = ''
  IDVisible.set_text(str(userID))
  Userid.set_text('Device ID:')
  pass
LogDevice.pressed(LogDevice_pressed)

def B8_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('8'))
  IDVisible.set_text(str(userID))
  pass
B8.pressed(B8_pressed)

def GetDeviceID_pressed():
  global userID, deviceID, deviceIDResponse
  Userid.set_text('DeviceID:')
  IDVisible.set_text('Loading')
  hide_numpad()
  IDVisible.set_text(str(GetDeviceIDFromUserID()))
  pass
GetDeviceID.pressed(GetDeviceID_pressed)

def B9_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('9'))
  IDVisible.set_text(str(userID))
  pass
B9.pressed(B9_pressed)

def StartLog_pressed():
  global userID, deviceID, deviceIDResponse
  Userid.set_text('Ip adress:')
  IDVisible.set_text('Loading')
  IDVisible.set_text(str(getLogsFromDeviceID()))
  hide_numpad()
  pass
StartLog.pressed(StartLog_pressed)

def B0_pressed():
  global userID, deviceID, deviceIDResponse
  userID = (str(userID) + str('0'))
  IDVisible.set_text(str(userID))
  pass
B0.pressed(B0_pressed)


start()

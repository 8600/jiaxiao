import time
import random
import string
import aiohttp
import asyncio
import datetime

async def fetch(session, url):
  header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'cookie': 'JX_LoginOn=' + ''.join(random.sample(string.ascii_letters + string.digits, 8)) + ';'
  }
  async with session.get(url, headers=header_dict) as response:
    return await response.text()

async def main():
  # while True:
  #   async with aiohttp.ClientSession() as session:
  #     html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.812.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
  #     print(html)
  #   time.sleep(1)
  while True:
    # 获取四天后日期
    today = datetime.date.today() + datetime.timedelta(days=6)
    day = str(today.day)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    h = time.strftime("%H")
    if (h == "06" or h == "07"):
      print("进入时间段!")
      # 分钟
      m = time.strftime("%M")
      if h == "06":
        if int(m) >= 56:
          s = time.strftime("%S")
          if (int(m) >= 59 and int(s) >= 44):
            print('尽全力！')
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            async with aiohttp.ClientSession() as session:
              html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.812.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
              print(html)
            async with aiohttp.ClientSession() as session:
              html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.15.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
              print(html)
            time.sleep(1)
          else:
            async with aiohttp.ClientSession() as session:
              html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.812.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
              print(html)
            time.sleep(3)
            async with aiohttp.ClientSession() as session:
              html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.15.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
              print(html)
            time.sleep(3)
        else:
          print('准备请求,再等10秒钟!')
          time.sleep(10)
      else:
        if int(m) < 2:
          async with aiohttp.ClientSession() as session:
            html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.15.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
            print(html)
          time.sleep(1)
          async with aiohttp.ClientSession() as session:
            html = await fetch(session, 'http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil?ipaddress=192.168.1.106&ossdk=26&os=an&trainType=3&xxzh=51852038&isJcsdYyMode=5&imei=50E276A23A9DDADF2A9902D1F7AA81CE&appversion=6.2.5.1&params=Z1505.2018%2F12%2F' + day + '.15.&osversion=8.0.0&version=6.2.5.1&jlcbh=')
            print(html)
          time.sleep(1)
        else:
          print("等待20小时")
          time.sleep(60 * 60 * 20)
    else:
      print("再等8分钟!")
      time.sleep(480)
  

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
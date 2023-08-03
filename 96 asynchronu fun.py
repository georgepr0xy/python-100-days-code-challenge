import time
import asyncio
import requests
async def function1():
    url = 'https://www.facebook.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('facebook.ico', 'wb').write(r.content)

    print("func 1")

async def function2():
    url = 'https://www.facebook.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('facebook2.ico', 'wb').write(r.content)
    print("func 2")

async def function3():
    url = 'https://www.facebook.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('facebook3.ico', 'wb').write(r.content)
    print("func 3")

async def main():
  l=await asyncio.gather(
      function1(),
      function2(),
      function3(),
  ) 
  print(l)
#  task=asyncio.create_task(function1())
# #  await function1()
#  await function2()
#  await function3()    

asyncio.run(main())
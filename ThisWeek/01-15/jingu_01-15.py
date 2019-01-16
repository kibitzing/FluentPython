"""
Asyncio Revisited in python version 3.5 or after.
source code and explanation ref: https://soooprmx.com/archives/6882

"""

import asyncio
import random

async def greet(msg):
    await asyncio.sleep(1)
    print(msg)

async def lazy_great(msg, delay=1):
    # await asyncio.sleep(1)
    # print(msg)
    print(msg, 'will be displayed in', delay,'seconds')
    await asyncio.sleep(delay)
    return msg.upper()

async def time_log():
    i = 0
    print(' time logging starts.')
    while True:
        await asyncio.sleep(1)
        i += 1
        print(' ...%02d sec' % (i,))

async def main():
    t = asyncio.ensure_future(time_log())
    messages = ['hello', 'world', 'apple', 'banana', 'cherry']
    fts = [asyncio.ensure_future(lazy_great(m, random.randrange(1,5))) for m in messages]

    result = await asyncio.gather(*fts)
    t.cancel()
    print(result)

loop = asyncio.get_event_loop()
# loop.run_until_complete(lazy_great('hello', 3))
loop.run_until_complete(main())
loop.close()


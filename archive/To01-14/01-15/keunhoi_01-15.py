#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p562-ch18end
# Example 18-10~18

"""
	reference:
	https://pythonprogramming.net/asyncio-basics-intermediate-python-tutorial/
"""

# 실용적인 예제는 아니지만, asyncio에 대해서 찾아보던 중 발견한 예제 코드.
import asyncio

async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)	# yield from 은 3.5부터 await로 작성한다.

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1,divs2,divs3])
    return divs1, divs2, divs3


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())	# run forever도 있다.
        print(d1.result())
    except Exception as e:
        # logging...etc
        pass
    finally:
        loop.close()	# close는 무조건 해야하기 때문에 이전에 배운 finally를 사용하게 된다.
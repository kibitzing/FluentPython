#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
"""
    Created by Jingu Kang on 14/01/2019.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION:
        implementation and comments of code 18-14
        quite not sure with TCP server usage
"""

import sys
import asyncio
# should import charfinder from https://github.com/fluentpython/example-code/blob/master/18-asyncio/charfinder/charfinder.py

from charfinder import UnicodeNameIndex # UnicodeNameIndex: 문자명 인덱스 생성, 쿼리 메서드 제공

CRLF = b'\r\n'
PROMPT = b'?> '

index = UnicodeNameIndex() # 객체 생성할 떄 기존 charfinder_index.pickle이 있으면 사용, 없으면 인덱스 빌드 -> 수초 소

@asyncio.coroutine
def handle_queries(reader, writer): # 서버에 전달할 코루틴
    while True: # 제어문자 올때 까지 무한 루프
        writer.write(PROMPT) # not coroutine
        yield from writer.drain() # is coroutine

        data = yield from reader.readline() # is coroutine

        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = '\x00' # null, 간편함을 위한 트릭

        client = writer.get_extra_info('peername')
        print('Received from {}:{!r}'.format(client, query))
        if query: # 제어문자 받으면 탈출
            if ord(query[:1]) < 32:
                break
            lines = list(index.find_description_strs(query))
            if lines:
                writer.writelines(line.encode() +CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)

            yield from writer.drain()
            print('Sent {} results'.format(len(lines)))

        # 종료
        print('Close the client socket')
        writer.close()

def main(address='127.0.0.1', port=2323):
    port = int(port)
    loop = asyncio.get_event_loop()
    # 서버 가져오기
    server_coro = asyncio.start_server(handle_queries, address, port, loop=loop)
    server = loop.run_until_complete(server_coro)
    # 서버 주소, 포트 가져오기
    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    print('Server shutting down.')
    server.close()

    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == '__main__':
    main(*sys.argv[1:])

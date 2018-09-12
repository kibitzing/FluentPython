import wave
import struct
from matplotlib import pyplot as plt

# 슬라이싱 예제, wav파일 채널별로 분리하여 플롯으로 출력하기

waveFile = wave.open('asd.wav','r')
format = "<" + str(waveFile.getnchannels()*waveFile.getnframes()) + "h"
ch_num = waveFile.getnchannels()
a = waveFile.readframes(waveFile.getnframes())
k = struct.unpack(format, a)
fig = plt.figure()
for i in range(0,ch_num):
    fig.add_subplot(ch_num,1,i+1)
    plt.plot(range(0,k[0+i::ch_num].__len__()),k[0+i::ch_num])
    print(i)
plt.show()
waveFile.close()
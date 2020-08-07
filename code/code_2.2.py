#使用字符串复制，用计算机打印出“爱你一万遍”，打印100次
import time
start = time.time()
word = '爱你一万遍'
words = word * 10000000
end = time.time()
# print(words)
print(end - start)

start = time.time()
temp = []
for i in range(10000000):
    temp.append(word)
words = ''.join(temp)
end = time.time()
print(end - start)

start = time.time()
words = ''
for i in range(10000000):
    words += word
end = time.time()
print(end - start)



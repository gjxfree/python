# 将”to be or not to be”字符串倒序输出
word = 'to be or not to be'
new_word = []
i = len(word)
while i:
    i -= 1
    new_word.append(word[i])
print(''.join(new_word))
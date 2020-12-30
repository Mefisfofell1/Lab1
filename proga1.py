chars = 0
empty_space = 0
word = 0
row_num = 0
count_punctuation = 0
count_sentence = 0
punc = '.,:;-()"?'
sentence_punc = '.!?'

with open("steam.csv", encoding='utf8') as f:
    for row in f:
        row_num += 1
        for letter in row:
            chars += 1
            if letter == ' ':
                empty_space += 1
            for i in punc:
                if letter == i:
                    count_punctuation += 1
            for i in sentence_punc:
                if letter == i:
                    count_sentence += 1

chars_wo_space = chars - empty_space
chars_wo_pun = chars - count_punctuation
word = empty_space + row_num

print('Символов', chars)
print('Символов без пробела', chars_wo_space)
print('Символов без знаков препинания', chars_wo_pun)
print('Количество слов', word)
print('Количество предложений', count_sentence)
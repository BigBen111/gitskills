import re
from collections import Counter
with open('training_label.txt', 'r',encoding='UTF-8') as f:
    train_0 = f.read()
def clean_text(text):
    # 去除特殊字符和标点符号
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    text = text.replace("+++$+++"," ")
    # 将文本转换为小写
    text = text.lower()
    # 去除多余的空格
    text = re.sub(r"\s+", " ", text)
    return text
text = train_0
# 清洗文本
train_cleaned = clean_text(text)
print("train_cleaned")

def tokenize(text):
    # 将文本中的标点符号替换为空格
    text = re.sub(r'[^\w\s]', ' ', text)
    # 将文本按空格分割成单词列表
    tokens = text.split()
    return tokens

text_2 = text
# 分词
train_3 = tokenize(text_2)
print("text.split done")


# 停用词列表
with open('stop.txt', 'r',encoding='UTF-8') as f:
    stop_0 = f.read()
    stop_words = stop_0.split("\n")
# 去除停用词
text_stop = [word for word in train_3 if word.lower() not in stop_words]
# 打印结果 为list
#print(text_stop)
print("stop list finished")
#构件词频表

words = Counter(text_stop)

print('before：',len(words))
words = {k:v for k,v in words.items() if v>1}
print('after：',len(words))

words = sorted(words, key=words.get,reverse=True)
print(words[:10])                                    # 打印一下出现次数最多的10个单词
print(type(words))

words = ['_PAD'] + words
words = ['_UNK'] + words
#映射
word2idx = {o:i for i,o in enumerate(words)}
idx2word = {i:o for i,o in enumerate(words)}
print(word2idx['good'])
print(idx2word[100])
print(words)
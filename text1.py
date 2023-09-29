import re
import subprocess
with open('training_label.txt', 'r',encoding='UTF-8') as f:
    train_0 = f.readlines()
train_len = 200000



def clean_text(text):
    # 去除特殊字符和标点符号
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    text = text.replace(r"+++$+++", " ")
    # 将文本转换为小写
    text = text.lower()
    # 去除多余的空格
    text = re.sub(r"\s+", " ", text)
    return text
train_cleaned = [[] for _ in range(train_len)]
for i in range(train_len):
    train_cleaned[i] = clean_text(train_0[i])
print("train_cleaned")

def tokensize(text):
    # 将文本中的标点符号替换为空格
    text = re.sub(r'[^\w\s]', ' ', text)
    # 将文本按空格分割成单词列表
    tokens = text.split()
    return tokens

text_2 = [[] for _ in range(train_len)]
for i in range(train_len):
    text_2[i] = tokensize(train_cleaned[i])
print(text_2[1])

#将数字抽取出来分开
train_labels = []
for i in range(train_len):
    train_labels.append([0 if x.split(' ')[0] == '0' else 1 for x in train_0[i]])
#print(len(train_labels))

# 停用词列表
with open('stop.txt', 'r',encoding='UTF-8') as f:
    stop_0 = f.read()
    stop_words = stop_0.split("\n")
# 去除停用词
text_stop = [[] for _ in range(train_len)]
for i in range (train_len):
    text_stop[i] = [word for word in text_2[i] if word.lower() not in stop_words]
# 打印结果 为list
#print(text_stop)
print(type(text_stop))

result = subprocess.run(['python','Dic.py'], capture_output=True, text=True,encoding="UTF-8")
#注意编码格式的修改
print(result.stdout)

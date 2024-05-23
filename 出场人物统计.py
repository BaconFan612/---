import jieba

# 打开并读取“西游记.txt”
with open(r"西游记.txt", "r", encoding='utf-8') as f:  # 使用 'r' 模式和正确的编码
    txt = f.read()

# 构建排除词库
excludes = {"一个", "那里", "怎么", "我们", "不知", "两个", "甚么",
            "只见", "不是", "原来", "不敢", "闻言", "如何", "什么"}

# 使用jieba分词
words = jieba.lcut(txt)

# 对划分的单词计数
counts = {}
for word in words:
    if len(word) == 1 and word not in excludes:  # 排除单字符且不在排除词库中的词
        continue
    elif word == "行者" or word == "大圣" or word == "老孙":
        rword = "悟空"
    elif word == "师父" or word == "三藏" or word == "长老":
        rword = "唐僧"
    elif word == "悟净" or word == "沙和尚":
        rword = "沙僧"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

# 删除无意义的词语（确保它们在counts中）
for word in excludes:
    if word in counts:
        del counts[word]

    # 按词语出现的次数排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

# 假设只输出前9个最常见的词
for i in range(min(9, len(items))):  # 确保不会超出items的范围
    word, count = items[i]
    print("{0:<5}{1:>5}次".format(word, count))
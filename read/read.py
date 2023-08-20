data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data),'筆資料')



sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	print(sum_len)

print('留言的平均是', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'比長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')


#文字計數

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增new key in wc dictionary
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['alice'])

while True:
	word = input('查啥?')
	if word == 'exit':
		break
	if word in wc:
		print(word, '出現', wc[word], '次')
	else:
		print('沒出現過')

print('tks using')
















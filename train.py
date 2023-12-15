import sys

counter = 0
line= sys.stdin.read()
for c in line:
	counter = counter + 1



word = ['مـذكـــرة', 'التقـابـل', 'اللغــوي', 'وتحليـل', 'الأخطـاء', '(', '522', 'عدد', '(', 'جمع', ' وإعداد', ':', 'د', '.', 'راشد', ' الدويش']
part_speech = ['NOUN', 'NOUN', 'NOUN', 'NOUN', 'NOUN', 'PUNCT', 'NUM', 'NOUN', 'PUNCT', 'NOUN', 'NOUN', 'PUNCT', 'ADP', 'PUNCT', 'NOUN', 'NOUN']

m = {}

# For each of the vocabulary items in the Spanish list
for w1 in word: 
    if w1 not in m: 
        m[w1] = {}
    # For each of the vocabulary items in the English list
    for w2 in part_speech:
        m[w1][w2] = 0

print('\t' + '\t'.join(eng))
for w1 in m:
        print('%s\t' % (w1), end='')
        for w2 in m[w1]:
                print('%d\t' % (m[w1][w2]), end='')
        print('')



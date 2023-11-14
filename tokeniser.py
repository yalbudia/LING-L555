import sys

sentence_counter = 0  # a variable for sorting sentences
line = sys.stdin.readline() # a variable for sorting sentences
while line:
	if "" == line.strip():
# Here I indednted the below line in order to loop the code to the end of text
		line = sys.stdin.readline()
		continue
	print('# sent_id = ', sentence_counter)
	print('# text = ', line.strip())
# Here i print the sentences with deleting empty lines using line.strip() 
	token_counter = 0
	line_with_spaces=line
	line_with_spaces=line_with_spaces.replace(')', ' )')
	line_with_spaces=line_with_spaces.replace('(', '( ')
	line_with_spaces=line_with_spaces.replace('(', '( ')
	line_with_spaces=line_with_spaces.replace('.', ' .')
	line_with_spaces=line_with_spaces.replace('),', ')')
	line_with_spaces=line_with_spaces.replace('-', '- ')
	line_with_spaces=line_with_spaces.replace('_', ' _')
	line_with_spaces=line_with_spaces.replace('،', ' ،')
	line_with_spaces=line_with_spaces.replace('؟', ' ؟')
	line_with_spaces=line_with_spaces.replace('!', ' !')
	line_with_spaces=line_with_spaces.replace(',', ' ,')
	line_with_spaces=line_with_spaces.replace('?', ' ?')
	line_with_spaces=line_with_spaces.replace('=', ' =')
	line_with_spaces=line_with_spaces.replace('%', ' %')
	line_with_spaces=line_with_spaces.replace('*', ' *')
	line_with_spaces=line_with_spaces.replace('-', ' -')
	line_with_spaces=line_with_spaces.replace(':', ' :')
#I need to add function here to delete the empty lines
	tokens=line_with_spaces.split()
	for s in tokens:
		if "" ==  s.strip():
			continue
		print(token_counter, '\t', s, '\t_\t_\t_\t_\t_\t_\t_\t_')
		token_counter=token_counter+1
		sentence_counter=sentence_counter+1
	line = sys.stdin.readline()
	print('\n')
#I need to write if statement to delete  white spaces and empty line like if the ..  "" then continue .

#print(a)



#import sys

#sentence_counter=0
#line=sys.stdin.readline()
#while line:
#        print(sentence_counter)
#        print(line)

#        token_counter=0
#        tokens=line.split(' ')
#        for s in tokens:
#                print(token_counter, s)
#                token_counter=token_counter+1

#        sentence_counter=sentence_counter+1
#        line=sys.stdin.readline()






#code 1
#for token in li:
#Here is a code for printing numbers, tokens list  each one in each column
#import sys

#counter = 1
#tokens = ('I','see','it')
#for token in tokens:
#        print (counter, token)
#        counter = counter + 1

#code 2
#code that print numbers in one list from 1-10 and each number of the first list matches 10 number of the other list 
#import sys

#a = 1
#b = 2
#for i in range(0,10):
#        for j in range (0,10):
#                print(a,b)
#                b = b + 1
#        a = a + 1

#code 3
# code that print numbers in one list  from 1-10 and each number of the first list match 10 numbers of the other lis

#import sys

#a = 1
#b = 1
#for i in range(0,3):
#        b=1
#        for j in range (0,3):
#                print(a,b)
#                b = b + 1
#        a = a + 1

#Hint: the variables to be used are b=1, b=b+1, a=1, a=a+1 in order to produce 1 1, 1 2, 1 3, 2 1,2 2,2 3, ..






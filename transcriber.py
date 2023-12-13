import sys

vocab = {} # dict to store frequency list

# Next step to make the code read from the tsv file and stort it to dict file (any name)
# for each line in file:
# make a row
# add the pair to a dictionary

# print out the dictionary
table = {}
fd = open('table.tsv', 'r')

for line in fd.readlines():
# here I make a row
	row = line.strip('\n').split('\t')
# here I add the pair to a dictionary
	table[row[0]]=row[1]
# Here  I add a dictionary by looking to the code in syllable K Value

print(table)


# for each of the lines of input
for line in sys.stdin.readlines(): 
    # strip any excess newlines
	line = line.strip('\n')
    # if there is no tab character, skip the line
	if '\t' not in line:
		print(line)
		continue
    # make a list of the cells in the row
	row = line.split('\t')
    # if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
    # the form is the value of the second cell
	form = row[1]

# Here I assign a value of the tenth column to a form
	row[9]= form
	print('\t'.join(row))


# Her I write a for loop to replece string in Form with Value in Table.tsv
# Be careful not to iterate in form, iterates in table
for line in fd.readlines():
	table = table.replace('form','table.tsv')
	print(form,table)

# Here I assign a value of the tenth column to a form
	row[9]= form
	print('\t'.join(row))

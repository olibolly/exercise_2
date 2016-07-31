import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv[1])

#input_word = str(sys.argv[1])
#print input_word
input_string = "SELECT word, sum(count) as sum_count from tweetwordcount where word = %s group by word" % str(sys.argv[1])
print(input_string)
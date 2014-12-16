import sys
import json


def readnprint(afinnfile):
	#afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	    scores[term] = int(score)  # Convert the score to an integer.

	return scores

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #print readnprint()our
    scores = readnprint(sent_file)
    ls  = tweet_file.readlines()
    #ljson = json.loads(ls[100])
    #if len(ljson.keys())>1:
    #	print ljson['text'].encode('utf-8').split()
    #print scores
    for l in ls:
    	ljson = json.loads(l)
    	if len(ljson.keys())>1:
    		tweetwords = ljson['text'].encode('utf-8').split()
    		ss = 0
    		for w in tweetwords:
    			if w in scores.keys():
    				ss=ss+scores[w]
    		if ss != 0: 
    			print ss

    
    #lines(sent_file)
    #lines(tweet_file)
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()

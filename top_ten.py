import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    ls  = tweet_file.readlines()
    tophashtags={}
    #ljson = json.loads(ls[1900])
    #if len(ljson.keys())>1:
    #	print ljson['entities']['hashtags']#.encode('utf-8')
    
    for l in ls:
    	ljson = json.loads(l)
    	if len(ljson.keys())>1:
    		ht = ljson['entities']['hashtags']
    		if len(ht)>0:
    			if ht[0]['text'].encode('utf-8') in tophashtags:
    				tophashtags[ht[0]['text'].encode('utf-8')]+=1
    			else:
    				tophashtags[ht[0]['text'].encode('utf-8')]=1

    sortedlist = sorted(tophashtags, key= tophashtags.get, reverse=True)
    for i in xrange(10):
    	print sortedlist[i], tophashtags[sortedlist[i]]
    tweet_file.close()


if __name__ == '__main__':
    main()

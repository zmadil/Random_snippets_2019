
#Program to execute pretty print feature

import pprint
message= 'It was a nice Bright sunny Day'

count={} #Dictionary so setdafault method can execute

for i in message:
	count.setdefault(i,0)
	count[i]=count[i]+1

pprint.pprint(count)


import sys
import os

sys.path.insert(0, ".") #add our parent dir for secret.py and stream.py

import stream # we expect 2 id's 'user_id' and event tag
	      # user_id = "USER_ID_ON_FLICKR"
	      # event_tag = "tag to seach flickr for. 
import json

if os.path.isdir(stream.event_data_dir) == False:
	print "failsauce. Is not a dir!" + stream.event_data_dir
	exit (-1)

for x in os.listdir(stream.event_data_dir) :
	if x.endswith(".json"):
		print"=== " +  x + " ===="	
		x = os.path.join(stream.event_data_dir, x)
		#print x	
		with open(x) as fh:
			data = fh.read()
			data_dict = json.loads(data)
			print data_dict
		
		print"=== End: " +  x + " ===="	

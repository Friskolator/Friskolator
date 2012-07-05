
import secret # import local secret.py file containing keys.
	      # we expect 2 values in secret.py 
	      # api_key = "XXXX" #< your flickr api key
	      # api_secret = "YYYY" #< your flickr api secret

import stream # we expect 2 id's 'user_id' and event tag
	      # user_id = "USER_ID_ON_FLICKR"
	      # event_tag = "tag to seach flickr for. 

import flickrapi


flickr = flickrapi.FlickrAPI(secret.api_key)

filter_tags = [stream.event_tag, "friskolator"] # so we don't get general event tags

for photo in flickr.walk(tag_mode="and",tags=filter_tags):
    print photo.get('title')




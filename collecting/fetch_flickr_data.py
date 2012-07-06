
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
    print dir(photo)	
    id = photo.get('id')
    print id 
    #xmlnode = flickr.photos_getInfo(photo_id=id, format='xmlnode')
    etree = flickr.photos_getInfo(photo_id=id)
    for node in etree.iter():
	#print node.tag, node.attrib
	if node.tag == 'note':
		#print node.attrib
		id = node.attrib['id']
		text= node.text
		x,y = node.attrib['x'], node.attrib['y']
		w,h = node.attrib['w'], node.attrib['h']
		#print "note %s at %s %s %s %s " % ( text, x, y, w, h)
	info = stream.template_frisk.copy()
	photo_url = "http://www.flickr.com/photos/friskolator/" + id  + "/"	
	info['img'] = photo_url
	print info

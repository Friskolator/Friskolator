
### Friskolator! 

This is an open source opt-in little-brother data/privacy project.  We ask you to dump/share/show as much of your gear as you want, and we take a photo of it.  Then we process the photo, collect some (again, opt-in 'as much as you want' metada from you, and get it on the net.

After we have scads of amazingly amazing data, we'll crowdsource some stats and analytics on it. 

	collecting	- A directory of tools for pulling data from flickr into our local flat-file DB
	desktop		- Tools for having users input data on-site at a Friskolator station
	processing	- Directory of tools for converting flat-file DB data into graphs, infographics, etc
	
	collecting/secret.py	- Your custom 'secrets' file, containing flickr API keys, and other seekret host data
	stream.py	- Settings for a specific event's data stream.  Includes flickr, local db directory, and other shareable settings 
	data_template.py - Template dictionaries for data objects using by this library

### Running friskolator
#### Setting up
 Edit secret.py to contain your flickr API key data. 
 Edit stream.py to contain tag and event info, as well as your flatfile location
#### Collecting data from Flickr
 Setup virtualenv (go into collecting, and run setup.sh) and then start the virtualenv via '. /virtualenv/bin/activate'. Then return to the root directory, and collect the images and their tags from flickr by running 'python collecting/fetch_flickr_data.py ' to collect the data
and push it to your flat file location

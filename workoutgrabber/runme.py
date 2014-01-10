#-*- coding: utf-8 -*-
#!/usr/bin/env python2.7
from lxml import html
from StringIO import StringIO
from urlparse import urlparse
import requests
import urllib





##Requst workouts page: Overview
page = requests.get('http://neilarey.com/workouts.html')
tree = html.fromstring(page.text)

#links to articles
links = tree.xpath('//*/article/div/header/h2/a/@href')
#print 'links', links
print len(links)

for link in links:
	#print link
	#for each workout do this download stuff
	workout = requests.get(('http://neilarey.com%s')% link)
	workouttree = html.fromstring(workout.text)
	string1 = '/workouts/'
	string2 = ".html"
	picname = link
	picname = picname.replace(string1, "")
	picname = picname.replace(string2, "")
	print picname
	#links to images
	linkpic = workouttree.xpath('//*/p/img/@src')
	if len(linkpic) == 0:
		linkpic = workouttree.xpath('//*/p/strong/img/@src')
	print 'linkpic', linkpic
	print len(linkpic)
	if len(linkpic) == 1:
		print linkpic[0]
		image = urllib.urlopen(linkpic[0]).read()
		outfile = open('{0}.png'.format(picname),'wb')
		outfile.write(image)
		outfile.close()	
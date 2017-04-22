import urllib2
import optparse
from bs4 import BeautifulSoup
from urlparse import urlsplit
from os.path import basename

def findImages(url):
	print '[+] Recherche d\'image sur: "' + url + '"'
	urlContent = urllib2.urlopen(url).read()
	sp = BeautifulSoup(urlContent, "html.parser")
	return sp.find_all("img")

def downloadImage(imgTag):
	try:
		print "[+] Telechargement de l'image...."
		imgSrc = imgTag['src']
		imgContent = urllib2.urlopen(imgSrc).read()
		imgFileName = basename(urlsplit(imgSrc)[2])
		imgFile = open(imgFileName, "wb")
		imgFile.write(imgContent)
		imgFile.close()
		return imgFileName
	except:
		return ''

def main():
	parser = optparse.OptionParser('usageprog-u <url>')
	parser.add_option('-u', dest='url', type='string', help="Donner un bon url")
	(option, args) = parser.parse_args()
	url = option.url
	if url == None:
		print parser.usage
	else:
		imgTags = findImages(url)
		for img in imgTags:
			imgFileName = downloadImage(img)


if __name__ == '__main__':
	main()
	
			


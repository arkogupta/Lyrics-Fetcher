from bs4 import  BeautifulSoup
import re
import urllib2
import urllib
import sys


def GetLyrics(url,filename,artist):
	soup = BeautifulSoup(urllib2.urlopen(url))
	
	a = soup.find('div' , class_ = 'ringtone')
	
	b = a.next_siblings   #returns a list of all the elements which are on same level as element a

	for sib in b:
		if type(sib)!= str :
			tmp = str(sib)
			if tmp[0:5]=='<div>': #the first div tag after ringtone contains the lyrics
				lyrics = sib
				break	
			
	#print lyrics
    
	f = open(filename , 'w')
	f.write(filename[:-4].upper()+'('+ artist+')\n\n')    

     
	for string in lyrics.strings:
		string = string.encode('utf-8') #in python2 we cant print unicode strings which cant be converted to ascii
		f.write(string)

	f.close()

def RemoveSpaces(A):
	B = ''
	for i in xrange(0,len(A)):
		if(A[i]==' '):
			continue
		else:
			B+=A[i]
	return B

def main():

	

	
	try:
		artist = raw_input('Enter name of artist : ')
		artist = RemoveSpaces(artist.lower())
		song_name = raw_input('Enter name of song : ')
		song_name = RemoveSpaces(song_name.lower())
		url = 'http://www.azlyrics.com/lyrics/'+artist + '/'+ song_name+'.html
		urllib2.urlopen(url)
	except urllib2.HTTPError as err:
		if err.code == 404:
			print 'Please check the name of the artist and the song.'
			print 'The url',url,'does not exist'
		elif err.code == 403:
			print 'Access Denied!'
		else:
			print 'The following error occured : err',err.code
		
	print 'Fetching lyrics for song "' + song_name + ' "by '+ artist + '...' 
	GetLyrics(url,song_name+'.txt',artist)
	print 'Lyrics saved in file "'+ song_name+'.txt" '


if __name__ == '__main__':
  main()

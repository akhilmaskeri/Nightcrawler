from __future__ import print_function
import requests
import os,sys
from colorama import Fore,Back,Style
from bs4 import BeautifulSoup

class song:
	def __init__(self,num,title,artist,weeks):
		self.num = num
		self.setTitle(title)
		self.setArtist(artist)
		self.setWeeks(weeks)

	def setTitle(self,title):
		self.title = title

	def setArtist(self,artist):
		self.artist = artist

	def setWeeks(self,weeks):
		self.weeks = weeks

	def getWeeks(self):
		return self.weeks

	def getTitle(self):
		return self.title

	def getArtist(self):
		return self.artist

	def getNum(self):
		return int(self.num)

if '--help' in sys.argv:
    f = open("README.md")
    print (f.read())
    exit()

url="http://billboard.com/charts/hot-100"
sc=""
try:
	sc = requests.get(url)
except Exception as ex:
    print ("check the internet connection")
    exit(0)

args=[]
start=0
end=10

num = False
title=False
artist=False
woc = False
explicit = False

soup = BeautifulSoup(sc.text,'lxml')

li = soup.findAll('h2',{'class':'chart-row__song'})
art = soup.findAll('a',{'class':'chart-row__artist'})
woc = soup.findAll('span',{'class':'chart-row__value'})
s=[]

for i in range(len(art)):
	s.append(song(i+1,li[i].text,art[i].text.strip(),woc[i].text))
def byWeeks():
	s.sort(key=lambda s: s.getWeeks(),reverse=True)

def byRank():
	s.sort(key=lambda s:s.getNum())

def display(start=0,end=len(s)):
	for e in range(start,end):
		line=""
		if not explicit:
			line = Fore.RED+str(s[e].getNum())+"]  "+Style.RESET_ALL+s[e].getTitle()+Fore.YELLOW+"  ["+s[e].getArtist()+"]  "+Fore.CYAN+str(s[e].getWeeks())+" woc"+Style.RESET_ALL
		else:
			line=[]
			if num:
				line.append(Fore.RED+((str(s[e].getNum()) if s[e].getNum()>9 else ('0'+str(s[e].getNum())))+' ]'))
			if title:
				line.append(Style.RESET_ALL+s[e].getTitle())
			if artist:
				line.append(Fore.YELLOW+s[e].getArtist())
			if 'w' in sys.argv:
				line.append(Fore.CYAN+str(s[e].getWeeks())+" woc")
			line =  " ".join(line)
		line+=Style.RESET_ALL
		print (line)

for arg in sys.argv:
	if arg != sys.argv[0]:
		if arg.isdigit():
			if int(arg) >99:
				print ("invalid argument")
				exit(0)
			else:
				end = int(arg)
		elif arg == '-sw':
			byWeeks()
		elif arg == '-sr':
			byRank()
		elif arg == '-t':
			explicit = True
			title=True
		elif arg == '-n':
			explicit = True
			num = True
		elif arg == '-a':
			explicit = True
			artist = True
		elif arg == '-w':
			explict = True
			woc = True
		elif '-' in arg:
			if len(arg.split('-'))!=2:
				print ("invalid argument")
				exit(0)
			else:
                                start =0
                                if arg.split('-')[0]!='':
                                    start = int(arg.split('-')[0]-1)
                                end = int(arg.split('-')[1])
		else:
			printf("%d * %d = %d\n",c[j],c[i-j-1],c[j]*c[i-j-1]);
			print ("invlid argument")
			exit(0)

display(start,end)

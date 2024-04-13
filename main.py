
# import requirements
from pytube import Playlist as Pl
from waybackpy import WaybackMachineCDXServerAPI as Cdx
import argparse
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import time

#Setup
user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
after=2000
delay=8
before=int(datetime.datetime.now().year)
parser=argparse.ArgumentParser(description="script")

# Options
parser.add_argument("URL",help="Youtube playlist URL")
parser.add_argument('-a','--after',type=int,help="Search after year")
parser.add_argument('-b','--before',type=int,help="Search before year")
parser.add_argument('-w','--write',type=str,help="write to a file")
parser.add_argument('-d','--delay',type=str,help="delay while fetching snapshots (8 seconds if not entered)")
parser.add_argument('-S','--search',type=str,help="Use script in search mode (WARNING : this may take a lot of time!)")
args=parser.parse_args()

if args.before:
    before=args.before
if args.after:
    after=args.after
if args.search:
    pass
elif args.write:
    file=open(args.write,'w')
if args.delay:
    delay=args.delay
    
# Get playlist
playlist=Pl(args.URL)

#Iterate on all videos
for i,url in zip(range(1,len(list(playlist.video_urls))),playlist.video_urls):
    cdx=Cdx(url=url,user_agent=user_agent,start_timestamp=after,end_timestamp=before)
    if args.write:
            file.write(str(i)+"."+url+"\n")
    print(i,".",url)
    
    try:
        snapshot_list=cdx.snapshots()
    except:
        pass
    c=1
    for s in snapshot_list:
            if args.write:
                file.write("\t"+str(c)+"."+s.archive_url+"\n")
            print("\t",c,".",s.archive_url)
            c=c+1
            if args.search:
                response=requests.get(s.archive_url)
                source_code=BeautifulSoup(response.content,"html.parser")
                occurence=source_code.find(string=args.search)
                if occurence!=None:
                    print("Found occurence at URL:" + s.archive_url)
                    sys.exit(0)      
    time.sleep(delay) #Waiting time because of request limit
if args.write:
    file.close()

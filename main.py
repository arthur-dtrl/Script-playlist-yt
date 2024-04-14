
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
after=1999
delay=8
first_vid=1
before=int(datetime.datetime.now().year)
parser=argparse.ArgumentParser(description="script")

# Options
parser.add_argument("URL",help="Youtube playlist URL")
parser.add_argument('-a','--after',type=int,help="Search after year")
parser.add_argument('-b','--before',type=int,help="Search before year")
parser.add_argument('-w','--write',type=str,help="write to a file")
parser.add_argument('-d','--delay',type=str,help="delay while fetching snapshots (8 seconds if not entered)")
parser.add_argument('-s','--skip',type=int,help="skip to the nth video ( useful if you had an error )")
parser.add_argument('-S','--search',type=str,help="Find string in archive (WARNING : this may take a lot of time!)")
args=parser.parse_args()

if args.before:
    before=args.before
if args.after:
    after=args.after
if args.skip:
    first_vid=args.skip
if args.search:
    pass
elif args.write:
    file=open(args.write,'w')
if args.delay:
    delay=args.delay
    
# Get playlist
playlist=Pl(args.URL)

#Iterate on all videos
URLs_length=len(list(playlist.video_urls))
for i,url in zip(range(first_vid,URLs_length),playlist.video_urls[first_vid-1:URLs_length-1]):
    if args.write:
            file.write(str(i)+"."+url+"\n")
    print(i,".",url)
    cdx=Cdx(url=url,user_agent=user_agent,start_timestamp=after,end_timestamp=before)
    snapshot_list=cdx.snapshots()
    c=1
    try:
        for s in snapshot_list:
                if args.write:
                    file.write("\t"+str(c)+"."+s.archive_url+"\n")
                print("\t",c,".",s.archive_url)
                c=c+1
                if args.search:
                    time.sleep(6)
                    try:
                        response=requests.get(s.archive_url)
                    except:
                        print("Couldn't access archive")
                        pass
                    source_code=str(BeautifulSoup(response.content,"html.parser").prettify())
                    if args.search in source_code:
                            print("Found occurence at URL:" + s.archive_url)
                            sys.exit(0)      
                    
        time.sleep(delay) #Waiting time because of request limit
    except:
        print("Couldn't access Wayback Machine for this URL")
if args.write:
    file.close()


# import requirements
from pytube import Playlist as Pl
from waybackpy import WaybackMachineCDXServerAPI as Cdx
import argparse
import datetime
import time

#Setup
user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
after=2000
before=int(datetime.datetime.now().year)
parser=argparse.ArgumentParser(description="script")

# Options
parser.add_argument("URL",help="Youtube playlist URL")
parser.add_argument('-b','--before',type=int,help="Search before year")
parser.add_argument('-a','--after',type=int,help="Search after year")
parser.add_argument('-w','--write',type=str,help="write to a file")
args=parser.parse_args()  

if args.before:
    before=args.before
if args.after:
    after=args.after
if args.write:
    file=open(args.write,'w')
    
# Get playlist
playlist=Pl(args.URL)

# Search function
def searchWM(URL):
    
    # URL search on Wayback Machine
    
    
    return snapshots


for i,url in zip(range(1,len(list(playlist.video_urls))),playlist.video_urls):
    cdx=Cdx(url=url,user_agent=user_agent,start_timestamp=before,end_timestamp=after)
    if args.write:
            file.write(str(i))
            file.write(cdx.url)
            file.write("\n")
    print(i,cdx.url)
    snapshots=cdx.snapshots()
    for j,s in zip(range(1,len(list(snapshots))),snapshots):
        if args.write:
            file.write(str(j))
            file.write(s.archive_url)
            file.write("\n")
        print("\t",j,s.archive_url)

if args.write:
    file.close()



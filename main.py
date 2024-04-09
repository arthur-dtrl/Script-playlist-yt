
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
parser.add_argument('-a','--after',type=int,help="Search after year")
parser.add_argument('-b','--before',type=int,help="Search before year")
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
    time.sleep(8) #Waiting time because of request limit
if args.write:
    file.close()

from pytube import Channel 
import sys
 
 
def main():
    url = 'https://www.youtube.com/c/' + str(sys.argv[1]) + '/videos'
    c = Channel(url)
    for url in c.video_urls: 
        print(url) 
 
 
if __name__ == '__main__': 
    main() 

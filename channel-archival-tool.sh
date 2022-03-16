#!/bin/sh

echo YouTube Channel:
read yt_channel

python3 url-fetch.py $yt_channel > urls.txt

while IFS="" read -r p || [ -n "$p" ]
do
  youtube-dl "$p"
done < urls.txt

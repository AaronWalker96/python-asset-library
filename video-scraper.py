from pytube import YouTube
import sys 

url = sys.argv[len(sys.argv) - 2]
fileName = sys.argv[len(sys.argv) - 1]

print("downloading " + fileName + " from " + url)

YouTube(url).streams.first().download(fileName)
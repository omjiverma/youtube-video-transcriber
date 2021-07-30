from youtube_transcript_api import YouTubeTranscriptApi
url = input('Enter Youtube Video URL : ')
id = (url.split('='))[1]
transcript=YouTubeTranscriptApi.get_transcript(id)
f = open("Text.txt", 'w',encoding="utf-8")
for i in transcript:
    f.write(i['text'],)
f.close()

print('Task Over')
print('Please Check The Output Text File')




# https://www.youtube.com/watch?v=aDG1T0kJnd4

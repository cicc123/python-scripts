import re
import requests
def get_songid():
 """获取音乐的songid"""
 url = 'http://music.taihe.com/artist/7994'
 response = requests.get(url=url)
 html = response.text
# print ("%s" % html)
 sids = re.findall(r'href="/song/(\d+)"', html)
# print(sids)
 return sids
def get_music_url(songid):
 """获取下载链接"""
 api_url = f'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid={songid}&from=web'
# response = requests.get(api_url.format(songid=songid))
 response = requests.get(api_url.format(songid=songid))
 data = response.json()
 #print(data)
 try:
  music_name = data['songinfo']['title']
  music_url = data['bitrate']['file_link']
 # print(music_url)
  #print(music_name)
  if music_name is None or music_url is None:
   return 1,1
  return music_name, music_url #if music_name is not null and music_url is not null
 # return 0
 except Exception as e:
  #print(e)
  pass
def download_music(music_name, music_url):
 """下载音乐"""
 response = requests.get(music_url)
 content = response.content
 save_file(music_name+'.mp3', content)
def save_file(filename, content):
 """保存音乐"""
 with open(file=filename, mode="wb") as f:
   f.write(content)
if __name__ == "__main__":
 for song_id in get_songid():
   music_name, music_url = get_music_url(song_id)
  # print(get_music_url(song_id))
  # get_music_url(song_id)
  # download_music(music_name, music_url)
   #print("%s%s\n" %(music_name,music_url))
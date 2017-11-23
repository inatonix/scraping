import urllib.request
from urllib.parse import quote
import httplib2
import json
import os
import argparse

API_KEY = os.environ['IMG_API_KEY']
CUSTOM_SEARCH_ENGINE = os.environ['CUSTOM_SEARCH_ENGINE']

def getImageUrl(search_item, total_num):
 img_list = []
 i = 0
 while i < total_num:
  query_img = "https://www.googleapis.com/customsearch/v1?key=" + API_KEY + "&cx=" + CUSTOM_SEARCH_ENGINE + "&num=" + str(10 if(total_num-i)>10 else (total_num-i)) + "&start=" + str(i+1) + "&q=" + quote(search_item) + "&searchType=image"
  print (query_img)
  res = urllib.request.urlopen(query_img)
  data = json.loads(res.read().decode('utf-8'))
  for j in range(len(data["items"])):
   img_list.append(data["items"][j]["link"])
  i=i+10
 return img_list

def getImage(search_item, img_list):
 opener = urllib.request.build_opener()
 http = httplib2.Http(".cache")
 for i in range(len(img_list)):
  try:
   fn, ext = os.path.splitext(img_list[i])
   print(img_list[i])
   response, content = http.request(img_list[i])
   with open('./images/' + search_item+str(i)+ext, 'wb') as f:
    f.write(content)
  except:
   print("failed to download images.")
   continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "description goes here")
    parser.add_argument("-n", type=str, help = "help text goes here. This option is required", required=True)
    parser.add_argument("-c", type=int, help = "help text goes here. This option is required", required=True)

    arguments = parser.parse_args()

    os.mkdir('./images/')

    img_list = getImageUrl(arguments.n, arguments.c)
    print(img_list)
    getImage(arguments.n, img_list)

import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote
import json
import sys

def get_soup(id):
    url = "https://www.youtube.com/watch?v=" + id
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def scrap_author(soup) :
    return soup.find("span",itemprop="author").find("link",itemprop="name")["content"]

def scrap_title(soup) :
    return soup.find("meta",property="og:title")["content"]

def scrap_likes(soup) :
    reg = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data = json.loads(reg)
    
    likes_pos = data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["videoActions"]["menuRenderer"]["topLevelButtons"][0]["segmentedLikeDislikeButtonRenderer"]["likeButton"]["toggleButtonRenderer"]["defaultText"]["accessibility"]["accessibilityData"]["label"]
    return likes_pos.split(' ')[0].replace(',','')

def scrap_description(soup) :
    reg = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data = json.loads(reg)
    try:
        description = ""
        text = data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][1]["videoSecondaryInfoRenderer"]["description"]["runs"] 
        for l in text:
            description += l["text"].replace('\n','\\n')      
    except:
        description = "No description available"
    return description

def scrap_links(soup) :
    reg = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data = json.loads(reg)
    links = []
    try :
        text = data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][1]["videoSecondaryInfoRenderer"]["description"]["runs"] 
        for l in text:
            if "navigationEndpoint" in l.keys():
                l = l["navigationEndpoint"]
                if "urlEndpoint" in l:
                    tmp_link = l["urlEndpoint"]["url"]
                    if "redirect" in tmp_link:
                        links.append(unquote(tmp_link.split("&q=")[1].split("&v=")[0]))
                    else:
                        links.append(unquote(tmp_link))
                elif "commandMetadata" in l:
                    tmp_link = l["commandMetadata"]["webCommandMetadata"]["url"]
                    links.append(unquote("https://youtube.com"+tmp_link))
    except :
       pass
    return links


def parse_video(id):
    res = {}
    soup = get_soup(id)
    res["title"] = scrap_title(soup)
    res["author"] = scrap_author(soup)
    res["likes"] = scrap_likes(soup)
    res["description"] = scrap_description(soup)
    res["links"] = scrap_links(soup)
    res["id"] = id

    return res



import pandas as pd
from bs4.element import Comment, Tag

import requests
from bs4 import BeautifulSoup, StopParsing
# url="https://github.com/topics"
# r=requests.get(url)
# print(r.status_code)
# print(r.text)
# htmlcontent=r.content
# page_content=r.text
# print(htmlcontent)
# with open('simple.html','w') as f:
#     f.write(str(len(page_content)))
    
# with open('webpage.html','w',encoding="utf-8") as f:
#     f.write(page_content)

# soup=BeautifulSoup(htmlcontent,'html.parser')
# empty_title=[];
# empty_desc=[];
# for title in soup.find_all('p',class_="f3 lh-condensed mb-0 mt-1 Link--primary")[:22]:
    # print(title.get_text())
    # empty_title.append(title.get_text())
# print(empty_title)
# for desc in soup.find_all('p',class_="f5 color-fg-muted mb-0 mt-1")[:22]:
    # print(desc.text)
    # empty_desc.append(desc.text.strip())
# print(empty_desc)
# print(soup.find_all('p',class_="f3 lh-condensed mb-0 mt-1 Link--primary")[0].get_text())
# print(soup.find_all('p',class_="f5 color-fg-muted mb-0 mt-1")[:5])

# print(soup.find("template",id="site-details-dialog"))
# print(soup.prettify)


# get all the paragraph from the page
# paras=soup.find_all('p')
# print(type(paras))
# print(paras)
# para=soup.find_all('a')
#finding element with tag
# print(soup.find('p')['class'][0])
# finding element with classname
# print(soup.find_all("p",class_="mt-2"))
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the links with attributes
# anchor =soup.find_all('a',class_="no-underline flex-grow-0")
# nonrepeatedlinks=[]
# for link in anchor[:22]:
#     # if(link.get("href")!="#"):
#         nonrepeatedlinks.append("https://www.github.com"+link["href"])
    

# print(nonrepeatedlinks)
# print(len(nonrepeatedlinks))


# Making Dictionary
# topics_excel={
#     "title":empty_title,
#     "description":empty_desc,
#     "url":nonrepeatedlinks
# }
# topics_dataframe=pd.DataFrame(topics_excel)
# print(topics_excel)

# topics_dataframe.to_csv("first.csv",index=None)

#peeping over the 3d topic of github

url1="https://github.com/topics/ajax"
response=requests.get(url1)
# threed_content=response.content
# print(response.status_code)

with open('ajaxd.html','w',encoding="utf-8") as f:
    f.write(response.text)

soup=BeautifulSoup(response.text,'html.parser')
# topic_title=soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[0].find_all('a')[0].text.strip()
# topic_url=url1+soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[0].find_all('a')[0]['href']
# topic_data=soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[0].find_all('a')[1].text.strip()
# topic_stars=soup.find_all('span',class_="Counter js-social-count")[0].text.strip()

# print(soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[0].find_all('a')[0].text.strip())
# print(soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[0].find_all('a')[0]['href'])
# print(topic_url)

# print(topic_stars)
# print(soup.find_all('h3'))
empty_topic_title=[]
empty_topic_url=[]
empty_topic_data=[]
empty_topic_stars=[]
for i in range(0,30):
    empty_topic_title.append(soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[i].find_all('a')[0].text.strip())
    empty_topic_url.append(url1+soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[i].find_all('a')[0]['href'])
    empty_topic_data.append(soup.find_all('h3',class_="f3 color-fg-muted text-normal lh-condensed")[i].find_all('a')[1].text.strip())
    # topic_stars=int(float(topic_stars.strip()[:-1])*1000)
    empty_topic_stars.append(soup.find_all('span',class_="Counter js-social-count")[i].text.strip())
    
print(empty_topic_title)
print(empty_topic_url)
print(empty_topic_data)
print(empty_topic_stars)

topics_excel={
    "title":empty_topic_title,
    "creator":empty_topic_data,
    "url":empty_topic_url,
    "Totalstars":empty_topic_stars
}

topics_dataframe=pd.DataFrame(topics_excel)
print(topics_excel)

topics_dataframe.to_csv("ajax.csv")





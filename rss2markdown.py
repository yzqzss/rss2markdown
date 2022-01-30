import feedparser
import html2text
import os

rss_url = input("Input rss URL or File_Address: ")
c_md = input("Convert to markdown format? \n(y as default) y/n: ")
c_name = input('Convert as Windows friendly file name?\n(n as default) y/n: ')

feed = feedparser.parse(rss_url)
items = feed["items"]
for item in items:
    time = item[ "published_parsed" ]
    format_time = str(time.tm_year)+'/'+str(time.tm_mon)+'/'+str(time.tm_mday)+'/ '+str(time.tm_hour)+':'+str(time.tm_min)+':'+str(time.tm_sec)
    title = item[ "title" ]

    print('Pocessing: ['+title+']…')

    if c_name == 'y':
        fileName = str(time.tm_year) + '-' + str(time.tm_mon) + '-' + str(time.tm_mday) + ':' + title + '.md'
        fileName = "./output/"+fileName.replace('/', '_').replace('\\', '_').replace(':', '：').replace('*', '×').replace('?', '？').replace('"', '\'\'').replace('<', '[').replace('>', ']').replace('|', 'l')
    else:
        fileName = str(time.tm_year) + '-' + str(time.tm_mon) + '-' + str(time.tm_mday) + ': ' + title + '.md'
        fileName = "./output/"+fileName.replace('/', '_')

    if not os.path.exists("output"):
					os.makedirs("output")

    f = open(fileName,'w')
    value = item["content"][0]['value']
    f.write('---\nlayout: post\ntitle: '+title+'\ndate: '+format_time+'\nupdated: '+format_time)
    f.write('''
status: publish
published: true
type: post
---

''')
    if c_md == 'n':
        f.write(value)
    else:
        value = html2text.html2text(value)
        f.write(value)
print('Done! please check out ./output')

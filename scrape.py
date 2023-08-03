#!/usr/bin/env python3

import hashlib
import os.path
import feedparser

feedsFile = open('feeds.txt', 'r')
feeds = [x.strip('\n') for x in feedsFile]
feedsFile.close()

dataFile = open('data.txt', 'r')
lines = [x.strip('\n') for x in dataFile]
dataFile.close()

keyFile = open('../../key.txt', 'r')
key = keyFile.read().strip('\n')
keyFile.close()

newLines = []
for feed in feeds:
    print(feed)
    newsfeed = feedparser.parse(feed)
    for entry in newsfeed.entries:
        guidText = feed+entry.link
        guid = hashlib.md5(guidText.encode('utf-8')).hexdigest()
        print(entry.title)

        if not os.path.isfile('articles/'+guid+'.html'):
            try:
                articleHtml = '<!DOCTYPE html><html lang="en"><head><title>'+entry.title+'</title><style type="text/css">body{font-size:20px;}</style></head><body>'
                articleHtml += '<h1>'+entry.title+'</h1>'
                articleHtml += '<p><strong>Source: <a href="' + entry.link + '" target="_blank">' + entry.link + '</a></strong></p>'
                articleHtml += '<p>[<a href="../read.php?key='+key+'&id='+guid+'">mark read</a>]</p>'
                if hasattr(entry,'content'):
                    articleHtml += entry.content[0].value
                else:
                    articleHtml += entry.summary
                articleHtml += '<p>[<a href="../read.php?key='+key+'&id='+guid+'">mark read</a>]</p>'
                articleHtml += '</body></html>'
                articleFile = open('articles/' + guid + '.html', 'w')
                articleFile.write(articleHtml)
                articleFile.close()
                ln = 'U|' + guid + '|' + entry.title
                newLines.append(ln)
            except Exception as e:
                print("ERR "+ entry.id + ":")
                print(repr(e))
    print('')

if len(newLines) > 0:
    dataFile = open('data.txt', 'a')
    d = '\n'
    d += '\n'.join(newLines)
    dataFile.write(d)
    dataFile.close()

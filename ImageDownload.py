import urllib
import urllib2
mn = 0
url = "http://mm.taobao.com/json/request_top_list.htm?type=2&page="
murl = url+str(5)
up = urllib2.urlopen(murl)
mcont = up.read()
mhead = 'a href="http://mm.taobao.com'
head = mcont.find(mhead)
tail = mcont.find("target",head)
purl = mcont[head+8:tail-2]
li = []
li.append(purl)
while head != -1:
    head = mcont.find(mhead,tail)
    if head != -1:
        tail = mcont.find("target",head)
        purl = mcont[head+8:tail-2]
        if "photo" not in purl:
            li.append(purl)
           
i = 0       
while i < 2:
    print 'purl--->',i,li[i]
    up1 = urllib2.urlopen(li[i])
    mmcont = up1.read()
    mmhead = '''taobaocdn.com/imgextra'''
    mmtail = '''jpg'''
    pos = 0
    k = 0
    while k <= mmcont.count(mmhead)/2-1:
        mmpos = mmcont.find(mmhead,pos)
        mmtailpos = mmcont.find(mmtail,mmpos)
        pos = mmtailpos
        mmurl=mmcont[mmpos-13:pos+3]
        urllib.urlretrieve(mmurl,"mm"+str(mn)+".jpg")
        mn += 1
        k+=1
    i+=1
    print '----------------------------------------'
print "Done"

'''
    while mmhead != -1:
        mmpos = mmcont.find(mmhead,mmtail)
        if mmpos != -1:
            mmtail = mmcont.find('jpg',mmpos)
            imgurl = mmcont[mmpos-13:mmpos+90]
            print imgurl
            urllib.urlretrieve(imgurl,"mm"+str(mn)+".jpg")
    print up1.read()
'''

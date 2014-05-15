import xml
import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime
from datetime import datetime, timedelta,date, time
#xmldoc = minidom.parse('twtmob_users_20140507.xml')
count = 0

#line = '<favmoviegenres>0x80Action/Adventure0x80Comedy0x80Drama</favmoviegenres>'
#line = ' <favmusicgenres>0x80Rap/Hip-Hop0x80R&amp;amp;B 0x80Soul0x80Pop0x80Rock/Alternative0x80Jazz/Experimental0x80Indie Rock0x80Punk Rock0x80Country0x80Dance</favmusicgenres>'

#line = '<favmoviegenres>0x80Action/Adventure0x80Comedy0x80Drama</favmoviegenres>'
#doc  = xml.etree.ElementTree.fromstring(line)
import xml.dom.minidom
count = 0
influencer = dict()
#twtMobInfluencers_last6mos_20140512
#twtmob_users_20140507
with open('twtMobInfluencers_last6-2mos_20140512.xml') as fp:
    for line in fp:
       #doc  = xml.dom.minidom.parseString(line)
       try :
         doc =xml.etree.ElementTree.fromstring(line)
         if 'twtmobuserid' in doc.tag:
            influencer.setdefault(doc.text,{})
            twtmobuserid = doc.text
         else :
            influencer[twtmobuserid].setdefault(doc.tag,[])
            influencer[twtmobuserid][doc.tag].append(doc.text)
       except :
         pass
#print('tweets rejected')
count = 0
female = 0
male = 0
partcount = 0
age_dict = dict();
ethnic_dict = dict();
print(len(influencer))
for twtmobuserid in influencer :
    if 'twitterfollowers' in influencer[twtmobuserid] :
        followers = influencer[twtmobuserid]['twitterfollowers']
        userstatus = influencer[twtmobuserid]['userstatus']
        gender = influencer[twtmobuserid]['sex']
        age = influencer[twtmobuserid]['age']
        ethnicity = ['None']
        if 'ethnicity' in influencer[twtmobuserid] :
            ethnicity = influencer[twtmobuserid]['ethnicity']
        if 'twitterAvgEngagementRate' in influencer[twtmobuserid] :
            engagerate = float(influencer[twtmobuserid]['twitterAvgEngagementRate'][0])
        else :
            engagerate = -1.0
        participated = 0

        if 'last_participated' in influencer[twtmobuserid] :
            participated = 1
            partcount +=1
            #date = influencer[twtmobuserid]['last_participated']
            #date2 = date[0].replace('T',' ')
            #date_str = datetime.strptime(date2,"%Y-%m-%d %H:%M:%S.%f")
#if 'particpationRate' in influencer[twtmobuserid] :

        #print(userstatus[0])
        #print(followers[0]) #and 'Active' in userstatus
        if int(followers[0]) > 5000  and participated is 1:
            username = influencer[twtmobuserid]['twitterusername']
            retweet_approx = int(followers[0])*engagerate
            
            print '"'+username[0]+'"'
            #float(engagerate)*5000.0>0.00000:
            #print(twtmobuserid,influencer[twtmobuserid]['twitterusername'],followers[0])
            if ethnicity[0] in ethnic_dict :
                ethnic_dict[ethnicity[0]] +=1
            else :
                ethnic_dict.setdefault(ethnicity[0])
                ethnic_dict[ethnicity[0]] = 1
            if age[0] in age_dict:
                age_dict[age[0]] +=1
            else :
                age_dict.setdefault(age[0])
                age_dict[age[0]] = 1
            if 'Female' in gender[0] :
                female +=1
            elif 'Male' in gender[0] :
                male +=1
            count +=1
print('total number of influeners > 5000',count)
print ('female',female,'male',male)
print 'age',age_dict
print partcount
#print 'ethinicty',ethnic_dict
    #print(count, 'bad line',line)
#tree = ET.parse('twtmob_users_20140507.xml')
#root = tree.getroot()

#print(root.tag)
#from xml.dom import minidom
#xmldoc = minidom.parse('twtmob_users_20140507.xml')

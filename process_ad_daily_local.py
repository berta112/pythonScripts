#from boto.s3.connection import S3Connection
#s3 = S3Connection()
#s3.get_bucket('faveme')
import boto
import sys, os
import json
import glob
from os import listdir
from os.path import isfile, join
import csv
from csv import DictWriter
    #from boto.s3.key import Key


def writeCSV(filename,hashtags,hash_list,tweet_list,tweet_data,lang_hist,gender_hist,location_hist):
   print('writing to csv file')
   time = tweet_data.get(tweet_data.keys()[0])
   time2 = time[2].split()
   date = (time2[1]+' '+time2[2]+' '+time2[3])
  
   writer = csv.writer(open(filename+'.csv', 'wb'))
   writer.writerow(['total ads',len(tweet_data),'total people',len(tweet_list),'day of week',time2[0],'date',date])
   writer.writerow(['hashtag','hashtag count','hash unique users','user id','Ad Count','user name','followers','following','favourite count','gender','language','user id','user name','time','language','language count','gender name','gender count','hash value'])

   sorted_hash = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
   sorted_tweeters = sorted(tweet_list.items(), key = lambda x: x[1], reverse=True)
  
   for k in range(0,len(hash_list)) :
     if (k < len(hashtags)) :
        str1 = sorted_hash[k][0].encode('utf-8') #hashtags.keys()[k].encode('utf-8')
        # val =  sorted_hash[k][1][0] #str(hashtags.get(hashtags.keys()[k],-1))
        str2 = sorted_hash[k][1][0]
        str2a = sorted_hash[k][1][1]
     else :
        str1 = ' '
        str2 = ' '
     if (k < len(tweet_list)) :
        str3 = sorted_tweeters[k][0] #tweet_list.keys()[k]
        # val = #tweet_list.get(tweet_list.keys()[k])
        str4 = sorted_tweeters[k][1][0] #val[0]
        str5 = sorted_tweeters[k][1][1]
        str6 = sorted_tweeters[k][1][2]
        str7 = sorted_tweeters[k][1][3]
        str8 = sorted_tweeters[k][1][4]
        str9 = sorted_tweeters[k][1][5]
        str10 = sorted_tweeters[k][1][6]
     else :
        str3 = ' '
        str4 = ' '
        str5 = ' '
        str6 = ' '
        str7 = ' '
        str8 = ' '
        str9 = ' '
        str10 = ' '
     if k < len(tweet_data) :
        val = tweet_data.get(tweet_data.keys()[k])
        str11 = val[0]
        str12 = val[1]
        time2 = val[2].split()
        str13 = time2[4]
     else :
        str11 = ' '
        str12 = ' '
        str13 = ' '
     if k < len(lang_hist) :
        val = lang_hist.get(lang_hist.keys()[k])
        str14 = lang_hist.keys()[k]
        str15 = lang_hist.get(lang_hist.keys()[k])
     else :
        str14 = ' '
        str15 = ' '
     if k < len(gender_hist):
        str16 = gender_hist.keys()[k]
        str17 = gender_hist.get(gender_hist.keys()[k])
     else :
        str16 = ' '
        str17 = ' '
     writer.writerow([str1,str2,str2a,str3,str4,str5,str6,str7,str8,str9,str10,str11,str12,str13,str14,str15,str16,str17,hash_list[k].encode('utf-8')])

def writeCSVpeople(filename,hashtags,hash_list,tweet_list,tweet_data,lang_hist,gender_hist) :
    print('writing to csv file')
    time = tweet_data.get(tweet_data.keys()[0])
    time2 = time[2].split()
    date = (time2[1]+' '+time2[2]+' '+time2[3])
    
    writer = csv.writer(open(filename+'people'+'.csv', 'wb'))
    writer.writerow(['total ads',len(tweet_data),'total people',len(tweet_list),'day of week',time2[0],'date',date])
    writer.writerow(['user id','Ad Count','user name','followers','following','favourite count','gender','language','user id','user name','time','language','language count','gender name','gender count'])
    
    sorted_hash = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    sorted_tweeters = sorted(tweet_list.items(), key = lambda x: x[1], reverse=True)
    
    for k in range(0,len(hash_list)) :
        if (k < len(tweet_list)) :
            str3 = sorted_tweeters[k][0] #tweet_list.keys()[k]
            # val = #tweet_list.get(tweet_list.keys()[k])
            str4 = sorted_tweeters[k][1][0] #val[0]
            str5 = sorted_tweeters[k][1][1]
            str6 = sorted_tweeters[k][1][2]
            str7 = sorted_tweeters[k][1][3]
            str8 = sorted_tweeters[k][1][4]
            str9 = sorted_tweeters[k][1][5]
            str10 = sorted_tweeters[k][1][6]
        else :
            str3 = ' '
            str4 = ' '
            str5 = ' '
            str6 = ' '
            str7 = ' '
            str8 = ' '
            str9 = ' '
            str10 = ' '
        if k < len(tweet_data) :
            val = tweet_data.get(tweet_data.keys()[k])
            str11 = val[0]
            str12 = val[1]
            time2 = val[2].split()
            str13 = time2[4]
        else :
            str11 = ' '
            str12 = ' '
            str13 = ' '
        if k < len(lang_hist) :
            val = lang_hist.get(lang_hist.keys()[k])
            str14 = lang_hist.keys()[k]
            str15 = lang_hist.get(lang_hist.keys()[k])
        else :
            str14 = ' '
            str15 = ' '
        if k < len(gender_hist):
            str16 = gender_hist.keys()[k]
            str17 = gender_hist.get(gender_hist.keys()[k])
        else :
            str16 = ' '
            str17 = ' '
        writer.writerow([str3,str4,str5,str6,str7,str8,str9,str10,str11,str12,str13,str14,str15,str16,str17])

def writeCSVads(filename,hashtags,tweet_list,tweet_data,lang_hist,gender_hist):
    print('writing to csv ads file')
    time = tweet_data.get(tweet_data.keys()[0])
    time2 = time[2].split()
    date = (time2[1]+' '+time2[2]+' '+time2[3])
    
    writer = csv.writer(open(filename+'hastag'+'.csv', 'wb'))
    writer.writerow(['total ads',len(tweet_data),'total people',len(tweet_list),'tom',time2[0],'date',date])
    writer.writerow(['hashtag','hashtag count','hash unique users', 'hash giveaway','language','language count','gender','gender count'])
    
    sorted_hash = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    sorted_tweeters = sorted(tweet_list.items(), key = lambda x: x[1], reverse=True)
    
    for k in range(0,len(hashtags)) :
        if (k < len(hashtags)) :
            str1 = sorted_hash[k][0].encode('utf-8') #hashtags.keys()[k].encode('utf-8')
            # val =  sorted_hash[k][1][0] #str(hashtags.get(hashtags.keys()[k],-1))
            str2 = sorted_hash[k][1][0]
            str2a = sorted_hash[k][1][1]
            str2b = sorted_hash[k][1][2]
        else :
            str1 = ' '
            str2 = ' '
            str2a = ' '
            str2b = ' '
        if k < len(lang_hist) :
            val = lang_hist.get(lang_hist.keys()[k])
            str14 = lang_hist.keys()[k]
            str15 = lang_hist.get(lang_hist.keys()[k])
        else :
            str14 = ' '
            str15 = ' '
        if k < len(gender_hist):
            str16 = gender_hist.keys()[k]
            str17 = gender_hist.get(gender_hist.keys()[k])
        else :
            str16 = ' '
            str17 = ' '
        writer.writerow([str1,str2,str2a,str2b,str14,str15,str16,str17])

def writeCSVhashdata(filename,hashtags,tweet_hash_data,tweet_data,tweet_list):
    print('writing to csv tweet_hash_data file')
    time = tweet_data.get(tweet_data.keys()[0])
    time2 = time[2].split()
    date = (time2[1]+' '+time2[2]+' '+time2[3])
    
    writer = csv.writer(open(filename+'tweethash'+'.csv', 'wb'))
    writer.writerow(['total ads',len(tweet_data),'total people',len(tweet_list),'day of the week',time2[0],'date',date])
    writer.writerow(['hashtag','tot hash count','user_id','user_name','count times used', 'count giveaways','followers','following','total tweets','language','gender'])
    sorted_hash = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    for k in range(0,len(sorted_hash)) :
        tag = sorted_hash[k][0]
        tot = sorted_hash[k][1][0]
        for l in tweet_hash_data[tag]  :
            val = tweet_hash_data[tag][l]
            user_id = l
            user_name = val[0]
            count = val[1]
            giveaway = val[2]
            followers = val[3]
            following = val[4]
            tot_tweets = val[5]
            lang = val[6]
            gender = val[7]
            writer.writerow([tag.encode('utf-8'),tot,user_id,user_name,count,giveaway,followers,following,tot_tweets,lang,gender])



def main():
    path = sys.argv[-1] #'/Users/bertasandberg/Development/pythonCode/2014-03-17'
    list = os.listdir(path)
    print(path)
   
    hashtags = dict() #uniqu hashtags
    hash_list = []  #list of all hashtags
    tweet_list = dict() #list of unique users who tweeted ads today
    tweet_data = dict() #list of tweet data per user and time it was tweeted
    tweet_hash_data = dict() #list of users and all the hashtags they used that had to do with ads
    lang_hist = dict() #histogram data for languages use
    gender_hist = dict() #histogram data for
    ad_count = 0 #number of ads for the day
    file_count = 0
    user_hash_use = dict()
    
    for key in list:
        filename = os.path.join(path,key)
        file_count = file_count +1
        with open(filename) as json_file:
            json_data = json.load(json_file)
    
        for k in range(0,len(json_data["interactions"])):
            ad_count = ad_count + 1
            val = json_data["interactions"][k]["twitter"]
            user_val = json_data["interactions"][k]["twitter"]["user"]["id"]
            if 'hashtags' in val.keys() :
                hash_val =json_data["interactions"][k]["twitter"]["hashtags"]
                giveaway = 0
                if ('Giveaway' in hash_val or 'Giveaways' in hash_val or 'giveaway' in hash_val or 'giveaways' in hash_val) :
                    giveaway=1
                user_name = json_data["interactions"][k]["twitter"]["user"]["screen_name"]
                language = json_data["interactions"][k]["twitter"]["user"]["lang"]
                if language in lang_hist :
                    lang_hist[language] = lang_hist[language] +1
                else :
                    lang_hist.setdefault(language)
                    lang_hist[language] = 1
                time = json_data["interactions"][k]["twitter"]["created_at"]
                time2 = time.split(); #we want 4th value in array for utc time
                twitter_created = json_data["interactions"][k]["twitter"]["user"]["created_at"]
                gender = "empty"
                if 'demographic' in json_data["interactions"][k].keys() :
                    gender = json_data["interactions"][k]["demographic"]["gender"]
                    tag = gender.lower()
                    if tag in gender_hist :
                        gender_hist[tag] = gender_hist[tag] +1
                    else :
                        gender_hist.setdefault(tag)
                        gender_hist[tag] = 1
                followers = json_data["interactions"][k]["twitter"]["user"]["followers_count"]
                following = json_data["interactions"][k]["twitter"]["user"]["friends_count"]
                favourite = -1.0
                if 'favourites_count' in json_data["interactions"][k]["twitter"]["user"]  :
                    favourite = json_data["interactions"][k]["twitter"]["user"]["favourites_count"]
                tag = str(ad_count)
                tweet_data.setdefault(tag,[])
                tweet_data[tag].append(user_val)
                tweet_data[tag].append(user_name)
                tweet_data[tag].append(time)
                    #tweet_data[tag].append(favourite)
                tag = user_val;
                if tag in tweet_list :
                    tweet_list[tag][0]=tweet_list[tag][0]+1
                else :
                    tweet_list.setdefault(tag,[])
                    tweet_list[tag].append(1)
                    tweet_list[tag].append(user_name)
                    tweet_list[tag].append(followers)
                    tweet_list[tag].append(following)
                    tweet_list[tag].append(favourite)
                    tweet_list[tag].append(gender)
                    tweet_list[tag].append(language)
                status = -1.0
                if 'statuses_count' in json_data["interactions"][k]["twitter"]["user"] :
                    status = json_data["interactions"][k]["twitter"]["user"]["statuses_count"]
            for l in range(0,len(hash_val)) :
                tag = hash_val[l].lower()
                #print tag
                if tag in hashtags :
                    hashtags[tag][0]=hashtags[tag][0]+1
                    if user_val not in tweet_hash_data[tag] :
                        hashtags[tag][1] +=1
                        # tweet_hash_data[tag].append(user_val)
                        tweet_hash_data[tag].setdefault(user_val,[])
                        tweet_hash_data[tag][user_val].append(user_name)
                        tweet_hash_data[tag][user_val].append(1)
                        tweet_hash_data[tag][user_val].append(1)
                        tweet_hash_data[tag][user_val].append(followers)
                        tweet_hash_data[tag][user_val].append(following)
                        tweet_hash_data[tag][user_val].append(status)
                        tweet_hash_data[tag][user_val].append(language)
                        tweet_hash_data[tag][user_val].append(gender)
                        hashtags[tag][2] +=giveaway
                    else :
                        tweet_hash_data[tag][user_val][1] +=1
                        tweet_hash_data[tag][user_val][2] +=giveaway
                else :
                    hashtags.setdefault(tag,[])
                    hashtags[tag].append(1)
                    hashtags[tag].append(1)
                    hashtags[tag].append(1)
                    tweet_hash_data.setdefault(tag,{}).setdefault(user_val,[])
                    #tweet_hash_data[tag].append(user_val)
                    tweet_hash_data[tag][user_val].append(user_name)
                    tweet_hash_data[tag][user_val].append(1)
                    tweet_hash_data[tag][user_val].append(1)
                    tweet_hash_data[tag][user_val].append(followers)
                    tweet_hash_data[tag][user_val].append(following)
                    tweet_hash_data[tag][user_val].append(status)
                    tweet_hash_data[tag][user_val].append(language)
                    tweet_hash_data[tag][user_val].append(gender)
                hash_list.append(tag)
             
    outputfile = sys.argv[-1]
    writeCSVads(outputfile,hashtags,tweet_list,tweet_data,lang_hist,gender_hist)
    writeCSVpeople(outputfile,hashtags,hash_list,tweet_list,tweet_data,lang_hist,gender_hist)
    writeCSV(outputfile,hashtags,hash_list,tweet_list,tweet_data,lang_hist,gender_hist," ")
    writeCSVhashdata(outputfile,hashtags,tweet_hash_data,tweet_data,tweet_list)


main()
sys.exit()






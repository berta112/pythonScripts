#from boto.s3.connection import S3Connection
#s3 = S3Connection()
#s3.get_bucket('faveme')
import boto
import sys, os
import json
import glob
#import time
import datetime
from datetime import datetime, timedelta,date, time
from os import listdir
from os.path import isfile, join
import csv
#from csv import DictWriter
    #from boto.s3.key import Key


def writeCSV(filename,daily_ad,weekly_ad,lang_hist,gender_hist):
    print('writing to csv tweet_hash_data file')
   
    writer = csv.writer(open(filename+'ad_data'+'.csv', 'wb'))
    
    writer.writerow(['day','daily count','week','weekly count','language','language count','gender','gender count'])
   
    for k in range(0,len(daily_ad)) :
        day = daily_ad.keys()[k]
        daily_count = daily_ad.get(day)

        weekly_count = ' '
        week = ' '
        if k < len(weekly_ad) :
           week = weekly_ad.keys()[k]
           weekly_count = weekly_ad.get(week)
        lang_count = ' '
        lang = ' '
        if k < len(lang_hist) :
            lang = lang_hist.keys()[k]
            lang_count = lang_hist.get(lang)
        gender_count = ' '
        gender = ' '
        if k < len(gender_hist) :
            gender =  gender_hist.keys()[k]
            gender_count = gender_hist.get(gender)
        writer.writerow([day,daily_count,week,weekly_count,lang,lang_count,gender,gender_count])



def main():
    path = sys.argv[-3] #'/Users/bertasandberg/Development/pythonCode/2014-03-17'
    start = sys.argv[-2]
    end = sys.argv[-1]
    start_date = datetime.strptime(str(start),"%Y-%m-%d")
    end_date = datetime.strptime(end,"%Y-%m-%d")
    print(start_date)
    print(end_date)
  
    lang_hist = dict() #histogram data for languages use
    gender_hist = dict() #histogram data for
    ad_count = 0 #number of ads for the day
    
    daily_ad = dict()
    weekly_ad = dict()
    #for list in dirlist:
    d = start_date
    delta = timedelta(days=1)
    week_count = 0
    print(end_date)
    while d <= end_date :
      current_date = d.strftime("%Y-%m-%d")
      print(current_date)
      filename = os.path.join(path,current_date)
      daily_ad.setdefault(current_date)
      list2 = os.listdir(filename)
      if week_count is 7 :
        week_count = 0
      if week_count is 0 :
        week = current_date
        weekly_ad.setdefault(week)
        weekly_ad[week]=0
        print week
      for key in list2:
        filename2 = os.path.join(filename,key)
        # filename = os.path.join(path,key)
        
        with open(filename2) as json_file:
            json_data = json.load(json_file)
        ad_count += len(json_data["interactions"]);
        for k in range(0,len(json_data["interactions"])):
            val = json_data["interactions"][k]["twitter"]
            if 'hashtags' in val.keys() :
                language = json_data["interactions"][k]["twitter"]["user"]["lang"]
                if language in lang_hist :
                    lang_hist[language] = lang_hist[language] +1
                else :
                    lang_hist.setdefault(language)
                    lang_hist[language] = 1
                gender = "empty"
                if 'demographic' in json_data["interactions"][k].keys() :
                    gender = json_data["interactions"][k]["demographic"]["gender"]
                    tag = gender.lower()
                    if tag in gender_hist :
                        gender_hist[tag] = gender_hist[tag] +1
                    else :
                        gender_hist.setdefault(tag)
                        gender_hist[tag] = 1
        #end reading data by the file
      weekly_ad[week] += ad_count
      week_count += 1
      daily_ad[current_date] = ad_count
      ad_count = 0
      d += delta
    
    #print (len(daily_ad),len(weekly_ad),len(lang_hist),len(gen_hist))
    outputfile = start+' '+end  #sys.argv[-1]
    writeCSV(outputfile,daily_ad,weekly_ad,lang_hist,gender_hist)

main()
sys.exit()






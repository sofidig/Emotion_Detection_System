import csv
import os
arr = []
with open ('legend.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            emotion = row['emotion'].lower()
            if emotion == 'happiness':
                print (emotion)
                prevName = row['image']
                newName = 'happiness/'+row['image']
                os.rename(prevName,newName)
            if emotion == 'neutral':
                print (emotion)
                prevName = row['image']
                newName = 'neutral/'+row['image']
                os.rename(prevName,newName)
            if emotion == 'surprise':
                print (emotion)
                prevName = row['image']
                newName = 'surprise/'+row['image']
                os.rename(prevName,newName)
            if emotion == 'anger':
                print (emotion)
                prevName = row['image']
                newName = 'anger/'+row['image']
                os.rename(prevName,newName)
            if emotion == 'disgust':
                print (emotion)
                prevName = row['image']
                newName = 'disgust/'+row['image']
                os.rename(prevName,newName)
            if emotion == 'fear':
                print (emotion)
                prevName = row['image']
                newName = 'fear/'+row['image']
                os.rename(prevName,newName)
            if emotion == 'sadness':
                print (emotion)
                prevName = row['image']
                newName = 'sadness/'+row['image']
                os.rename(prevName,newName)
        except (FileNotFoundError):
            continue


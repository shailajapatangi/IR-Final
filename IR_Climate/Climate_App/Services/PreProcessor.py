import re
import os

def getDocuments(data):

    documents = []; id = 0
    for each in data['response']['docs']:

        if(id==5):
            break
        documents.append(each['content']);
        id+=1


    return documents

def processDocuments(documentList):

    cwd = os.getcwd()
    with open(cwd+"/Climate_App/Services/stopwords", "r") as f:
        stop_list = set(line.rstrip('\n') for line in f)

    docAfterProcessing = []
    for each in documentList:

        each = cleanString(each)

        for word in stop_list:
            each = re.sub(r'\b%s\b' % word,"",each)

        docAfterProcessing.append(each)

    return docAfterProcessing

def cleanString(string):
    string = string.replace('"',"")
    string = re.sub("<.*?>", " ", string)
    string = re.sub("'s", "", string)
    string = re.sub("[+^:,*?;#&~=%@`'$!_)/(}{\\.]", "", string)
    string = re.sub('-', " ", string)
    #string = re.sub("[^a-zA-Z0-9 ]","",string)
    string = re.sub("\\s+", " ", string).strip().lower()
    string = re.sub(r'\b\d+\b', '', string)

    return string
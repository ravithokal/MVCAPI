from django.shortcuts import render
import os
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

# Mthod for home page redirection
@csrf_exempt
def index(request):
    return render(request, 'home.html')

    
@csrf_exempt
def CreateLogoByName(request):
    """
        Check if an ID was provided as part of the URL(request).
        If ID is provided or present in request then assign it to a variable.
        If there is no ID in request the show the error message.
    """
    id = request.POST.get('id')
  
    with open('static/CompaniesList.json', encoding="utf8") as f:
        companyDetails = json.loads(f.read())
  
    for company in range(len(companyDetails)):
        companyId = companyDetails[company]['CompanyId']
        if companyId == id:
            companyName = companyDetails[company]['Company_Name']
            if len(companyName) > 0:
                occurenceList = []
                occurenceList = charOccurence(str(companyName))
                logoName = chooseCharForLogo(occurenceList)

    if logoName != 404:
        return render(request, 'result.html', {'logo_name':logoName})
    else:
        return render(request, 'result.html', {'logo_name':'Error!!!'})
    


def chooseCharForLogo(occurenceList):
    logoName = ""
    try:
        occurenceList = sorted(occurenceList, key=lambda x: (-occurenceList[x], x))
        sortedoccurenceList = occurenceList[0:3]
        logoName = listToString(sortedoccurenceList)
        return logoName
    except:
        return 404

def listToString(list):  
    res = ""
    if(len(list) != 0):
        s = [str(i) for i in list] 
        # Join list items using join() 
        res = "".join(s)
    return(res) 

def charOccurence(str):
   occurence = {}
   print("in char occurance",str)
   for c in str:
       if c != " ":
           occurence[c] = str.count(c)
   return occurence


def read_jsonFile_data():
    # fp = open(data_source, 'r')
    json_data = open('static/CompaniesList.json', encoding="utf8")
    data1 = json.loads(json_data)
    print("*****************",type(json_data)) 
    data_source = json.dumps(data1)
    print("!!!!!!!!!!!!!!!!",data_source)
    print("!!!!!!******!!!!",type(data_source))

    return data_source


    
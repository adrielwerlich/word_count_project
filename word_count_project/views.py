from django.http import HttpResponse
from django.shortcuts import render
import operator
def showRequest(request):
    #return HttpResponse(print("COOKIES: --- " + str(request.method)))
    return HttpResponse("request")

def myView(request):
    return HttpResponse('my arbitrary text message')

def homePage(request):
    return render(request, 'myHomePage.html', {'dicKey':'dicValue_test'})

def count(request):
    myVar = request.GET['myTextArea']
    wordList = myVar.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    #print(myVar)
    return render(request, 'make_show_count.html',
                  {'myKey': myVar, 'lenOfWordList': len(wordList),'wordDicKey': wordDict.items(),
                   'mySortedDic': sortedWords})


def gotoAbout(request):
    return render(request, 'about.html')
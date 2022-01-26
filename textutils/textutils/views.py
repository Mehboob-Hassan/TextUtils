# MH made this file
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

# First function to show main Index file 
def first(request):
    return render(request, 'index.html')

#Getting the values from the index file
def analyze(request):
    gettext = request.POST.get('text','off')
    rmvpunc = request.POST.get('removePunc','off')
    rmvExSpace = request.POST.get('removeExSpace','off')
    rmvNLine = request.POST.get('removeNLine','off')
    countChar = request.POST.get('countChar','off')
    capit = request.POST.get('cap','off')

#Capitalizing
    if(capit == "on"):
        analyzed = ""
        for char in gettext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Analyze Text', 'analyzed_text': analyzed}
        gettext = analyzed

#Removing Punctuations
    if rmvpunc == 'on':
        print(rmvpunc)
        analyzed = ""
        puncts = '''"'!@#$%^&*().,?<>|;/\:'''
        for char in gettext:
            if char not in puncts:
                analyzed = analyzed + char
            params = {'purpose': 'Analyze Text', 'analyzed_text': analyzed}
            gettext = analyzed

    #Removing Extra Space
    if rmvExSpace == 'on':
        analyzed = ""
        for index, char  in enumerate(gettext):
            if not(gettext[index]==" " and gettext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Analyze Text', 'analyzed_text': analyzed}
        gettext = analyzed

    #Removing New Line
    if(rmvNLine == 'on'):
        analyzed = ""
        for char in gettext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char    
            params = {'purpose': 'Analyze Text', 'analyzed_text': analyzed}
            gettext = analyzed


    return render(request, 'analyze.html', params)

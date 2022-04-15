import re
from django.shortcuts import render
from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def M2H(title):
    MDfile=util.get_entry(title)
    text=markdown2.markdown(MDfile)
    return text


def click2Entry(request):
    title=request.GET['topic']
    text=M2H(title)
    return render(request,'entryPage.html',{"title":title,"content":text})

def search2Entry(request):
    query=request.GET['q']
    entries=util.list_entries()
    titles=list()
    flag=0
    for entry in entries:
        if query==entry :
            flag=1
            break
        elif query in entry:
            flag=2
            titles.append(entry)
    if flag==0:
        return render(request,'error.html',{"error":"The entry searched for does not exist：)"})
    elif flag==2:
        return render(request,'index.html',{"entries":titles})
    else:
        text=M2H(query)
        return render(request,'entryPage.html',{"title":query,"content":text})

def randomEntry(request):
    entries=util.list_entries()
    count=len(entries)
    rnum=random.randint(0,count-1)
    title=entries[rnum]
    text=M2H(title)
    return render(request,'entryPage.html',{"title":title,"content":text})

def addNew(request):
   return render(request,'newPage.html') 


def editMD(request):
    title=request.GET['t']
    MDtext=util.get_entry(title)
    return render(request,'mdeditor.html',{"title":title,"content":MDtext})

def saveNewMD(request):
    title=request.GET['t']
    for entry in util.list_entries():
        if title==entry:
            return render(request,'error.html',{"error":"This entry already exits!"})
    content=request.GET['c']
    util.save_entry(title,content)
    text=M2H(title)
    return render(request,'entryPage.html',{"title":title,"content":text})

def saveMD(request):
    title=request.GET['t']
    content=request.GET['c']
    util.save_entry(title,content)
    text=M2H(title)
    return render(request,'entryPage.html',{"title":title,"content":text})

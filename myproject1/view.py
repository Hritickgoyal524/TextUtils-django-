from django.http import HttpResponse
from django.shortcuts import render 
def index(request):
    parm={"package":"Django","langauge":"Python"}
    return render(request,'index.html',parm)
def analyzer(request):
     text=request.POST.get("text","Hiiii")
     removepun=request.POST.get("removepun","of")
     upparcase=request.POST.get("Upparcase","of")
     removenewline=request.POST.get("Removenewline",'of')
     lowercase=request.POST.get("Lowercase","of")
     extraspace=request.POST.get("Extraspace","of")
     analyzed=""
     punctuation='''!()-{}[];,"":'/\?<>.@#$%^&*~'''
     if removepun=="on":
       for char in text:
           if char not in punctuation:
             analyzed=analyzed+char  
       parm={"purpose":"Removed punctuation","analyzed_text":analyzed}
       text=analyzed
       #return render(request,'analzer.html',parm)
     if upparcase=='on':  
            analyzed=text.upper()
            parm={"purpose":"Upparcase Conversion","analyzed_text":analyzed}
            text=analyzed
            #return render(request,'analzer.html',parm)
     if removenewline=='on':
            for char  in text:
                 if not char=='\n':
                    analyzed+=analyzed+char 
            parm={"purpose":"NewLine Remover","analyzed_text":analyzed}
            text=analyzed
            #return render(request,'analzer.html',parm)
     if lowercase=='on':
            analyzed=text.lower()
            parm={"purpose":"Lowercase Conversion","analyzed_text":analyzed}
            text=analyzed
           # return render(request,'analzer.html',parm)       
     if extraspace=='on':
            for index,char in enumerate(text):
                 if not (text[index]=='\n'and text[index+1]=="\n"):
                    analyzed+=analyzed+char 
            parm={"purpose":"NewLine Remover","analyzed_text":analyzed}
            text=analyzed
            #return render(request,'analzer.html',parm)
     if extraspace!='on' and lowercase!='on' and removenewline!='on' and upparcase!='on' and  removepun!="on":

        return HttpResponse("Please select any operation")
     return render(request,'analzer.html',parm) 

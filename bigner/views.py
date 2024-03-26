from django.shortcuts import render,redirect
from django.http import HttpResponse



def home(request):
    params={'name':'Parmeshwar Gupta','place':'mars'}
    return render(request, 'index.html', params)

def index(request):
    return HttpResponse("this is index page <a href='/'>back</a>")

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspace=request.POST.get('extraspace','off')
    charcount=request.POST.get('charcount','off')




    # print(removepunc)
    # print(djtext)
    analysed=""
    punctuations='''~`!@#$%^&*()_|\}{]['":;?/>.<,'''
    if removepunc=='on':
        for i in djtext:
            if i not in punctuations and removepunc=='on':
                analysed=analysed+i
            
        params={'purpose':'Removed Punctuation', 'analysed_text':analysed}
        djtext=analysed
        # return render(request,'analysed.html', params)
   
    if (fullcaps=='on'):
         analysed=""
         for char in djtext:
             analysed=analysed+char.upper()
         params={'purpose':'captalize the text', 'analysed_text':analysed}
         djtext=analysed
        #  return render(request,'analysed.html', params)
    
   
    if (newlineremove == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext=analysed
        # return render(request, 'analysed.html', params)
           
    if(extraspace=="on"):
        analysed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
               analysed=analysed+char
        params={'purpose':'extra spaces are removed', 'analysed_text':analysed}
        djtext=analysed
        # return render(request,'analysed.html', params)
    
    if(charcount=="on"):
        analysed=0
        for char in djtext:
            if (char!=" "):
               analysed=analysed+1
        params={'purpose':'this count all the character', 'analysed_text':analysed}
                  
    if(removepunc!='on' and fullcaps!='on'and newlineremove != "on" and extraspace!="on" and charcount!="on"):
         return HttpResponse("please mark the chekbox" )  
    
    return render(request,'analysed.html', params)
         

    
       

# def capfirst(request):
#     return HttpResponse("this is captalizer  page")

# def newlineremove(request):
#     return HttpResponse("this is new line remover page")

# def spaceremove(request):
#     return HttpResponse("this is space remover page page")

# def charcount(request):
#     return HttpResponse("this is char count  page")

# def removepunc(request):
#     return HttpResponse("this is remove punctuation page")
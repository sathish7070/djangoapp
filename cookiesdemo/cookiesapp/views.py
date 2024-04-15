from django.shortcuts import render

# Create your views here.
def cookies_count_view(request):
    count=request.session.get('count',0)
    totalcount=int(count)+1
    request.session['count']=totalcount
    print(request.session.get_expiry_date())
    return render(request,'cookiesapp/cookiescount.html',{'count':totalcount})
    
#def cookies_count_view(request):
 #   count=request.COOKIES.get('count',0)
  #  totalcount=int(count)+1
   # response=render(request,'cookiesapp/cookiescount.html',{'count':totalcount})
    #response.set_cookie('count',totalcount)
    #return response
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from random import choice
from django.http import JsonResponse
from home.models import buffer,portfolio

l=[]
#Load All labels of companies
s=open('static\\text\\dataset_company-symbols.txt')
data=s.read().split(',')
s.close()
#Some importants commands
def get_buffer(symbol):
    data=buffer.objects.filter(symbol=symbol)
    return data.buffer
def get_stock_price(request,stock_exchange='NSE'):
    symbol=l[-1]
    url = f"https://www.google.com/finance/quote/{symbol}:{stock_exchange}"
    requests.get(url)
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    data_element = soup.find("div", class_='YMlKec fxKbKc')
    return JsonResponse({'stock_price': data_element.get_text()})


    
#Some importants commands
def fetch_stock(symbol,stock_exchange='NSE'):
    url = f"https://www.google.com/finance/quote/{symbol}:{stock_exchange}"
    requests.get(url)
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    data={'symbol':symbol,'stock_exchange':stock_exchange,'stock_name':None,'stock_price':None,'toggle_per':None,'current_price':None,'prev_close':None,'day_range':None,'year_range':None,'market_cap':None,'pe_ratio':None,'div_yield':None}
    fetch_data_classes={'stock_name':'zzDege','stock_price':'YMlKec fxKbKc ','toggle_per':'JwB6zf','current_price':'P2Luy Ez2Ioe ZYVHBb','div_yield':'gyFHrc'}
    for key,value in fetch_data_classes.items():
        data_element = soup.find("div", class_=value)
        if data_element:
            data[key]=data_element.get_text()

    class_name = "P6K39c"
    elements = soup.find_all(class_=class_name) 
    try:
        data['prev_close']=elements[0].get_text()
        data['day_range']=elements[1].get_text()
        data['year_range']=elements[2].get_text()
        data['market_cap']=elements[3].get_text()
        data['pe_ratio']=elements[4].get_text()
        data['div_yield']=data['div_yield'][36:]
    except:
        pass
    return data


# Create your views here.
def home(request,data=data):
    
    s=str(choice(data))[1:]
    s=s.replace('"','')
    data=fetch_stock(s)
    l.append(s)
    parms={'stock_detail':data}
    print(buffer.objects.all())
    try:
        buffer_data=buffer.objects.filter(symbol=s)
        buffer_num=buffer_data.buffer
    except:
        buffer_data=buffer(symbol=s,price_bought=0,buffer=0)
        buffer_num=0
        buffer_data.save()
    if request.method == 'POST':
        fraction_stock=request.POST.get('fraction_stock')
        print(fraction_stock)
        SI=int(fraction_stock)
        # if SI+buffer_num>fraction_stock:
        buffer_data=buffer(symbol=s,buffer=SI+buffer_num-fraction_stock)
        buffer_data.save()
        portfolio_data=portfolio(symbol=s,price_bought=get_stock_price(s)['stock_price'],fraction_bought=fraction_stock)        
        portfolio_data.save()
        parms['order_passes']=True
        

    return render(request,'home/index1.html',parms)
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
#Some importants commands
def fetch_stock(symbol,stock_exchange='NSE'):
    url = f"https://www.google.com/finance/quote/{symbol}:{stock_exchange}"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    data={'symbol':symbol,'stock_exchange':stock_exchange,'stock_name':None,'stock_price':None,'toggle_per':None,'current_price':None,'prev_close':None,'day_range':None,'year_range':None,'market_cap':None,'pe_ratio':None,'div_yield':None}
    fetch_data_classes={'stock_name':'zzDege','stock_price':'YMlKec fxKbKc','toggle_per':'JwB6zf','current_price':'P2Luy Ez2Ioe ZYVHBb','div_yield':'gyFHrc'}
    for key,value in fetch_data_classes.items():
        data_element = soup.find("div", class_=value)
        if data_element:
            data[key]=data_element.get_text()

    class_name = "P6K39c"
    elements = soup.find_all(class_=class_name) 
    data['prev_close']=elements[0].get_text()
    data['day_range']=elements[1].get_text()
    data['year_range']=elements[2].get_text()
    data['market_cap']=elements[3].get_text()
    data['pe_ratio']=elements[4].get_text()
    data['div_yield']=data['div_yield'][36:]
    return data


# Create your views here.
def home(request):
    data=fetch_stock('INDSWFTLAB')
    print(data)
    parms={'stock_detail':data}
    return render(request,'home/index1.html',parms)
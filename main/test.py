# # import requests

# # url = "https://alpha-vantage.p.rapidapi.com/query"

# # querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

# # headers = {
# # 	"X-RapidAPI-Key": "ca9b400099msh7bf11aa6338a124p14c14ejsn3dd373131bb0",
# # 	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
# # }

# # response = requests.get(url, headers=headers, params=querystring)
# # data=response.json()
# # print(len(data['Time Series (5min)']))


# #live stocks prize
# # from yahoo_fin.stock_info import get_analysts_info
# # import yahoo_fin.stock_info as si
# # si.get_quote_table("aapl", dict_result = False)
# # import pandas as pd
# # import datetime
# # import requests
# # from requests.exceptions import ConnectionError
# # from bs4 import BeautifulSoup

# # def web_content_div(web_content,class_path):
# #     web_content_div=web_content.find_all('div',{'class':class_path})
# #     print(web_content_div)
# #     try:
# #         spans=web_content_div[0].find_all('span')
# #         texts=[span.get_text() for span in spans]
# #     except IndexError:
# #         texts=[]
# #     return texts
# # def real_time_price(stock_code):
# #     # url=f'https://finance.yahoo.com/quote/{stock_code}p={stock_code}&.tsrc=fin-srch'
# #     url='https://www.google.com/finance/quote/INDSWFTLAB:NSE'
# #     try:
# #         r=requests.get(url)
# #         web_content=BeautifulSoup(r.text,'lxml')
# #         print(web_content)
# #         texts=web_content_div(web_content,'My(6px) Pos(r) smartphone_Mt(6px)')
# #         print(texts)
# #         if texts!=[]:
# #             price,change=texts[0],texts[1]
# #         else:
# #             price,change=[],[]

# #     except ConnectionError:
# #         price,change=[],[]
# #     return price,change
# # Stock=['DIS']
# # print(real_time_price(Stock[0]))

# import requests
# from bs4 import BeautifulSoup
# def fetch_stock(symbol,stock_exchange='NSE'):
#     url = f"https://www.google.com/finance/quote/{symbol}:{stock_exchange}"
#     response = requests.get(url)
#     html_content = response.content
#     soup = BeautifulSoup(html_content, "html.parser")
#     data={'symbol':symbol,'stock_exchange':stock_exchange,'stock_name':None,'stock_price':None,'toggle_per':None,'current_price':None,'prev_close':None,'day_range':None,'year_range':None,'market_cap':None,'pe_ratio':None,'div_yield':None}
#     fetch_data_classes={'stock_name':'zzDege','stock_price':'YMlKec fxKbKc','toggle_per':'JwB6zf','current_price':'P2Luy Ez2Ioe ZYVHBb','div_yield':'gyFHrc'}
#     for key,value in fetch_data_classes.items():
#         data_element = soup.find("div", class_=value)
#         if data_element:
#             data[key]=data_element.get_text()

#     class_name = "P6K39c"
#     elements = soup.find_all(class_=class_name) 
#     data['prev_close']=elements[0].get_text()
#     data['day_range']=elements[1].get_text()
#     data['year_range']=elements[2].get_text()
#     data['day_range']=elements[3].get_text()
#     data['market_cap']=elements[4].get_text()
#     data['pe_ratio']=elements[5].get_text()
#     data['div_yield']=data['div_yield'][36:]
#     return data




# print(fetch_stock('BBL'))






# # import requests

# # url = "https://www.google.com/finance/quote/TCS:NSE"
# # response = requests.get(url)
# # html_content = response.content

# # from bs4 import BeautifulSoup

# # soup = BeautifulSoup(html_content, "html.parser")

# # class_name = "P6K39c"
# # elements = soup.find_all(class_=class_name)
# # extracted_data = []

# # for element in elements:
# #     # Extract data from each element and append it to the list
# #     data = element.get_text()  # Adjust this based on your specific needs
# #     extracted_data.append(data)

# # print(extracted_data)
import upstox_client
from upstox_client import api_client    

api_key = 'your_api_key'
api_secret = 'your_api_secret'
redirect_uri = 'http://localhost'  # Redirect URI used during authentication
api_client
upstox = Upstox(api_key, api_secret)

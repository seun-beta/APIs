import urllib.request, urllib.error
import json
import ssl 

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print ('Welcome to your exchange rates portal!')
name = input('What is your name: ')
print (name,'Please note that the DEFAULT BASE CURRENCY is EUR')
print ('Welcome!', name)

usage = input(''' 
Type '1' if you want the latest exchange rate.\n
Type '2' if you want historical exchange rates for a time period.\n 
Type '3' if you want to change the base currency.\n 
Type '4' if you want a specific exchange rate e.g: USD to EUR.\n 
Type '5' if want historical exchange rates for a time peroid.\n
Type '6' if you want historical exchagnge rates against a different currency.\n 
Input your number: ''' )

currency_2 = None

choice = 'n'
while choice == 'n':
    try:
        usage = int(usage)
    except:
        print ('Please input a valid number')
        continue 
    if usage == 1:
        api_url ='https://api.exchangeratesapi.io/latest'
        ex_url = api_url

    elif usage == 2:
        api_url= 'https://api.exchangeratesapi.io/'
        print ('Please input the day in YYYY-MM-DD format ')
        day = input('Input the day: ')
        ex_url = api_url + day

    elif usage == 3:
        api_url = 'https://api.exchangeratesapi.io/latest?base='
        print ('Please input the BASE currency you want to use e.g: USD, EUR, GBP, JPY. ')
        change_base = input('Input the currency you want to use as BASE CURRENCY ')
        change_base = change_base.upper()
        ex_url = api_url + change_base

    elif usage == 4:
        api_url = 'https://api.exchangeratesapi.io/latest?symbols='
        currency_1 = input('Input the first currency: ')
        currency_1 = currency_1.upper()
        currency_2 = input('Input the second currency: ')
        currency_2 = currency_2.upper()
        print ('This means you are converting from', currency_1,'to',currency_2)
        ex_url = api_url + currency_1 + ',' + currency_2

    elif usage == 5:
        api_url = 'https://api.exchangeratesapi.io/history?start_at='
        print ('The date format is YYYY-MM-DD')
        first_day = input('Input the first day: ')
        last_day = input ('Input the last day: ')
        ex_url = api_url +first_day+ '&end_at='+ last_day

    elif usage == 6:
        api_url = 'https://api.exchangeratesapi.io/history?start_at='
        print ('The date format is YYYY-MM-DD')
        change_base = input('Input the currency you want to use as BASE CURRENCY ')
        first_day = input('Input the first day: ')
        last_day = input ('Input the last day: ')
        ex_url = api_url +first_day+ '&end_at='+ last_day + 'base='+change_base

    choice = input('''Type 'y' to move on or 'n' to input again: ''' )


url = urllib.request.urlopen(ex_url,context = ctx)
read_url = url.read().decode()

data = json.loads(read_url)
yes = 'y'
while yes == 'y': 
    if currency_2 is None:
        input_currency = input ('Input the abbreviation of the currency: ')
        input_currency = input_currency.upper()
        currency = data['rates'][input_currency]
        print ('''1 EUR is equal to {} {}'''.format(currency,input_currency))
    else :
        currency = data['rates']
        print (currency)
    yes = input('''Type 'y' to continue or 'n' to stop: ''')

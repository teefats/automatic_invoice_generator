import requests

url = 'http://127.0.0.1:5000/'
data = {
'duedate': 'September 1, 2014',
'from_addr': {
            'addr1': '12345 Sunny Road',
            'addr2': 'Sunnyville, CA 12345',
            'company_name': 'Python Tip'
        },
        'invoice_number': 123,
        'items': [{
                'charge': 300.0,
                'title': 'website design'
            },
            {
                'charge': 75.0,
                'title': 'Hosting (3 months)'
            },
            {
                'charge': 10.0,
                'title': 'Domain name (1 year)'
            }
        ],
        'to_addr': {
            'company_name': 'Acme Corp',
            'person_email': 'john@example.com',
            'person_name': 'John Dilly'
        }}

html = requests.post(url, json=data)
with open('invoice.pdf', 'wb') as f:
    f.write(html.content)
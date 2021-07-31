    
from_addr= {
            'addr1': '12345 Sunny Road',
            'addr2': 'Sunnyville, CA 12345',
            'company_name': 'Python Tip'
        },
      
items= [{
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
to_addr= {
            'company_name': 'Acme Corp',
            'person_email': 'john@example.com',
            'person_name': 'John Dilly'
        }
duedate = "July 1, 2021"
total = sum([i[0]['charge'] for i in items])
#print(total)

for item in items:
    total = sum(deal['charge'] for deal in item for item in items)
    print(total)
    
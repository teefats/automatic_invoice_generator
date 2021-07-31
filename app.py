from weasyprint import HTML
#import flask
from flask import Flask, render_template
from datetime import date
import os
app = Flask(__name__)


# html =HTML('invoice.html')
# html.write_pdf('invoice.pdf')



@app.route('/')
def hello_world():
    today = date.today()#.strftime("%B %-d, %Y")
    today =today.strftime("%d/%m/%Y")
    invoice_number = 123
    
    from_addr= {
            'addr1': '12345 Sunny Road',
            'addr2': 'Sunnyville, CA 12345',
            'company_name': 'Python Tip'
        }
    to_addr= {
            'company_name': 'Acme Corp',
            'person_email': 'john@example.com',
            'person_name': 'John Dilly'
        }
      
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
 
    duedate = "July 1, 2021"
    for item in items:
        total = sum(deal['charge'] for deal in item)
    

    return render_template('invoice.html', date=today,from_addr=from_addr, to_addr=to_addr, items=items, total=total, invoice_number=invoice_number,duedate=duedate)
    


    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
from pyscript import display
from js import document

# Basic info
owner_first_name = 'Selena Mansueto'
owner_last_name = 'Galvez'
sections = ['Emerald', 'Ruby', 'Sapphire', 'Topaz']
restaurant_name = 'Filo'
year_established = '2025'
business_hours = '10 AM - 9 PM'

# Menu as list of tuples
products = [
    ("Adobo",  250 ),
    ("Sinigang",  250 ),
    ("Sisig",  150 ),
    ("Tinola", 120 ),
    ("Lumpia", 220 )
]

# Display owner and metadata
if document.getElementById('div3'):
    display(f'Owner: {owner_first_name} {owner_last_name}', target='div3')
    display(f'Since {year_established}', target='div3')
    display(f'Section: 10-{sections[2]}', target='div3')
    display(f'Business Hours: {business_hours}', target='div3')

# Display products
if document.getElementById('div2'):
    display("Product Name - Price", target='div2')
    for product in products:
        display(f"{product[0]} - {product[1]}", target='div2')

# Contact info

contact_email = "contact@filo.com"
phone_number = "+63 914 241 7582"
location = "123 Sesame street"

# Display contact info
if document.getElementById('contact-info'):
    display(f'Please feel free to contact us your concerns!', target='contact-info')

if document.getElementById('location-info'):
    display(f"📍 Location: {location}", target="location-info")

if document.getElementById('contact-details'):
    display(f"📞 Phone: {phone_number}", target="contact-details")

if document.getElementById('email-info'):
    display(f"📧 Email: {contact_email}", target="email-info")

# Order Form

prices = {
    'adobo': 250,
    'sinigang': 250,
    'sisig': 150,
    'tinola': 120,
    'lumpia': 220,
}

def sample_function(e):
    name = document.getElementById('text1').value
    address = document.getElementById('text2').value
    contact = document.getElementById('text3').value

    adobo_price = prices['adobo'] if document.getElementById('adobo').checked else 0
    sinigang_price = prices['sinigang'] if document.getElementById('sinigang').checked else 0
    sisig_price = prices['sisig'] if document.getElementById('sisig').checked else 0
    tinola_price = prices['tinola'] if document.getElementById('tinola').checked else 0
    lumpia_price = prices['lumpia'] if document.getElementById('lumpia').checked else 0

    total = adobo_price + sinigang_price + sisig_price + tinola_price + lumpia_price

    document.getElementById('output').innerHTML = ""

    display(f'Order Receipt', target='output')
    display("----------------------", target='output')
    display(f'Order for: {name}', target='output')
    display(f'Address: {address}', target='output')
    display(f'Contact number: {contact}', target='output')
    display("----------------------", target='output')

    display(f'Total Price: ₱{total}', target='output')

    display("----------------------", target='output')
   

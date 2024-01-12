from django.db import connection
from django.shortcuts import render

# from .models import Product

def index(request):
#    products = Product.objects.all()
#    return render(request, 'index.html', {'products': products})
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products;")
        columns = [col[0] for col in cursor.description]
        data = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return render(request, 'index.html', {'products': data})

def about(request):

    testimonials = [
        {
            "name": "Shraddha Negi",
            "title": "Local Guide",
            "text": "A name which is synonymous with quality, value for money and excellent services. SINGH IS TRULY THE KING OF ALL DARBARS - In all categories of food menu served. From crispy kachoris to melt in mouth moti chur laddos they can wow! and impress you with all!! 😋 😋 yumm",
            "img": "assets/img/testimonial/img-01.jpg"
        },
        {
            "name": "Bharat Arya",
            "title": "Local Guide",
            "text": "It is a very beautiful dhaba and the staff here is very good, the taste is also amazing, the sweets and snacks here are also very tasty, the cleanliness is very good, this is a small Punjab, you all must visit here. 💯👍",
            "img": "assets/img/testimonial/img-02.jpg"
        },
        {
            "name": "Harpreet Singh",
            "title": "Local Guide",
            "text": "Phenomenal quality of sweets. Much better than other renowned names of the town. The most prominent thing is that they have very calculated sugar quantity in their sweets, unlike others which let you taste sugar instead of particular sweet. Must try before preferring other old brands. Hundred out of hundred.",
            "img": "assets/img/testimonial/img-03.jpg"
        }
    ]

    return render(request, 'about.html', {'testimonials': testimonials})

def sweetsDhaba(request):
    return render(request, 'sweets-dhaba.html')

def panIndia(request):
    return render(request, 'pan-india.html')

def contact(request):
    return render(request, 'contact.html')

def productDetail(request, name):
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM product WHERE name = %s", [name])
    #     columns = [col[0] for col in cursor.description]
    #     data = [
    #         dict(zip(columns, row))
    #         for row in cursor.fetchall()
    #     ]
    # return render(request, 'product-detail.html', {'data': data})
    return render(request, 'product-detail.html')
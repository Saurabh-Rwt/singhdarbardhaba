from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products ORDER BY created_at DESC LIMIT 8;")
        columns = [col[0] for col in cursor.description]
        data = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return render(request, 'index.html', {'latest_products': data})


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
    all_products = Product.objects.all()

    selected_category_slug = request.GET.get('category', None)
    selected_subcategory = request.GET.get('subcategory', None)

    filters = {}

    # Apply category filter
    if selected_category_slug:
        filters['category'] = selected_category_slug

    # Apply subcategory filter
    if selected_subcategory:
        filters['sub_category'] = selected_subcategory

    all_products = all_products.filter(**filters)

    paginator = Paginator(all_products, 6)

    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'sweets-dhaba.html', {'products': products, 'selected_category_slug': selected_category_slug, 'selected_subcategory': selected_subcategory})

def panIndia(request):
    return render(request, 'pan-india.html')

def contact(request):
    return render(request, 'contact.html')

def productDetail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product-detail.html', {'product': product})
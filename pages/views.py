from django.shortcuts import render, get_object_or_404

from ads.models import Ads, Category, AdsImages, AdsTopBanner, AdsRightBanner, AdsBottomBanner
from django.contrib.auth.models import User
from ads.models import Author
from django.core.mail import send_mail
from django.conf import settings



# Model Forms.

# Create your views here.

# Home view
def home(request):
    
    # Fetch recend ads
    recent_ads = Ads.objects.filter(is_active=True).order_by('-date_created')[0:4]
    
    # Fetch featured Ads
    featured_ads = Ads.objects.filter(is_featured=True).filter(is_active=True)
    #get counts
    ads_count = Ads.objects.all().count()
    user_count = User.objects.all().count()
    
    # Browse Ads by Category
    category_listing = Category.objects.all()

    # Browse Ads by State
    #state_listing = State.objects.all()

    # Fetch Ads Banner
    sidebar_banners = AdsRightBanner.objects.all()
    top_banner = AdsTopBanner.objects.all()
    bottom_banner = AdsBottomBanner.objects.all()

    # Fetch search location & category 
    #state_search = State.objects.values_list('state_name', flat=True).distinct().order_by("state_name")
    category_search = Category.objects.values_list('category_name', flat=True).distinct().order_by("category_name")
    
    # Contexts
    context = {
        'recent_ads' : recent_ads,
        'featured_ads' : featured_ads,
        #'state_search' : state_search,
        'category_search' : category_search,
        'category_listing' : category_listing,
        #'state_listing' : state_listing,
        'sidebar_banners' : sidebar_banners,
        'top_banner' : top_banner,
        'user_count':user_count,
        'ads_count':ads_count,
        'bottom_banner' : bottom_banner,
    }

    return render(request, 'pages/index.html', context)

# Faq view
def faq(request):
    return render(request, 'pages/faq.html')

# Terms of service view
def terms_of_service(request):
    return render(request, 'pages/terms-of-service.html')

# Contact view
def contact(request):
    if request.method=="POST":
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')

      data = {
        'email':email,
        'subject':subject,
        'message':message
      }
      message ='''
      New message: {}

      From: {}
      '''.format(data['message'],data['email'])
      #send_mail('Contact Form',message,settings.EMAIL_HOST_USER,['dailytourneys2022@gmail.com'],fail_silently=False
      send_mail(data['subject'],message,'',['dailytourneys2022@gmail.com'])
    return render(request, 'pages/contact.html')

def ads_search(request):
    
    if request.method=="POST":
      searched=request.POST['searched']
      ads_search_result = Ads.objects.filter(title__contains=searched)
      context = {
        'searched':searched,
        'ads_search_result':ads_search_result
    }

    return render(request, 'ads/ads-search.html',context)

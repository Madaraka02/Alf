from django.shortcuts import render, get_object_or_404,redirect
from .forms import *
from blogs.models import *
from blogs.forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs=Blog.objects.filter(approved=True).order_by('-id')[:4]
    atts=Attraction.objects.all().order_by('-id')[:3]
    att3=Attraction.objects.all().order_by('-id')[3:6]
    destinations=Park.objects.all().order_by('-id')[:6]
    


    context={
        'blogs':blogs,
        'atts':atts,
        'att3':att3,
        'destinations':destinations
    }
    return render(request, 'index.html',context)


def destinations(request):
    atts=Park.objects.all().order_by('-id')[:3]
    attractions=Park.objects.all().order_by('-id')[3:]
    context={
        'attractions':attractions,
        'atts':atts
    }
    return render(request, 'destinations.html',context)

def atts(request):
    atts=Attraction.objects.all().order_by('-id')[:3]
    attractions=Attraction.objects.all().order_by('-id')[3:]
    context={
        'attractions':attractions,
        'atts':atts
    }
    return render(request, 'attractions.html',context)

@login_required
def adminatt(request):
    if request.user.is_staff:

        form = AttractionForm()

        if request.method == "POST":
            form = AttractionForm(request.POST, request.FILES)
            files = request.FILES.getlist('more_attraction_images')
            if form.is_valid():
                attraction = form.save()
                for f in files:
                    attraction_image = AttractionImages(attraction=attraction, image=f)
                    attraction_image.save()
                messages.success(request, "Attraction was added successfully")
                return redirect('admin_home')    
        context = {
            'form': form,
        }
        return render(request, 'adminn/add.html', context)   


@login_required
def adminhome(request):
    if request.user.is_staff:
        atts_list = Attraction.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(atts_list, 15)
        try:
            attractions = paginator.page(page)
        except PageNotAnInteger:
            attractions = paginator.page(1)
        except EmptyPage:
            attractions = paginator.page(paginator.num_pages)  
        context = {
            'attractions':attractions,
            'attractions':attractions,
        }
        return render(request, 'adminn/dashboard.html', context)
    return redirect('home') 

@login_required
def adminpark(request):
    if request.user.is_staff:

        form = ParkForm()

        if request.method == "POST":
            form = ParkForm(request.POST, request.FILES)
            files = request.FILES.getlist('more_park_images')
            if form.is_valid():
                park = form.save()
                for f in files:
                    park_image = ParkImages(park=park, image=f)
                    park_image.save()
                messages.success(request, "Destination was added successfully")
                
                return redirect('admin_destinations')    
        context = {
            'form': form,
        }
        return render(request, 'adminn/add.html', context)  


@login_required 
def admin_blogs(request):
    if request.user.is_staff:
        blog_list = Blog.objects.filter(approved=False).order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(blog_list, 15)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)  

        context = {
            'blogs':blogs,
        }  
        return render(request, 'adminn/blogs.html', context)    

@login_required 
def admin_rsvps(request):
    if request.user.is_staff:
        blog_list = VisitAttraction.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(blog_list, 15)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)  

        context = {
            'blogs':blogs,
        }  
        return render(request, 'adminn/rsvp.html', context) 


@login_required 
def admin_bookings(request):
    if request.user.is_staff:
        blog_list = Book.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(blog_list, 15)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)  

        context = {
            'blogs':blogs,
        }  
        return render(request, 'adminn/bookings.html', context)   

@login_required 
def admin_destinations(request):
    if request.user.is_staff:
        parks_list = Park.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(parks_list, 15)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)  

        context = {
            'blogs':blogs,
        }  
        return render(request, 'adminn/destinations.html', context)
@login_required 
def admin_messages(request):
    if request.user.is_staff:
        parks_list = Contact.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(parks_list, 15)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)  

        context = {
            'blogs':blogs,
        }  
        return render(request, 'adminn/messages.html', context)


def edit_att(request, id):
    att = get_object_or_404(Attraction, id = id)
    form = AttractionForm(instance=att)
    if request.method == "POST":
        form = AttractionForm(request.POST or None, instance=att)
        if form.is_valid():
            form.save()
            messages.success(request, "Attraction was updated successfully")
            return redirect('admin_home')
    context = {
        'att':att,
        'form':form,
    }
    return render(request, 'adminn/add.html', context)  


def edit_park(request, id):
    park = get_object_or_404(Park, id = id)
    form = ParkForm(instance=park)
    if request.method == "POST":
        form = ParkForm(request.POST or None, instance=park)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination was updated successfully")
            return redirect('admin_destinations')
    context = {
        'park':park,
        'form':form,
    }
    return render(request, 'adminn/add.html', context)  

@login_required
def delete_att(request, id):
    att = get_object_or_404(Attraction, id = id)
    att.delete()
    messages.success(request, "Attraction was deleted successfully")
    return redirect('admin_home')

@login_required
def delete_visit(request, id):
    att = get_object_or_404(VisitAttraction, id = id)
    att.delete()
    messages.success(request, "Booking was deleted successfully")
    return redirect('admin_rsvps')

@login_required
def delete_dest(request, id):
    att = get_object_or_404(Book, id = id)
    att.delete()
    messages.success(request, "Booking was deleted successfully")
    return redirect('admin_reservations')

@login_required
def delete_park(request, id):
    park = get_object_or_404(Park, id = id)
    park.delete()
    messages.success(request, "Destination was deleted successfully")
    return redirect('admin_destinations')

@login_required
def delete_message(request, id):
    park = get_object_or_404(Contact, id = id)
    park.delete()
    messages.success(request, "Message was deleted successfully")
    return redirect('admin_messages')

class LikeAtt(generic.View):
    def post(self, request, id ,*args, **kwargs):
        att= get_object_or_404(Attraction, id=id)


        is_liked=False

        for like in att.likes.all():
            if like == request.user:
                is_liked=True
                break
        if not is_liked:
            att.likes.add(request.user)

        if is_liked:
            att.likes.remove(request.user)   

        next=request.POST.get('next', '/')
        return HttpResponseRedirect(next)




def search(request):
    q = request.GET['q']
    if q:
        context = {
            'data' : Attraction.objects.filter(name__icontains=q).order_by('-id'),
            'rel_blogs' : Blog.objects.filter(snippet__icontains=q ).order_by('-id'),
        }

        return render(request, 'search.html', context)
    return redirect('attractions')  



@login_required
def user_profile(request):
    if request.user.is_authenticated:
        user=request.user
        blogs=Blog.objects.filter(author=user).order_by('-id')

        form = BlogForm() 
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                blog = form.save(commit=False)   
                blog.author = request.user
                blog.save()

        context={
            'blogs':blogs,
            'form':form
        }
        return render(request, 'dashboard.html', context)

    return redirect('home')  


@login_required
def book_destination(request, id):
    if request.user.is_authenticated:
        park = get_object_or_404(Park, id=id)
        form = BookDestinationForm() 
        if request.method == "POST":
            form = BookDestinationForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                blog = form.save(commit=False)   
                blog.user = request.user
                blog.park = park

                blog.save()
                messages.success(request, "Booked successfully")
                return redirect('destinations')
    
        context = {
            'form':form,
            'park':park
        }
        return render(request, 'form.html', context)
        
        
def contact(request):
    form = ContactForm() 
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        
        
        if form.is_valid():  
            form.save() 
            messages.success(request, "Your message was send succesfully")
            return redirect('contact')

    context = {
        'form':form,
    }
    return render(request, 'form.html', context)        


@login_required
def visit_attraction(request, id):
    if request.user.is_authenticated:
        attraction = get_object_or_404(Attraction, id=id)
        form = VisitAttractionForm() 
        if request.method == "POST":
            form = VisitAttractionForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                visit = form.save(commit=False)   
                visit.user = request.user
                visit.attraction = attraction

                visit.save()
                messages.success(request, "Booked successfully")
                return redirect('attractions')
    
        context = {
            'form':form,
            'attraction':attraction
        }
        return render(request, 'form.html', context)

def reply_book(request, id):
        # att = get_object_or_404(VisitAttraction, id = id)
    att = get_object_or_404(Book, id = id)
    user=att.user
    mess='See you soon'
    messag=Reply.objects.create(user=user, message=mess)
    messages.success(request, "Reply send successfully")

    return redirect('admin_reservations')     

def reply_visit(request, id):
        # att = get_object_or_404(VisitAttraction, id = id)
    att = get_object_or_404(VisitAttraction, id = id)
    user=att.user
    mess='See you soon'
    messag=Reply.objects.create(user=user, message=mess)
    messages.success(request, "Reply send successfully")

    return redirect('admin_rsvps')


@login_required
def user_mesages(request):
    user=request.user
    blogs=Reply.objects.filter(user=user)
    parks_list = Reply.objects.filter(user=user).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(parks_list, 15)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)  



    context={
        'blogs':blogs
    }
    return render(request, 'user-mess.html', context)

@login_required
def delete_reply(request, id):
    park = get_object_or_404(Reply, id = id)
    park.delete()
    messages.success(request, "Reply was deleted successfully")
    return redirect('user_mesages')

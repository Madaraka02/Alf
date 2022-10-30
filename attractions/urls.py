
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),

    path('travel/admin/', adminhome, name='admin_home'),

    path('travel/admin/add-attraction', adminatt, name='add_att'),
    path('travel/admin/add-destination', adminpark, name='add_dest'),

    path('travel/admin/blogs/', admin_blogs, name='admin_blogs'),
    path('travel/admin/messages/', admin_messages, name='admin_messages'),
    path('travel/admin/destination/bookings/', admin_bookings, name='admin_reservations'),
    path('travel/admin/attraction/bookings/', admin_rsvps, name='admin_rsvps'),



    path('travel/admin/destinations/', admin_destinations, name='admin_destinations'),
    path('user/profile/', user_profile, name='user_profile'),
    path('attractions/', atts, name='attractions'),
    path('destinations/', destinations, name='destinations'),
    path('destinations/<int:id>/book/', book_destination, name='book_destination'),
    path('attractions/<int:id>/like/', LikeAtt.as_view(), name='like_att'),
    path('attractions/<int:id>/update/', edit_att, name='edit_att'),
    path('attractions/<int:id>/delete/', delete_att, name='delete_att'),

    path('destinations/<int:id>/update/', edit_park, name='edit_park'),
    path('destinations/<int:id>/delete/', delete_park, name='delete_park'),
    path('boooking/<int:id>/delete/', delete_dest, name='delete_dest'),
    path('visit/<int:id>/delete/', delete_visit, name='delete_visit'),

    path('messages/<int:id>/delete/', delete_message, name='delete_message'),

    path('attractions/<int:id>/book-visit/', visit_attraction, name='visit_attraction'),





]




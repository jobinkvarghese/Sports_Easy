from django.contrib import admin
from . models import User_regtbl
from . models import add_to_cart_table,posts_tbl,turf_booking_tbl,Placeoreder,OrderItem,OrderTable
from . models import Booking,complaint_reg_tbl,book_event_tbl,Academy_admission_tbl,comments_tbl
# Register your models here.
admin.site.register(User_regtbl)
admin.site.register(add_to_cart_table)
admin.site.register(Booking)
admin.site.register(complaint_reg_tbl)
admin.site.register(book_event_tbl)
admin.site.register(Academy_admission_tbl)
admin.site.register(posts_tbl)
admin.site.register(comments_tbl)
admin.site.register(turf_booking_tbl)
admin.site.register(Placeoreder)
admin.site.register(OrderItem)
admin.site.register(OrderTable)
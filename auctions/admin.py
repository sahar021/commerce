from django.contrib import admin
from .models import User, Product, Auction, Watchlist, Bid, Chat
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Chat)

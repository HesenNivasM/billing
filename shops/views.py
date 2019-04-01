from django.shortcuts import render
from .models import Shops

def shopsPanel(request):
    return render(request, 'shops/shopsPanel.html')

def viewShops(request):
    if request.method == "POST" and request.POST.get('selectShop'):
        shopId = request.POST.get('shop')
        request.session['shopId'] = shopId
        shopData = Shops.objects.filter(id=shopId)
        shops = Shops.objects.all()
        return render(request, 'shops/viewShops.html',{
            "shopData" : shopData[0],
            "shops" : shops
        },content_type="text/html")
    shops = Shops.objects.all()
    return render(request, 'shops/viewShops.html',{
        "shops" : shops
    },content_type="text/html")

def updateShops(request):
    if request.method == "POST" and request.POST.get('updateShop'):
        data = Shops.objects.get(id=request.session.get('shopId'))
        name = request.POST.get('name')
        ownerName = request.POST.get('ownerName')
        gstNo = request.POST.get('gstNo')
        areaCode = int(request.POST.get('areaCode'))
        address = request.POST.get('address')
        phoneNo = request.POST.get('phoneNo')
        data.name = name
        data.ownerName = ownerName
        data.gstNo = gstNo
        data.areaCode = areaCode
        data.address = address
        data.phoneNo = phoneNo
        data.save()
        shops = Shops.objects.all()
        return render(request, 'shops/updateShops.html',{
            "return_message" : "The Shop details has been updated successfully",
            "shops" : shops
        },content_type="text/html")
    if request.method == "POST" and request.POST.get('selectShop'):
        shopId = request.POST.get('shop')
        request.session['shopId'] = shopId
        shopData = Shops.objects.filter(id=shopId)
        shops = Shops.objects.all()
        return render(request, 'shops/updateShops.html',{
            "shopData" : shopData[0],
            "shops" : shops
        },content_type="text/html")    
    shops = Shops.objects.all()
    return render(request, 'shops/updateShops.html',{
        "shops" : shops
    },content_type="text/html")

def createShops(request):
    if request.method == "POST":
        name = request.POST.get('name')
        ownerName = request.POST.get('ownerName')
        gstNo = request.POST.get('gstNo')
        areaCode = int(request.POST.get('areaCode'))
        address = request.POST.get('address')
        phoneNo = request.POST.get('phoneNo')
        data = Shops()
        data.name = name
        data.ownerName = ownerName
        data.gstNo = gstNo
        data.areaCode = areaCode
        data.address = address
        data.phoneNo = phoneNo
        data.save()
        return render(request, 'shops/createShops.html',{
            "return_message" : "Shop has been added Successfully"
        },content_type="text/html")    
    return render(request, 'shops/createShops.html')
from django.shortcuts import render, redirect
from stocks.models import Stocks
from shops.models import Shops
from .models import BillDetails, Transactions
import json

def billPanel(request):
    return render(request, 'bills/billPanel.html')

def viewBill(request):
    if request.method == "POST" and request.POST.get('billNumber'):
        billsData = BillDetails.objects.filter(billNo = request.POST.get('billNumber'))
        grandTotal = 0.0
        for billData in billsData:
            grandTotal += float(billData.itemTotal)
        bills = BillDetails.objects.all()
        stocks = Stocks.objects.all()
        shops = Shops.objects.all()
        return render(request, 'bills/viewBill.html',{
            "grandTotal" : grandTotal,
            "stocks" : stocks,
            "shops" : shops,
            "bills" : bills,
            "billsData" : billsData,
            "templateBillsData" : billsData[0],
        },content_type="text/html")
    bills = BillDetails.objects.all()
    return render(request, 'bills/viewBill.html',{
        "bills":bills,
    },content_type="text/html")

def createBill(request):
    if request.method == "POST": #increment the bill number
        billNo = request.session.get('billNo')
        billDate = request.POST.get("billDate")
        shopId = request.POST.get("shopname")
        grandTotal = 0
        for i in range(1,100):     
            if(request.POST.get(str(i)+"_name")):
                print("hai")
                name = request.POST.get(str(i)+"_name")
                hsnCode = request.POST.get(str(i)+"_hsnCode")
                quantity = request.POST.get(str(i)+"_quantity")
                mrp = request.POST.get(str(i)+"_mrp")
                rate = request.POST.get(str(i)+"_rate")
                scheme = request.POST.get(str(i)+"_scheme")
                gst = request.POST.get(str(i)+"_gst")
                total = request.POST.get(str(i)+"_total")
                #Save each Bill Detail
                data = BillDetails()
                data.billNo = billNo
                data.billDate = str(billDate)
                data.shopId = shopId
                data.itemName = name
                data.itemRate = rate
                data.itemHsnCode = hsnCode
                data.itemQuantity = quantity
                data.itemMrp = mrp
                data.itemGst = gst
                data.itemScheme = scheme
                data.itemTotal = total
                data.save()
                #Calculate Grand Total to store in Transcations
                grandTotal += float(total)
                #Reduce the purchased items from Stocks
                item = Stocks.objects.get(id = int(name))
                item.quantity = item.quantity - int(quantity)
                item.save()
            else:
                break 
        #Add a Transcation
        t = Transactions()
        t.billNo = billNo           
        t.shopId = shopId
        t.date = str(billDate)
        t.total = str(grandTotal)
        t.save()
        #Update the balance
        s = Shops.objects.get(id = shopId)
        s.balance = str(float(s.balance) + float(grandTotal))
        s.save()
        #increment the bill value
        with open("bills/static/count.json", 'r+') as f: #read the bill number
            j = json.load(f)
            j['count'] = int(j['count']) + 1
            f.seek(0)
            json.dump(j, f, indent=4)
            f.truncate()

    data = Stocks.objects.all()
    shops = Shops.objects.all()
    j = ""
    with open("bills/static/count.json", 'r+') as f: #read the bill number
        j = json.load(f)
        # j['id'] = 134 
        f.seek(0)
        json.dump(j, f, indent=4)
        f.truncate()
    request.session["billNo"] = j["count"]
    return render(request, 'bills/createBill.html',{
        "billNo" : j["count"],
        "data" : data,
        "shops" : shops,
    },content_type="text/html")
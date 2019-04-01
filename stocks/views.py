from django.shortcuts import render
from .models import Stocks

def stocksPanel(request):
    return render(request, 'stocks/stocksPanel.html')

def viewStocks(request):
    if request.method == "POST" and request.POST.get('selectStock'):
        stockId = request.POST.get('stock')
        request.session['stockId'] = stockId
        stockData = Stocks.objects.filter(id=stockId)
        stocks = Stocks.objects.all()
        return render(request, 'stocks/viewStocks.html',{
            "stockData" : stockData[0],
            "stocks" : stocks
        },content_type="text/html")
    stocks = Stocks.objects.all()
    return render(request, 'stocks/viewStocks.html',{
        "stocks" : stocks
    },content_type="text/html")

def updateStocks(request):
    if request.method == "POST" and request.POST.get('updateStock'):
        data = Stocks.objects.get(id=request.session.get('stockId'))
        name = request.POST.get('name')
        hsnCode = request.POST.get('hsnCode')
        mrp = request.POST.get('mrp')
        quantity = int(request.POST.get('quantity'))
        gst = request.POST.get('gst')
        stockCode = request.POST.get('stockCode')
        data.name = name
        data.hsnCode = hsnCode
        data.quantity = quantity
        data.mrp = mrp
        data.gst = gst
        data.stockCode = stockCode
        data.save()
        stocks = Stocks.objects.all()
        return render(request, 'stocks/updateStocks.html',{
            "return_message" : "The Stock details has been updated successfully",
            "stocks" : stocks
        },content_type="text/html")
    if request.method == "POST" and request.POST.get('selectStock'):
        stockId = request.POST.get('stock')
        request.session['stockId'] = stockId
        stockData = Stocks.objects.filter(id=stockId)
        stocks = Stocks.objects.all()
        return render(request, 'stocks/updateStocks.html',{
            "stockData" : stockData[0],
            "stocks" : stocks
        },content_type="text/html")    
    stocks = Stocks.objects.all()
    return render(request, 'stocks/updateStocks.html',{
        "stocks" : stocks
    },content_type="text/html")

def createStocks(request):
    if request.method == "POST":
        name = request.POST.get('name')
        hsnCode = request.POST.get('hsnCode')
        mrp = request.POST.get('mrp')
        quantity = int(request.POST.get('quantity'))
        gst = request.POST.get('gst')
        stockCode = request.POST.get('stockCode')
        data = Stocks()
        data.name = name
        data.hsnCode = hsnCode
        data.quantity = quantity
        data.mrp = mrp
        data.gst = gst
        data.stockCode = stockCode
        data.save()
        return render(request, 'stocks/createStocks.html',{
            "return_message" : "Stock has been added Successfully"
        },content_type="text/html")    
    return render(request, 'stocks/createStocks.html')
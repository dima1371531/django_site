from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from mainApp.models import Users,Cart,Product

# Create your views here.
from django.contrib import auth


def index(request):
    # return render(request,'login.html')
    products=Product.objects.all()
    return render(request,'product_list_extended.html',{'products':products})

def register(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = Users.objects.create_user(username=username, password=password, email=email)
        user.save()

        auth.login(request, user)
        return HttpResponseRedirect("/product_list")

    return render(request, 'registration.html')

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/product_list")

    return render(request, 'login.html')

def show_cart(request):

    user = request.user
    try:
        Cart.objects.get(User=user)
    except:
        cart = Cart(User=user)
        cart.save()
    cart=Cart.objects.get(User=user)
    products = cart.ProdList.all()
    total=0
    for product in products:
        total+=product.Price
    return render(request, 'shoping_cart_extended.html', {'products': products,'total':total})

def add_to_cart(request, id):
    if request.user.is_authenticated:
        print('entered if')
        user = request.user
        product = Product.objects.get(id = id)
        try:
            Cart.objects.get(User=user)
        except:
            cart = Cart(User=user)
            cart.save()
        currCart=Cart.objects.get(User=user)
        currCart.ProdList.add(product)
        currCart.save()
        return redirect('index')
    else:
        return redirect('login')



def delete_product(request, id):
    if request.user is not None:
        user = request.user
        product = Product.objects.get(id = id)
        try:
            Cart.objects.get(User=user)
        except:
            cart = Cart(User=user)
            cart.save()
        currCart=Cart.objects.get(User=user)
        currCart.ProdList.remove(product)
        currCart.save()
        return redirect('show_cart')
    else:

        return redirect('login')

def order(request):
    user = request.user
    try:
        Cart.objects.get(User=user)
    except:
        cart = Cart(User=user)
        cart.save()
    cart = Cart.objects.get(User=user)
    products = cart.ProdList.all()
    total = 0
    for product in products:
        total += product.Price
    if request.method=='POST':
        qiwi_phone = '+79130731008'
        url = 'https://qiwi.com/payment/form/99?extra%5B%27account%27%5D=' + qiwi_phone + '&amountInteger=' + str(
            total) + '&amountFraction=' + str(0) + '&currency=643&blocked[0]=account'
        answer = redirect(url)
        print('redirect on payment')
        return answer
    return render(request, 'chekout_extended.html',{'products': products,'total':total})





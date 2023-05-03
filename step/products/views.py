from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import UserInfo
from .models import Products, Cart, Orders
from .forms import AddProductForm
from datetime import datetime
from datetime import date
# Create your views here.

@login_required(login_url='/')
def add_products(request):

    user_type = UserInfo.objects.get(user=request.user)

    #making sure students cant access
    if user_type.is_student == True:
        messages.warning(request, "You are a student and trying to access the teachers portal")
        return redirect('/')

    
    if request.method == 'POST':
        if request.FILES.get('product_image') == None:
            messages.info(request, "image not found")

             
        else:
            form = AddProductForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                product_name = form.cleaned_data['product_name']
                product_price = form.cleaned_data['product_price']
                product_category = form.cleaned_data['product_category']
                product_image = form.cleaned_data['product_image']
                items_remaining = form.cleaned_data['items_remaining']

                add_product = Products.objects.create(user=user, product_name=product_name, product_price=product_price, product_category=product_category, product_image=product_image, items_remaining=items_remaining)
                

                messages.info(request, "Product Added")
                

                return redirect('all_products')
            
            else:
                messages.info(request, form.errors)

    form = AddProductForm()
    return render(request, 'products/add_products.html', {'user_type':user_type,'form': form,})



@login_required(login_url='/')
def all_products(request):
    user_type = UserInfo.objects.get(user=request.user)
    products = Products.objects.all()
    cart = Cart.objects.filter(user=request.user)

    items = 0

    for item in cart:
        items = items+1

    if request.method == 'POST':
        user = request.user
        product = request.POST['product_id']
        product_obj = Products.objects.get(id=product)
        number_of_items = 1
        total_price = product_obj.product_price
        


        if Cart.objects.filter(user=user,product=product_obj):
            product_cart = Cart.objects.get(user=user,product=product_obj)

            if product_cart.number_of_items < product_obj.items_remaining:
                product_cart.number_of_items = product_cart.number_of_items+1
                product_cart.total_price = product_cart.total_price + product_obj.product_price 
                product_cart.save()

            else:
                messages.warning(request, f"{product_obj.product_name} can't be added anymore, more stock isn't available")


        else:

            add_to_cart = Cart.objects.create(user=user, product=product_obj, number_of_items=number_of_items, total_price=total_price)
            messages.info(request, f"{product_obj.product_name} added to the cart")
            return redirect('all_products')

    if user_type.is_student == True:
        user_profile = UserInfo.objects.get(user=request.user)
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return render(request, 'products/all_products.html', {'user_profile':user_profile, 'today':today,
                        'products': products, 'current_time': current_time, 'items': items})

    else:
        return render(request, 'products/teacher_all_products.html', {'user_type':user_type,
                        'items':items, 'products': products, 'cart':cart,})


@login_required(login_url='/')
def my_cart(request):
    user_profile = UserInfo.objects.get(user=request.user)
    cart = Cart.objects.filter(user=request.user)
    products = Products.objects.all()

    for product in products:
        for item in cart:
            if item.product == product:
                if product.items_remaining == 0 or product.items_remaining < item.number_of_items:
                    delete_from_cart = Cart.objects.get(user=request.user, product=product)
                    delete_from_cart.delete()
                
                    messages.info(request, f"{delete_from_cart} removed from your cart as the required quantity is no longer in stock, please check the products page again")
                    return redirect('my_cart')


    if user_profile.is_student == True:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        return render(request, "products/my_cart.html", {'user_profile':user_profile, 'cart':cart,
                'today':today, 'current_time': current_time,})
    
    else:
        user_type = UserInfo.objects.get(user=request.user)
        return render(request, "products/teacher_my_cart.html", {'user_type':user_type, 'cart':cart,})




@login_required(login_url='/')
def my_orders(request):
    user_type = UserInfo.objects.get(user=request.user)

    if request.method == 'POST':
        cart = Cart.objects.filter(user=request.user)

        for item in cart:
            # check if number of items in cart are more than products remaining
            product = item.product
            
            if product.items_remaining >= item.number_of_items:
           
                user = request.user
                
                number_of_items = item.number_of_items
                total_price = item.total_price

                create_order = Orders.objects.create(user = user, product = product, number_of_items = number_of_items, total_price = total_price)
                empty_cart = cart.delete()

                # decrease number of products from product table 
                product_obj = Products.objects.get(id=product.id)
                product_obj.items_remaining = product_obj.items_remaining - number_of_items
                product_obj.save()

        messages.info(request, "Your order has been placed sucessfully")

        return redirect('my_orders')
    
    else:
        orders = 1

        if Orders.objects.filter(user=request.user):
            orders = Orders.objects.filter(user=request.user)





        if user_type.is_student == True:
            user_profile = UserInfo.objects.get(user=request.user)
            today = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            return render(request, "products/my_orders.html", {'user_profile':user_profile,
                    'today':today, 'current_time': current_time, 'orders': orders})
        

        else:
            return render(request, "products/teacher_my_orders.html", {'user_type':user_type, 'orders': orders})



@login_required(login_url='/')
def increment(request):

    if request.method == 'POST':
        product_id = request.POST['product_id']
        product_obj = Products.objects.get(id=product_id)
        cart_obj = Cart.objects.get(user=request.user, product = product_obj)

        #increment
        cart_obj.number_of_items = cart_obj.number_of_items + 1
        cart_obj.total_price = cart_obj.total_price + product_obj.product_price
        cart_obj.save()
    return redirect('my_cart')





@login_required(login_url='/')
def decrement(request):

    if request.method == 'POST':
        product_id = request.POST['product_id']
        product_obj = Products.objects.get(id=product_id)
        cart_obj = Cart.objects.get(user=request.user, product = product_obj)

        #check if product quantity is 1 in whihc case we'll just delete the object
        if cart_obj.number_of_items == 1:
            cart_obj.delete()
            messages.info(request, f"Removed {product_obj.product_name} from cart")
            return redirect('my_cart')


        cart_obj.number_of_items = cart_obj.number_of_items - 1
        cart_obj.total_price = cart_obj.total_price - product_obj.product_price
        cart_obj.save()
 
    return redirect('my_cart')



@login_required(login_url='/')
def empty_cart(request):
    
    cart = Cart.objects.filter(user = request.user)
    
    
    
    for item in cart:
        delete_cart = Cart.objects.filter(user = request.user).first()
        delete_cart.delete()


    messages.info(request, 'Cart emptied')
    return redirect('all_products')













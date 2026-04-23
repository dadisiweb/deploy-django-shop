from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Order, OrderItem, Cart, CartItem


# ----------------------------
# PRODUCTS
# ----------------------------

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {
        'product': product
    })


# ----------------------------
# CART
# ----------------------------

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart, _ = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    cart_items = []
    total = 0

    for item in items:
        subtotal = item.product.price * item.quantity
        total += subtotal

        cart_items.append({
            "product": item.product,
            "qty": item.quantity,
            "subtotal": subtotal
        })

    return render(request, "shop/cart.html", {
        "cart_items": cart_items,
        "total": total
    })


# ----------------------------
# CHECKOUT
# ----------------------------

@login_required
def checkout(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    if not items.exists():
        return redirect('cart_detail')

    order = Order.objects.create(user=request.user)

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    # clear cart
    items.delete()

    return redirect('order_list')


# ----------------------------
# ORDERS
# ----------------------------

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')

    return render(request, 'shop/orders.html', {
        'orders': orders
    })



# ----------------------------
# AUTH
# ----------------------------

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def increase_qty(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart_detail')

def decrease_qty(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart_detail')

import uuid
from django.shortcuts import redirect, render, get_object_or_404
from cinetpay_sdk.s_d_k import Cinetpay
from django.contrib.auth import get_user_model
from .models import Cart, Order, VenteCars, LivraisonAdresse
from car.models import Vehicule, Piece

User = get_user_model()


from django.urls import reverse

def add_to_cart_car(request, id):
    user = request.user
    vehicule = get_object_or_404(Vehicule, id=id)
    cart, _ = Cart.objects.get_or_create(user=user)
    cart.save()
    order, created = Order.objects.get_or_create(user=user, ordered=False, vehicule=vehicule)

    if created:
        cart.order.add(order)
        cart.save()
    else:
        order.quatity += 1
        order.save()
    return redirect(reverse("car:cars_details", args=[id]))

def add_to_cart_piece(request, id):
    user = request.user
    pieces = get_object_or_404(Piece, id=id)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, piece=pieces)
    if created:
        cart.order.add(order)
        cart.save()
    else:
        order.quatity += 1
        order.save()
    return redirect(reverse("car:pieces_details", args=[id]))



def cart(request):
    cart = Cart.objects.get(user=request.user)

    return render(request, "sell/cart.html", {"orders": cart.order.all(), "total_price": float(cart.get_total_price())})




    

def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    
    return redirect("")











def achatCar(request, id):
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        adresse_livraison = request.POST.get('adresse_livraison')

        articles = cart.order.all()

        all_achat_items = []

        for article in articles:
            if article.vehicule:
                all_achat_items.append(article.vehicule.marque)

            if article.piece:
                all_achat_items.append(article.piece.type_piece)

        description_text = ", ".join(all_achat_items)

        apikey = "1411544841658c7c9c109d46.02803105"
        site_id = "5866737"

        client = Cinetpay(apikey, site_id)

        transaction_id = str(uuid.uuid4())

        data = { 
            'amount': cart.get_total_price(),
            'currency': 'USD', 
            'transaction_id': transaction_id,
            'description': f'Achat de(s) Article(s) suivant: {description_text}',  
            'return_url': f"http://127.0.0.1:8000/sell/confirmations", 
            'notify_url': "http://127.0.0.1:8000", 
            'customer_name': request.user.username,                               
            'customer_surname': request.user.first_name,
            'channels': "ALL",
        }

        response = client.PaymentInitialization(data)

        transaction = VenteCars(
            user=request.user,
            cart=cart,
            amount=data['amount'],
            currency=data['currency'],
            transaction_id=data['transaction_id'],
            description=data['description'],
            return_url=data['return_url'],
            notify_url=data['notify_url'],
            customer_name=data['customer_name'],
            customer_surname=data['customer_surname'],
            channels=data['channels'],
            response=response,
        )
        transaction.save()

        livraison_addresse = LivraisonAdresse(
            cart=cart,
            adresse_livraison = adresse_livraison,
            )
        livraison_addresse.save()

        print(response)

        return redirect(response['data']['payment_url'])

    else:
        return render(request, 'sell/achatVoiture.html')
    

def payment_confirmation(request):
    if request.method == "POST":
        return render(request, 'sell/payment_confirmation.html')
    else:
        return render(request, 'error.html')

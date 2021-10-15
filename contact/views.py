# from django.shortcuts import render

# # Create your views here.

# def contact(request):

#     return render(request, "contact/contact.html")

from django.shortcuts import redirect, render, redirect

from .forms import ContactForm

from django.core.mail import EmailMessage

# Create your views here.


def contact(request):

    contact_form=ContactForm()

    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            content=request.POST.get('content')

            email=EmailMessage(f"Message from *{name}*", 
            "Name: {}\nEmail: {}\nMessage:\n{}".format(name,email,content),
            "",["jonjonyjonjony444@gmail.com"], reply_to=[email])

            try: 
                email.send() #Si hay un error ocurre o no, lo siguiente

                return redirect('/contact/?valido')
            except:
                return redirect('/contact/?novalido')

    return render(request, "contact/contact.html", {'miFormulario':contact_form})


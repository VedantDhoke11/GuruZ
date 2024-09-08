from django.shortcuts import render
from .models import Pandit, User, Booking
from django.shortcuts import redirect
from .forms import PanditRegistrationForm

# Create your views here.

def pandit_list(request):
    pandits = Pandit.objects.all()
    return render(request, 'pandits_list.html', {'pandits': pandits})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

# View to list all Bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings_list.html', {'bookings': bookings})

def pandit_register(request):
    if request.method == 'POST':
        form = PanditRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the Pandit details
            return redirect('home')  # Redirect to a success page
    else:
        form = PanditRegistrationForm()
    return render(request, 'pandit_register.html', {'form': form})
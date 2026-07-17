from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')  # reloads the page after submit
    else:
        form = ReservationForm()
    
    return render(request, 'reservation.html', {'form': form})
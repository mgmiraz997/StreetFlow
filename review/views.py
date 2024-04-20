from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reserve.models import Book
from .forms import ReviewForm
from .models import Book


# Create your views here.
@login_required
def submit_review(request, booking_id):
    context = {}
    booking = get_object_or_404(Book, id=booking_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.user = request.user
            review.save()
            return redirect('seebookings')
    else:
        form = ReviewForm()

    context['form'] = form
    context['booking'] = booking
    return render(request, 'review.html', context)

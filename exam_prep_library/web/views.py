from django.shortcuts import render, redirect, get_object_or_404

from exam_prep_library.web.forms import AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm, CreateProfileForm
from exam_prep_library.web.models import Profile, Book


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_homepage(request):
    profile = get_profile()
    books = Book.objects.all()

    if profile is None:
        return create_profile(request)

    context = {
        'profile': profile,
        'books': books,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = AddBookForm()

    context = {
        'form': form,
    }

    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = EditBookForm(instance=book)

    context = {
        'book': book,
        'form': form,
    }

    return render(request, 'edit-book.html', context)


def show_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    context = {
        'book': book,
    }

    return render(request, 'book-details.html', context)


def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    books = Book.objects.all()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            books.delete()
            profile.delete()
            return redirect('show homepage')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)

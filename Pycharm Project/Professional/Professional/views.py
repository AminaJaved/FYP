from django.shortcuts import render,redirect


def main(request):
    return render(request, 'index.html')


def about(request):
        return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def cancerTypes(request):
    return render(request, 'cancerTypes.html')

def cancer(request):
    return render(request, 'cancer.html')

def treatment(request):
    return render(request, 'treatment.html')

def cancerclassification(request):
    return render(request, 'cancerclassification.html')



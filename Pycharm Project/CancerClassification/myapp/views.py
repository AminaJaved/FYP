from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm, CancerAnalysisForm, CancerClassification,VisualizationForm
from .AllFunctions import SVM_CancerClassification,print_class
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Blog


#render to contact without model.forms



def reg(request):
        return render(request, 'app1/reg.html')


def main(request):
        return render(request, 'app1/main.html')



def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']

            print(name,email,subject)
    form = ContactForm()
    return render(request,'form.html',{'form':form})


#render to contact with model.forms

def snippet_detail(request):
    if request.method=='POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
           form.save()


    form = SnippetForm()
    return render(request, 'form.html', {'form': form})


#cancer classification without data goes in DB
@csrf_exempt
def classify(request):
    if request.method =='POST':
        form = CancerClassification(request.POST)
        if form.is_valid():
            NPFFR1 = float(form.cleaned_data['NPFFR1'])
            TAS2R19 = float(form.cleaned_data['TAS2R19'])
            ADRA2C = float(form.cleaned_data['ADRA2C'])
            SOWAHA = float(form.cleaned_data['SOWAHA'])
            TAS2R60= float(form.cleaned_data['TAS2R60'])
            KRT20 = float(form.cleaned_data['KRT20'])
            AADACL4 = float(form.cleaned_data['AADACL4'])
            NACA2 = float(form.cleaned_data['NACA2'])
            CLDN8 = float(form.cleaned_data['CLDN8'])
            GJC3 = float(form.cleaned_data['GJC3'])
            FEM1A = float(form.cleaned_data['FEM1A'])
            DRD5 = float(form.cleaned_data['DRD5'])
            PABPC3 = float(form.cleaned_data['PABPC3'])
            HIST1H4C = float(form.cleaned_data['HIST1H4C'])
            MC2R = float(form.cleaned_data['MC2R'])

            Gene_array = [NPFFR1,TAS2R19,ADRA2C,SOWAHA,TAS2R60,KRT20,AADACL4,NACA2,CLDN8,GJC3,FEM1A,DRD5,PABPC3,HIST1H4C,MC2R]

            prediction = SVM_CancerClassification(Gene_array)
            class_predicted = print_class(prediction)

            print(prediction)
            print(class_predicted)

    form = CancerClassification()
    return render(request,'cancerclassification.html',{'form':form})


#cancer classification with data goes in DB

def cancer_analysis(request):
    if request.method == 'POST':
        form = CancerAnalysisForm(request.POST)
        if form.is_valid():
           form.save()

    form = CancerAnalysisForm()
    return render(request, 'cancerclassification.html', {'form': form})


#form to visualize the predicted class of cancer


def cancer_visualization(request):
    if request.method == 'POST':
        form = VisualizationForm(request.POST)
        if form.is_valid():
            form.save()

    form = VisualizationForm()
    return render(request, 'CancerVisualization.html', {'form': form})


class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_list.html'


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'



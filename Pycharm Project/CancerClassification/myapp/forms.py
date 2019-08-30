from django import forms
from myapp.models import Snippet,Cancer,visualise
from crispy_forms.helper import  FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')
        )

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name','body')


class CancerClassification(forms.Form):
    NPFFR1 = forms.CharField()
    TAS2R19 = forms.CharField()
    ADRA2C = forms.CharField()
    SOWAHA = forms.CharField()
    TAS2R60 = forms.CharField()
    KRT20 = forms.CharField()
    AADACL4 = forms.CharField()
    NACA2 = forms.CharField()
    CLDN8 = forms.CharField()
    GJC3 = forms.CharField()
    FEM1A = forms.CharField()
    DRD5 = forms.CharField()
    PABPC3 = forms.CharField()
    HIST1H4C = forms.CharField()
    MC2R = forms.CharField()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'NPFFR1',
            'TAS2R19',
            'ADRA2C',
            'SOWAHA',
            'TAS2R60',
            'KRT20',
            'AADACL4',
            'NACA2',
            'CLDN8',
            'GJC3',
            'FEM1A',
            'DRD5',
            'PABPC3',
            'HIST1H4C',
            'MC2R',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class CancerAnalysisForm(forms.ModelForm):
    class Meta:
        model = Cancer

        fields = ('NPFFR1','TAS2R19','ADRA2C','SOWAHA','TAS2R60','KRT20','AADACL4','NACA2','CLDN8','GJC3','FEM1A','DRD5','PABPC3','HIST1H4C','MC2R')
        widgets = {
            'NPFFR1': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'TAS2R19': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'ADRA2C': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'SOWAHA': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'TAS2R60': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'KRT20': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'AADACL4': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'NACA2': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'CLDN8': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'GJC3': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'FEM1A': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'DRD5': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'PABPC3': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'HIST1H4C': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'MC2R': forms.TextInput(attrs={'class': 'myfieldclass'}),

        }
class VisualizationForm(forms.ModelForm):
    class Meta:
        model = visualise
        fields = ('Cancer_Class','Description','Symptoms','image')




from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="MAIN"),
    path("reg", views.reg, name="REG"),



    #contact us
    path('contact', views.contact),
    #classify cancer without data in db
    path('classify', views.classify),
    #contact us with DB
    path('snippet', views.snippet_detail),
    #classify cancer with data in db
    path('cancer', views.cancer_analysis),
    #Visualization with data in db
    path('visualize', views.cancer_visualization, name='visualize'),
    #Blog
    path('BLOG-LIST', views.BlogList.as_view(), name='BLOG-LIST'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),

]

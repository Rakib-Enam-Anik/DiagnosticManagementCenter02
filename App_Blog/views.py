from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Blog.models import  Blog, Comment, Likes 
from django.urls import reverse, reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Blog.forms import CommentForm
import uuid

# Create your views here.

def blog_list(request):
    return render(request, 'App_Blog/blog_list.html', context={}) 

from django.shortcuts import render
from .models import Titanic
from .forms import TitanicForm
from django.http import HttpResponse, JsonResponse
import joblib
import os

# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

def predict(request):
    if request.method == "GET":
        form = TitanicForm(request.POST)
        return render(
            request,
            'single_pages/predict.html',
            {"titanic_form": form})

    elif request.method == "POST":
        model_dc = joblib.load('./titanic_model/decision_tree_model.pkl')
        model_knn = joblib.load('./titanic_model/knn_model.pkl')
        model_rf = joblib.load('./titanic_model/random_forest_model.pkl')
        form = TitanicForm(request.POST)
        data = request.data.dict()

        return HttpResponse(status=200, data={})
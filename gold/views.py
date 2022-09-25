from django.shortcuts import render ,redirect
import random 	

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request,'index.html')
    

def process(request):
    if request.POST['action'] == 'Farm' or 'Cave' or 'House' in request.POST:
        random_number = random.randint(10, 20)
        request.session['gold'] += random_number
    if request.POST['action'] == 'Quest':
        random_number = random.randint(-50, 50)
        request.session['gold']  += random_number
    return redirect('/')


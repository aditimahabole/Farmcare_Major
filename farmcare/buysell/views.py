from django.core.paginator import Paginator
import fertilizer_prediction2
from django.shortcuts import redirect, render
from buysell.models import Form,MandiDetails
import requests
import joblib
import tensorflow as tf
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

print('--------Inside buysell views.py-----------')

# ---------CNN FERTILIZER--------------
def cnn_fertilizer(request):
    print("---inside cnn_fertilizer----")
    tf.compat.v1.disable_eager_execution()
    filename = "fertilizer_model.sav"
    cl = joblib.load(filename)
    input_data = pd.DataFrame({
        'Ca': [float(request.POST.get('ca'))],
        'Mg': [float(request.POST.get('mg'))],
        'K': [float(request.POST.get('k'))],
        'S': [float(request.POST.get('s'))],
        'N': [float(request.POST.get('n'))],
        'Lime': [float(request.POST.get('lime'))],
        'C': [float(request.POST.get('c'))],
        'P': [float(request.POST.get('p'))],
        'Moisture': [float(request.POST.get('moisture'))]
    })
    
    prediction = cl.predict(input_data)
    s = "The predicted class of fertilizer is: {}".format(prediction[0])
    return render(request, 'fertilizer_result.html', {'ans': s})
# ---------POST--------------
def post(request):
    print("---inside post----")
    username = request.user.username
    print('username is ',username)
    name = request.POST.get('name')
    phone_no = request.POST.get('phone_no')
    city = request.POST.get('city')
    state = request.POST.get('state')
    crop_name = request.POST.get('crop_name')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    user = User.objects.get(username = username)
    temp = Form(user = user,name=name, phone_no=phone_no, city=city,
                state=state, crop_name=crop_name, quantity=quantity, price=price)
    temp.save()
    # time.sleep(5)
    return redirect('home')
# ---------DISPLAY--------------
def display(request):
    print("---inside display----")
    obj = Form.objects.all()
    context = {
        'obj': obj,
    }
    
    return render(request, 'sell.html', context)
    # return render(request, 'sell.html', locals())
# ---------GET HOME--------------
@login_required(login_url='login_page')
def gethome(request):
    print("---inside get_home----")
    return render(request, 'index.html')
# ---------GET LIST--------------
def getlist(request):
    print("---inside get_result----")
    return render(request, 'list.html')
# ---------GET RECOMMENDATION OF CROPS--------------
def get_recommendation(request):
    print("---inside get_recommendation----")
    return render(request, 'recommend.html')
# ----------GET PREDICTION OF FERTILIZER-------------
def get_prediction(request):
    print("---inside get_prediction----")
    return render(request, 'fprediction.html')
# ---------GET CROP RESULT--------------

def get_crop_result(request):
    print("---inside get_cropresult----")
    cls = joblib.load('final_model.sav')
    lis = []
    lis.append(request.POST.get('n'))
    lis.append(request.POST.get('p'))
    lis.append(request.POST.get('k'))
    lis.append(request.POST.get('temp'))
    lis.append(request.POST.get('hum'))
    lis.append(request.POST.get('ph'))
    lis.append(request.POST.get('rain'))
    ans = cls.predict([lis])
    s = ""
    s = s.join(ans)
    return render(request, 'crop_result.html', {'ans': s})
# ---------GET FERTILIZER RESULT--------------
def get_fertilizer_result(request):
    print("---inside get_fertilizer----")
    cls = joblib.load('fertilizer_model.sav')
    lis = []
    lis.append(request.POST.get('ca'))
    lis.append(request.POST.get('mg'))
    lis.append(request.POST.get('k'))
    lis.append(request.POST.get('s'))
    lis.append(request.POST.get('n'))
    lis.append(request.POST.get('lime'))
    lis.append(request.POST.get('c'))
    lis.append(request.POST.get('p'))
    lis.append(request.POST.get('moisture'))
    ans = str(cls.predict([lis]))
    s = ""
    s = s.join(ans)
    return render(request, 'fertilizer_result.html', {'ans': s})
# ---------MANDI LIVE--------------
def live(request):
    main_url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset="
    end_url = "&limit=10"
    data = []
    search_word = request.POST.get('search')
    selected= request.POST.get('option_selected')
    for offset in range(0, 90, 10):
        url = main_url + str(offset) + end_url
        response = requests.get(url).json()
        # data += response["records"]
        # date_format = data[offset]['arrival_date'].split('-')
        # date_str =date_format[2]+"-"+date_format[1]+"-"+date_format[0];
        # date_str = str(date_str)
        # temp = MandiDetails(state=data[offset]['state'],
        #                   district=data[offset]['district'],
        #                   market=data[offset]['market'],
        #                   commodity=data[offset]['commodity'],
        #                   variety=data[offset]['variety'],
        #                   grade = data[offset]['grade'],
        #                   arrival_date = date_str,
        #                   min_price = str(data[offset]['min_price']),
        #                   max_price = str(data[offset]['max_price']),
        #                   modal_price = str(data[offset]['modal_price'])
        #                   )
        # temp.save()
    queryset = MandiDetails.objects.all()
    if search_word!= None and selected == "1":
        print('inisde 1')
        queryset = queryset.filter(state__icontains = search_word )
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "2":
        print('inisde 2')
        queryset = queryset.filter(district__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "3":
        print('inisde 3')
        queryset = queryset.filter(market__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        pagination_size = min(len(queryset), 10)
        p = Paginator(queryset,pagination_size)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected =="4":
        print('inisde 4')
        queryset = queryset.filter(commodity__icontains = search_word)
        print(queryset)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        pagination_size = min(len(queryset), 10)
        print('pagiiiiiii : ', pagination_size)
        p = Paginator(queryset,pagination_size)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "5":
        print('inisde 5')
        queryset = queryset.filter(variety__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "6":
        print('inisde 6')
        queryset = queryset.filter(arrival_date__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "7":
        print('inisde 7')
        queryset = queryset.filter(min_price__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "8":
        print('inisde 8')
        queryset = queryset.filter(max_price__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})
    
    elif search_word!= None and selected == "9":
        print('inisde 9')
        queryset = queryset.filter(modal_price__icontains = search_word)
        if(len(queryset) == 0):
            print('oops not present')
            return render(request, 'mandi_live.html', {'response': '0'})
        p = Paginator(queryset,10)
        page = request.GET.get('page')
        record = p.get_page(page)
        return render(request, 'mandi_live.html', {'response': record})   
            
    p = Paginator(queryset, 10)
    page = request.GET.get('page')
    record = p.get_page(page)
    return render(request, 'mandi_live.html', {'response': record})
# -------------------LOGIN PAGE--------------------------------
def login_page(request):
    if request.method == "POST":
        password = request.POST.get('password')
        username = request.POST.get('username')
        check_u =  User.objects.filter(username=username).first()
        
        if check_u is None:
            print('user not found')
            messages.error(request, 'Invalid Credentials!')
            return redirect('login_page')
        
        check_p = check_password(password, check_u.password)
        
        if not check_p:
            print('password is incorrect')
            messages.error(request, 'Invalid Credentials!')
            return redirect('login_page')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, 'login.html')
# --------------------REGISTER PAGE-----------------------------
def register_page(request):
    print('inside register page---------')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = User.objects.filter(username = username)
        if user.exists():
            print('bhai kya hora')
            messages.error(request,'Username already exists!')
            return redirect('register_page')
        hashed_password = make_password(password)
        print('pass is : ',hashed_password)
            
        user = User.objects.create(
            first_name= first_name,
            username = username,
            password = hashed_password
        )
        user.save()
        messages.success(request,'Account created Successfully!')
        print('Done register page---------')
        return redirect('login_page')
        
    return render(request,'register.html')
# ---------------LOGOUT-----------------------
def logout_page(request):
    print('user loged out')
    logout(request)
    return redirect('login_page')
# ------------------------------------------------------------------------------------------------------------
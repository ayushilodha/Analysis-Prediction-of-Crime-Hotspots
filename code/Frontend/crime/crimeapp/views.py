from django.shortcuts import render,redirect
from.forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import RandomOverSampler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registeration Sucessufull.')
            return redirect("login")
        messages.error(
            request, "Unsuccessful rregistraion"
            
        )
    form = NewUserForm()
    return render(request=request, template_name='register.html', context={'register_form': form})


# login page

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("userhome")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name= 'login.html', context={"login_form": form})


def userhome(request):
    return render(request,'userhome.html')

def view(request):
    global df
    df = pd.read_excel('crimeapp/20230320020226crime_data_extended_entries.xlsx')
    col = df.head(100).to_html
    return render(request, "view.html", {'table': col})


def moduless(request):
    global df,x_train, x_test, y_train, y_test
    df = pd.read_excel('crimeapp/20230320020226crime_data_extended_entries.xlsx')
    #Delete a unknown column
    df.drop("date",axis=1,inplace=True)
    df.drop("time_of_day",axis=1,inplace=True)
    df.drop("latitude",axis=1,inplace=True)
    df.drop("longitude",axis=1,inplace=True)
    le = LabelEncoder()
    col = df[['crime_type','location','victim_gender','perpetrator_gender','weapon','injury','weather','previous_activity']]
    for i in col:
        df[i]=le.fit_transform(df[i])
    x = df.drop(['crime_type'], axis = 1) 
    y = df['crime_type']
    Oversample = RandomOverSampler(random_state=72)
    x_sm, y_sm = Oversample.fit_resample(x[:100],y[:100])
    x_train, x_test, y_train, y_test = train_test_split(x_sm, y_sm, test_size = 0.3, random_state= 72) 
    if request.method == "POST":
        model = request.POST['algo']

        if model == "1":
            re = RandomForestClassifier(random_state=72)
            re.fit(x_train,y_train)
            re_pred = re.predict(x_test)
            ac = accuracy_score(y_test,re_pred)
            ac
            msg='Accuracy of RandomForest : ' + str(ac)
            return render(request,'moduless.html',{'msg':msg})
        elif model == "2":
            de = DecisionTreeClassifier()
            de.fit(x_train,y_train)
            de_pred = de.predict(x_test)
            ac1 = accuracy_score(y_test,de_pred)
            ac1
            msg='Accuracy of Decision tree : ' + str(ac1)
            return render(request,'moduless.html',{'msg':msg})
        elif model == "3":
            gd = GradientBoostingClassifier()
            gd.fit(x_train,y_train)
            gd_pred = gd.predict(x_test)
            bc = accuracy_score(y_test,gd_pred)
            bc
            msg='Accuracy of GradientBoostingClassifier : ' + str(bc)
            return render(request,'moduless.html',{'msg':msg})
    return render(request,'moduless.html')


def prediction(request):
    try:
        global df,x_train, x_test, y_train, y_test

        if request.method == 'POST':
            a = float(request.POST['f1'])
            # b = float(request.POST['f2'])
            # c = float(request.POST['f3'])
            d = float(request.POST['f4'])
            e = float(request.POST['f5'])
            f = float(request.POST['f6'])
            g = float(request.POST['f7'])
            h = float(request.POST['f8'])
            i = float(request.POST['f9'])
            j = float(request.POST['f10'])
            k = float(request.POST['f11'])
            l = float(request.POST['f12'])
            
            l = [[a,d,e,f,g,h,i,j,k,l]]
            de = DecisionTreeClassifier()
            de.fit(x_train,y_train)
            pred = de.predict(l)
            if pred == 0:
                msg = 'Robbery'
            elif pred == 1:
                msg = 'Embezzlement'
            elif pred == 2:
                msg = 'Burglary'
            elif pred == 3:
                msg = 'Vandalism'
            elif pred == 4:
                msg = 'Theft'
            elif pred == 5:
                msg = 'Assault'
            elif pred == 6:
                print('Forgery')
            elif pred == 7:
                msg ='Drug Offense'
            else:
                msg = 'Fraud'
            
            if a == 1:
                lat = 12.9255
                lag = 77.5468
                name = "Banashankari"
            if a == 2:
                lat = 12.9304
                lag = 77.6784
                name = "Bellandur"
            if a == 3:
                lat = 12.8452 
                lag = 77.6602
                name = "Electronic City"
            if a == 4:
                lat = 12.9121  
                lag = 77.6446
                name = "HSR layout"
            if a == 5:
                lat = 12.9784
                lag = 77.6408
                name = "Indiranagar"
            if a == 6:
                lat =  12.9308
                lag =  77.5838
                name = "jayanagar"
            if a == 7:
                lat = 12.9063
                lag = 77.5857
                name = "jp nagar"
            if a == 8:
                lat = 12.9855
                lag = 77.5269
                name = "Kamakshipalya"
            if a == 9:
                lat = 12.9352
                lag = 77.6245
                name = "Koramangala"
            if a == 10:
                lat = 12.9569
                lag = 77.7011
                name = "Marathahalli"
            if a == 11:
                lat = 12.9698
                lag = 77.7500
                name = "White Field"
            if a == 12:
                lat = 13.1155
                lag = 77.6070
                name = "White Field"
    
            print(lat)
            print(lag)
            import folium
            m = folium.Map(location=[19,-12],zoom_start=2)
            folium.Marker([lat,lag],tooltip=name,popup=msg).add_to(m)
            m = m._repr_html_()
            print(msg)
            return render(request,'result.html',{'msg':msg,'m':m})
    except:
        msg = "Please give a required input"
        return render(request,'prediction.html',{'msg':msg})
        

    return render(request,'prediction.html')
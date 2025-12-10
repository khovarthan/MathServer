# Ex.04 Design a Website for Server Side Processing
## Date:10-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html

<html>
<head>
    <title>Mileage Calculator</title>
    <style>
        body 
        {
            background: linear-gradient(rgb(0, 255, 251), black);
        }
        .id1 
        {
            text-align: center;
            color: rgb(0, 0, 0);
        }
        .box 
        {
            text-align: center;
            width: 30%;
            background-color: red;
            border: solid 3px black;
            padding: 20px;
            margin: 50px auto;
        }
        .result 
        {
            font-weight: bold;
        }
    </style>
</head>
<body>
    
    <div class="box">
        <h2><u>Mileage Calculator</u></h2>
        <h3>KHOVARTHAN V (25012253)</h3>

        <form method="post">
            {% csrf_token %}
            <label>Distance Travelled</label>
            <br>
            <input type="number" name="distance"> km
            <br>
            <br>
            <label>Liters Consumed</label>
            <br>
            <input type="number" name="liters"> L
            <br>
            <br>
            <button type="submit">Calculate</button>
            <br>
            <br>
            <label>Mileage</label>
            <br>
            <input class='result' type="number" name="Mileage" value={{miles}}x>Km/L
        </form>
    </div>
</body>
</html>


views.py

from django.shortcuts import render
def mileage(request):
    dist = int(request.POST.get('distance', 0))
    lit = int(request.POST.get('liters', 0))
    miles = dist / lit if request.method == 'POST' and lit != 0 else 0
    print("kilometers =", dist)
    print("liters =", lit)
    print("Mileage =", miles)
    return render(request, 'mathapp/math.html', {'dist': dist, 'lit': lit, 'miles': miles})


urls.py

    from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.mileage, name='mileage'),
]
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (48).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (47).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.

from django.shortcuts import render
def mileage(request):
    dist = int(request.POST.get('distance', 0))
    lit = int(request.POST.get('liters', 0))
    miles = dist / lit if request.method == 'POST' and lit != 0 else 0
    print("kilometers =", dist)
    print("liters =", lit)
    print("Mileage =", miles)
    return render(request, 'mathapp/math.html', {'dist': dist, 'lit': lit, 'miles': miles})
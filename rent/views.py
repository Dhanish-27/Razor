from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import houses
from .forms import HouseForm
from .filters import HouseFilter
# Create your views here.





def index(request):
    room=houses.objects.all()
    filterby=request.GET.get("selection")
    house_filter=HouseFilter(request.GET,queryset=room)
    if filterby:
        if filterby=="1":
            room=room.order_by("Room_priceperday")
        elif filterby=="2":
            room=room.order_by("Room_size")
        elif filterby=="3":
            room=room.order_by("Room_location")
        elif filterby=="4":
            room=houses.objects.filter(Room_is_booked=False)
    return render(request,"index.html",{"room":room,
                                        "house_filter":house_filter.qs})


def details(request,roomid):
    room=get_object_or_404(houses,pk=roomid)
    return render(request,"details.html",{"room":room})

@login_required
def booking(request,roomid):
    room=get_object_or_404(houses,pk=roomid)
    current_user=request.user
    username=current_user.username
    if request.method=="GET":
        no_of_persons=request.GET.get("No_of_persons")
        no_of_days=int(request.GET.get("no_of_days"))
        queries=request.GET.get("queries")
        max=int(room.Room_maximumstay)
        min=int(room.Room_minimumstay)
        if no_of_days>min and no_of_days<max:
            room.Room_is_booked=True
            room.Customer_booked=username
            room.save()
            if room.Room_is_booked:
                return redirect("/")
            else:
                error="room not booked"
                return  render(request,"booking.html",{"error":error})
        else:
            error="maximum or minimum stay is invalid"
            return  render(request,"booking.html",{"error":error})
    else:
        return render(request,"booking.html",{"room":room})

@login_required
def rental(request):
    if request.method=="POST":
       form=HouseForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect("/")
    else:
        form=HouseForm()
        return render(request,"rental.html",{"form":form})
    
@login_required
def cartroom(request):
    current_user=request.user
    current_user=current_user.username
    booked_rooms=houses.objects.filter(Customer_booked=current_user)
    return render(request,"cartroom.html",{"booked_rooms":booked_rooms})

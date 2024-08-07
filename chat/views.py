from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Message

def index(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    rooms = Room.objects.all()
    return render(request, "chat/room.html", {"rooms": rooms})

def room(request, slug):
    room_instance = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room_instance)
    
    return render(request, 'chat/chatpage.html', {
        "room_name": room_instance.name,
        "slug": slug,
        'messages': messages
    })

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
          
            return redirect('room', slug=room.slug)
    else:
        form = RoomForm()
    
    return render(request, 'chat/chatpage.html', {'form': form})
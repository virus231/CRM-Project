from django.shortcuts import render
from django.core.paginator import Paginator
from users.models import CustomUser
from myapp.models import Contact

ef listing(request):
	user_list = CustomUser.objects.all()
	paginator = Paginator(user_list, 1)
	
	page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})
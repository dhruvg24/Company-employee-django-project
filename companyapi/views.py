from django.http import HttpResponse, JsonResponse

def home_page(request):
    print('home page requested')
    friends = [
        'ashish', 'abhay', 'akshay'
    ]
    # return HttpResponse('<h1>This is home page</h1>')
    return JsonResponse(friends, safe=False)  
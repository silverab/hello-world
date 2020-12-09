from django.http import HttpResponse

def HomePageView(request):
	return HttpResponse('Hey Hassan! how are you')
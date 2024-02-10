from django.shortcuts import render

def about(request: HttpRequest) -> HttpResponse:
    """Док"""
    
    return render(request, template_name: 'pages/about.html')

def rules(request: HttpRequest) -> HttpResponse:
    """Док"""
    
    return render(request, template_name: 'pages/rules.html')

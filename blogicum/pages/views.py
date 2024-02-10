from django.shortcuts import render



def about(request):
    """Страница с описанием сайта."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Страница с правилами сайта."""
    template = 'pages/rules.html'
    return render(request, template)

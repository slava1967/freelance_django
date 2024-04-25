from django.shortcuts import render


def index(request):
    context = {
        'title': 'Django Test project',
        'banner_headline_alt': 'Работайте в свое удовольствие',
        'banner_headline_span': 'Тысячи покупателей готовы платить за ваши навыки и таланты',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'main/about.html', context)

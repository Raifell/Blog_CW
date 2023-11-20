from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Main page'
    }
    return render(request, 'main/index_main.html', context=context)

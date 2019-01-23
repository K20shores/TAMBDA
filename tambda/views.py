from django.shortcuts import render

def home(request):
    return render(request, 'tambda/home.html', {})

def lessons(request):
    return render(request, 'tambda/lessons.html', {})

def performance_team(request):
    return render(request, 'tambda/performance_team.html', {})

def consent(request):
    return render(request, 'tambda/consent.html')

def privacy(request):
    return render(request, 'tambda/privacy.html')

def competition_home(request):
    return render(request, 'tambda/competition_home.html', {})

def competition_attire(request):
    return render(request, 'tambda/competition_attire.html', {})

def competition_packing_list(request):
    return render(request, 'tambda/competition_packing_list.html', {})

def competition_pictures(request):
    return render(request, 'tambda/competition_pictures.html', {})

def competition_results(request):
    return render(request, 'tambda/competition_results.html', {})

def competition_forms(request):
    return render(request, 'tambda/competition_forms.html', {})

def competition_syllabus(request):
    return render(request, 'tambda/competition_syllabus.html', {})

def competition_links(request):
    return render(request, 'tambda/competition_links.html', {})

def officers(request):
    return render(request, 'tambda/officers.html', {})

def contact_us(request):
    return render(request, 'tambda/contact_us.html', {})
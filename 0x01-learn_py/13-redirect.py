from django.http import HttpResponse, HttpResponseRedirect

"""
in urls file, the path is:

path('bounce', views.bounce)
"""

#command to the browser
def bounce(req):
    """redirect instruction and notice"""
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')
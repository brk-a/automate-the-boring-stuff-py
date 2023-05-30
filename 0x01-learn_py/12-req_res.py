from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape

#create views here


def funky(req):
    """funky function"""
    res = """
    <html><body><p>This is the views main.html sample</p>
    <p> This code is available at
    <a href="https://github.com/csev/dj4e-samples" target="_blank">
    https://github.com/csev/dj4e-samples</a>
    </p>
    </body></html>
    """
    return HttpResponse(res)


def danger(req):
    """danger fn: vulnerable to XSS"""
    res = f'<html><body>\
        <p>This is the views main.html sample</p>\
        <p> Your guess was {req.GET["guess"]}</p>\
        </body></html>'
    return HttpResponse(res)


def game(req):
    """game fn: made such that it is not vulnerable to XSS: type not enforced"""
    res = f'<html><body>\
        <p>This is the views main.html sample</p>\
        <p> Your guess was {escape(req.GET["guess"])}</p>\
        </body></html>'
    return HttpResponse(res)


def rest(req, guess):
    """rest fn: made such that it is not vulnerable to XSS: type enforced"""
    """
    within the urlpatterns in views, the path is
        path('rest/<int:guess>, views.rest)
    this explicitly types the parameter guess to type int, therefore,
    an error will be thrown if data passed to guess is not of type int
    """
    res = f'<html><body>\
        <p>This is the views main.html sample</p>\
        <p> Your guess was {escape(guess)}</p>\
        </body></html>'
    return HttpResponse(res)


#
from django.urls import path
from . import views
from django.views.generic import TemplateView

#https://docs.djancoproject.com/en/2.1/topics/http/urls
app_name = 'views'
urlpatterns = [
    #pre-difined class from django
    path('', TemplateView.as_view(template_name='views/main.html')),
    #function from views.py
    path('funky', views.funky),
    path('danger', views.danger),
    path('game', views.game),
    path('rest/<int:guess>', views.rest),
    path('bounce', views.bounce),
    #class from views.py
    path('main', views.MainView.as_view()),
    path('remain/<slug:guess>', views.RestMainView.as_view()),
]

'''
the views/template/views/main.html file looks like this:

<html><body><p>This is the views main.html sample</p>
<p>
<ul>
    <li>This is a page from a file in views/templates/main.html</li>
    <li><a href="funky">Use a view function</a></li>
        ...
</ul>
</p>
<p> This code is available at
<a href="https://github.com/csev/dj4e-samples" target="_blank">
https://github.com/csev/dj4e-samples</a>
</p>
</body></html>
'''
'''
MainView viz

from django.http import HttpResponse
from django.views import View


class MainView(View):
    """class MainView"""
    def get(self, req):
        res = """
        <html><body>
        <p>This is the ManView view sample</p>
        <p> This code is available at
        <a href="https://github.com/csev/dj4e-samples" target="_blank">
        https://github.com/csev/dj4e-samples</a>
        </p>
        </body></html>
        """
        return HttpResponse(res)
'''
'''
RestMainView viz

from django.http import HttpResponse
from django.utils.html import escape
from django.views import View


class RestMainView(View):
"""class RestMainView"""
    def get(self, req, guess):
    res = f'<html><body>\
        <p>This is RestMainView</p>\
        <p> Your guess was {escape(req.GET["guess"])}</p>\
        </body></html>'
    return HttpResponse(res)
'''
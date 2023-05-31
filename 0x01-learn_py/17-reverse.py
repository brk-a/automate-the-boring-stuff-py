from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View

class SecondView(View):
    """class SecondView"""
    def get(self, req):
        """method get in class SecondView"""
        u = reverse_lazy('gview:cats')
        u2 = reverse_lazy('gview:dogs')
        u3 = reverse('gview:dog', args=['42'])
        context = {
            'x1': u,
            'x2': u2,
            'x3': u3,
            }
        return render(req, 'route/second.htm', context)
    

'''
route/urls.py

path('second', views.SecondView.as_view(), name='second-view')
'''

'''
route/templates/route/main.html:

<li>
    <a href="{%url 'route:second-view'%}">
        url 'route:second-view'
    </a>
</li>
<li>
{{ x1 }} (x1 from context)
</li>
<li>
{{ x2 }} (x2 from context)
</li>
<li>
{{ x3 }} (x3 from context)
</li>
'''
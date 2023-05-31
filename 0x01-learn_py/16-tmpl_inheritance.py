from django.shortcuts import render
from django.views import View


class GameView(View):
    def get(self, req, guess):
        context = {'guess': int(guess)}
        return render(req, 'tmpl/cond2.html', context)
    
'''
tmpl/templates/tmpl/cond2.html:

{% extends "tmpl/base.html" %}
{% block content %}
    <p>Your guess was {{ guess }}</p>
    {% if guess < 42 %}
        <p>Too low</p>
    {% elif guess > 42 %}
        <p>Too high</p>
    {% else %}
        <p>Just right</p>
    {% endif %}   
{% endblock  %}
'''

'''
tmpl/templates/tmpl/base.html:

<html>
    <head>Base template</head>
    <body>
    {% block content%}{% endblock %}
    </body>
</html>
'''
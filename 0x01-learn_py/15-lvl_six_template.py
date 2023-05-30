from django.shortcuts import render
from django.views import View


class GameView(View):
    """class GameView"""
    def get(self, req, guess):
        """get fn: safe from XSS"""
        context = {'guess': int(guess)}
        return render(req, 'tmpl/cond.htm', context)
    
'''
tmpl/cond.htm viz:

<html>
<head>
    <title>A conditional template</title>
</head>
<body>
    <p>Your guess is {{ guess }}</p>
    {% if guess < 42 %}
        <p>Too low</p>
    {% if guess > 42 %}
        <p>Too high</p>
    {% else %}
        <p>Just right</p>
    {% endif %}
</body>
</html>
'''
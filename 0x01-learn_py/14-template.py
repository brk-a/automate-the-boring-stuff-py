from django.shortcuts import render
from django.views import View

"""
in urls file, the path is:

path('game/<slug:guess>', views.GameView.as_view())
"""

class GameView(View):
    """class GameView"""
    def get(self, req, guess):
        """get fn: safe from XSS"""
        x = {'guess': int(guess)}
        return render(req, 'tmpl/cond.htm', x)
    

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
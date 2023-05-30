from django.shortcuts import render

def loop(req):
    """level 4 template"""
    f = ['mango', 'banana', 'passion']
    n = ['macadamia', 'cashew']
    context = {
        'fruits': f,
        'nuts': n,
        'zap': '42',
        }
    return render(req, 'tmpl/loop.html', context)

'''
tmpl/loop.html

<html>
<head>
    <title>level four template</title>
</head>
<body>
    <p>your guess is {{ zap }}</p>
    <ul>
        {% for x in fruits %}
            <li>{{ x }}</li>
        {% endfor %}
    </ul>
    {% if nuts %}
        <p>Number of nuts: {{ nuts|length }}</p>
    {% else %}
        <p>No nuts.</p>
    {% endif %}
</body>
</html>
'''
from django.shortcuts import render

def special(req):
    """level 3 template"""
    context = {
        'txt': '<b>bold</b>',
        'zap': '42',
        }
    return render(req, 'tmpl/special.html', context)

'''
tmpl/special.html

<html>
<head>
    <title>level three template</title>
</head>
<body>
    <p>to escape or not to escape?</p>
    <p>your guess is {{ zap }}</p>
    <p>Escaped: {{ txt }}</p>
    <p> Not escaped (`safe` used): {{ txt|safe}}</p>
</body>
</html>
'''
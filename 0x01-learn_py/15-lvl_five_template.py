from django.shortcuts import render

def nested(req):
    """level 5 template"""
    context = {
        'outer': {
            'inner': '42',
        },
        }
    return render(req, 'tmpl/nested.html', context)

'''
tmpl/nested.html

<html>
<head>
    <title>level five template</title>
</head>
<body>
    <p>your guess is {{ outer.inner }}</p>
</body>
</html>
'''
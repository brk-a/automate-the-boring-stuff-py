from django.shortcuts import render

def guess(req):
    """level 2 template"""
    context = {'zap': '42'}
    return render(req, 'tmpl/guess.html', context)

'''
tmpl/guess.html

<html>
<head>
    <title>level two template</title>
</head>
<body>
    <p>your guess is {{ zap }}</p>
</body>
</html>
'''
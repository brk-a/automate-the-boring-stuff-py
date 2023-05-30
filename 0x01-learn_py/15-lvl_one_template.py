from django.shortcuts import render

def simple(req):
    """level 1 template"""
    return render(req, 'tmpl/simple.html')

'''
tmpl/simple.html

<html>
<head>
    <title>level one template</title>
</head>
<body>
    <h1>this is quite easy</h1>
</body>
</html>
'''
# 

### Request-response cycle
* each time a user clicks on an anchor tag with a  _href=_ value to switch to a new page, the browser makes a connection to the web server and issues a _GET_ request to, well, _get_ the content of the page at the specified url
* the server returns the HTML doc to the browser; browser renders (formats and displays) the doc to the user
* example: click a link
    * browser is connected to internet
    * there is an event listener; it _listens_ for the click
    * you click the link
    * data is generated
    * said data is intercepted by browser
    * browser opens a network socket to a web server
    * browser sends a request
    * web server processes request
    * web server _serves_ a response (on the same connection)
    * browser parses response
    * browser renders data in response to you
* making a http request
    * connect to server
    * _"handshake"_
    * request a doc
### Network sockets
* the "phone calls" for pairs of apps
* are endpoints of a bidirectional inter-process communication flow accross an IP-based computer network such as the internet
* each computer has an IP address and several thousand ports
    * IPv4-style addresses: `xxx.xxx.xxx.xxx` whare `xxx` is between 0x00 (zero) and 0xFFF (255), inclusive
    * IPv6-style addresses: `xxxx:xxxx:xxxx:xxxx:oooo:oooo:oooo:oooo` where:
        * `xxxx` is a hex number between 0000 and FFFF, inclusive. this is the network component
        * `oooo` is an optional hex number between 0000 and FFFF, inclusive. this is the node component
    * a port is an application-specific or process-specific software communications endpoint
        * think of a port like a phone extension
        * example: http uses port 80, secure http (https) uses port 443
* history of HTTP
    * invented in 1990; runs atop sockets
    * there were many protocols (some still used are: _mailto:_ and _ftp:_)
    * before http, one had to use specific protocols on specific ports to talk to specific servers; bureaucratic, to say the least
    * rode on the tailwinds of the web browser (one piece of software that is multi-protocol) and URL
    * invented fot the web to retrieve html, images, docs etc
    * has been extended to handle data in addition to docs (rss, web services etc)
    * basic concept: make a connection, request a doc, retrieve said doc, close the connection
    * is the dominant app-layer protocol on the internet
    * the internet and sockets pre-date http by _c._ 20 years
* history of the URL
    * at an atomic level, it has three parts: protocol, host and document
    * example: `http://example.com/page1.html`
        * `http://` --> protocol
        * `example.com` --> host; a domain name that resolves to an IP address
        * `/page1.html` --> document
    * 
* history of internet standards
    * all internet protocols (inner working of the internet), called [RFCs](def2), are developed by the [IETF](def)
    * example: RFC 2616 is HTTP
    * publicly available for free
* 
### Virtual Hosting
* many domains, one system
### Models feature on Django
* implements an ORM (object relational mapper)
* allows dev to write `py` code; no explitic SQL. said code is converted to SQL by the feature
* creates [db portability](def5); any SQL db can be used
* migrations sub-feature [creates and evolves db schema](def4)
* has an admin interface; admin work is easier
* generates forms automatically
### Migrations
* `makemigrations` command reads all the `models.py` files in all the applications then creates/evolves the miration files; the db is not created here, rather, the instructions to build the db are created here
    * is guided by the apps listed in `settings.py`
    * migrations are portable across databases
* `migrate` command reads all the `migrations` folders in the application folders then creates/evolves the tables in the db e.g. _db.sqlite3_
### Flow of a web request in django
* Model-View-Controller style
* in other words the flow of a web request viz
    * request arrives at an app
    * incoming request url is compared to the list of paths in `urlpatterns` inside `urls.py`
    * a `View` is selected when there is a url match; _View_ handles any db access, produces a response and delivers said response to browser
        * _View_ accesses the db indirectly through an abstraction called a _model_
    * browser parses and renders
### MVC in django
* Model-View-Controller
* _Model_ --> the data of the app and the business rules used to manipulate the data (the persistent data kept in a store, say, a db)
* _View_ --> element of the user interface e.g. text, checkbox items etc (HTML, CSS etc; the _look and feel of an app_)
* _Controller_ --> manages how the Model and View communicate (the JS, Py etc; that is, the logic/_code that does the thinking and decison-making_)
    * Controller _orchestrates_; it is the conductor of all other aspects of MVC (brains of the operation, if you like)
* recall [request-response cycle](def6): user clicks on link, browser intercepts, browser sends a _GET_ request to web server, web server _web serves_, browser receives a response from web server, browser parses said response, browser renders data in response to user; the _web server web-serves_ part is covered by MVC
* tasks inside the web server
    * handle input --> process any user input data; possibly store it in a db or perform an action on said data eg delete a record 
    * store data --> decide which screen to send back to the user
    * retrieve any data needed
    * build HTML --> produce HTML response(s) and send that to browser (a template)
* in a django app
    * the _models_ functionality (`_models.py_` and the db) is the model
    * the _views_ fuctionality (`_views.py_`, `_forms.py_`, `_templates_`) is the view
    * the _routing_ functionality (containing `_urls.py_`) is the controller
### Projects, Applications ...
* see [11-views.py](def7)
* a project, in django, is just that; a project. the project dir is the root dir for the entire project
* an app is a specific feature within the project. example: a coffee shop project may have apps viz: check-out, eWallet, orders section etc
* URL dispatcher allows a clean, elegant URL scheme that has no framework limitations. to design URLs for an app, create a py module (a URLconf). this module is pure py code and is a mapping between URL path expressions to python fuctions (the views). this  mapping can be as long or short as needed; it can reference other mappings and be constructed dynamically because it is pure python code
### Request and response objects
* django uses  request and response objects to pass data throughout the django app
* say a page is requested by a browser. django creates a `HttpRequest` object as the first agrument to the view function. each view is responsible for returning a `HttpRequest` object
* the API for `HttpRequest` and `HttpResponse` objects are defined in the `django.http` module
### Danger
* see the `danger` and `game` functions in [12-req_res.py](def8)
* it is dangerous to take data from the user and include it in the HTTP response w/o _escaping_ the output
* you do not want to be _sending code_ (HTML and/or JS) to other users' browsers; in other words, you do not want anyone programming any user's browser
* XSS (cross-site scripting) enables an attacker to inject client-side scripts into web pages viewed by a user
* the `escape` function in `django.utils.html` makes it so that the scripts, if injected, are not interpreted and/or executed; in other words, they are _escaped_ (adding special characters, such as backslashes or quotes, that prevent the browser from treating data as code)
### Templates
* a template is, simply, a text file. it generates any text-based format (html, xml, csv and so on)
    * it contains _variables_; these are replaced by values when the template is evaluated
    * also contains _tags_; these control the logic of the template 
* django, being a web framework, requires a convenient way to generate HTML dynamically. the most common approach relies on _templates_. a template contains the static parts of the desired HTML output and special syntax that describes how dynamic content will be inserted
* a django project can be configured with zero or more template engines; zero means you do not use any templates
* django has built-in back-ends for its own template system, the django template language (DTL), and for `Jinja2`, a popular alternative
* template render process viz: data from response plus template into a render engine produces output to be rendered by the browser
* templates are _global_; they are accessible cross-application within a project (recall: a project, in django, has one or more apps). see [Projects, Applications section](def9)
    * it is common to reuse the _name_ of a template in more than one application; a technique called _namespace_ is used to allow an app to use its own templates
    * convention is `app_name/templates/app_name/template_name.html`; almost always, `template_name` is _detail_
    * each template is, now, referred to using `app_name/template_name.html`
    * _namespace_ works, in this case, because this way of reffering to a template makes the path to said template unique to that app
* template inheritance works viz: data from response plus base template plus template unique to the view and/or app into a render engine produces output to be rendered by the browser
### URL mapping
* a set of functions that make it easy and convenient to read `urls.py`
* in a project, there is a need  to obtain URLs in their final forms either for embedding in generated content or for navigation (eg redirection)
* strongly desirable to avoid hard-coding said URLs; dangerous move is to devise _ad hoc_ mechanisms to generate URLs because they may be parallel to the design described by `URLConf`. such URLs become stale over time
* quite clearly, a DRY mechanism is required; URL design will evolve w/o having to go over all the source code of the project to search & replace outdated URLs
* to get a URL, we have an identification (eg. the name) of the view in charge of handling it. other pieces of info necessary are the types (positional, keyword) and values of the view arguments

~~~python
app_name = 'route'
urlpatterns = [
    path('',TemplateView.as_view(template_name='route/main.html')),
    path('first',views.FirstView.as_view(), name='route/first-view'),
    path('second',views.SecondView.as_view(), name='route/second-view'),
]
~~~

~~~html
<!-- route/templates/route/main.html-->
<!-- snip -->
<li>
    <a href="/route/second">hard-coded to second-view (not DRY)</a>
</li>
<li>
    {%url 'route:first-view'%} -> url to first-view
</li>
<li>
    <a href="{%url 'route:second-vew'%}">
        url to second-view (DRY)
    </a>
</li>
<!-- snip -->
~~~

* here is how to get a view from a different app w/i the same project

~~~python
app_name = 'gview'
urlpatterns = [
    path('cats',views.CatListView.as_view(), name='cats'),
    path('cat/<int:pk_from_url>',views.CatDetailView.as_view(), name='cat'),
]
~~~

~~~html
<!-- route/templates/route/main.html-->
<!-- snip -->
<li>
    {%url 'gview:cats'%}
    (url 'gview:cats') from gview/urls.py
</li>
<li>
    {% url 'gview:cat' 42 %}
    (url 'gview:cat' 42) from gview/urls.py
</li>
<!-- snip -->
~~~

* you can rename and/or add a second _namespace_ to a view; think about it as a _"second"_ namespace

~~~python
app_name = 'gview'
urlpatterns = [
    path('', include('home.urls'))
    path('admin/', admin.site.urls), #keep
    path(r'^oauth/', include('social_django.urls') namespace='social'),
    path('hello/', include('hello.urls')),
    path('route/', include('route.urls'), namespace='nsroute'),
]
~~~

~~~html
<!-- route/templates/route/main.html-->
<!-- snip -->
<li>
    <a href="{%url 'route:second-view'%}">
        url 'route:second-view'
    </a>
</li>
<li>
    {% url 'nsroute:second-view' %}
    (url 'nsroute:second-view')
</li>
<!-- snip -->
~~~

* 

[def]: www.ietf.com
[def2]: https://www.ietf.org/standards/rfcs/
[def3]: https://www.freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples/
[def4]: https://en.wikipedia.org/wiki/Schema_evolution
[def5]: https://www.techopedia.com/definition/6752/data-portability
[def6]: #request-response-cycle
[def7]: ./11-views.py
[def8]: ./12-req_res.py
[def9]: #projects-applications
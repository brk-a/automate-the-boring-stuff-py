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
    * all internet protocols (inner working of the internet), called [RFCs][def2], are developed by the [IETF][def]
    * example: RFC 2616 is HTTP
    * publicly available for free
* 
### MVC in django
* Model-View-Controller; a pattern used to perform request-response cycles
* in other words the flow of a web request
    * request arrives at an app
    * incoming request url is compared to the list of paths in `urlpatterns` inside `urls.py`
    * a `View` is selected when there is a url match; _View_ handles any db access, produces a response and delivers said response to browser
        * _View_ accesses the db indirectly through an abstraction called a _model_
    * browser parses and renders
### Virtual Hosting
* many domains, one system
### Models feature on Django
* implements an ORM (object relational mapper)
* allows dev to write `py` code; no explitic SQL. said code is converted to SQL by the feature
* creates [db portability][def5]; any SQL db can be used
* migrations sub-feature [creates and evolves db schema][def4]
* has an admin interface; admin work is easier
* generates forms automatically
### Migrations
* `makemigrations` command reads all the `models.py` files in all the applications then creates/evolves the miration files; the db is not created here, rather, the instructions to build the db are created here
    * is guided by the apps listed in `settings.py`
    * migrations are portable across databases
* `migrate` command reads all the `migrations` folders in the application folders then creates/evolves the tables in the db e.g. _db.sqlite3_
### MVC
* Model-View-Controller
* _Model_ --> the data of the app and the business rules used to manipulate the data (the persistent data kept in a store, say, a db)
* _View_ --> element of the user interface e.g. text, checkbox items etc (HTML, CSS etc; the _look and feel of an app_)
* _Controller_ --> manages how the Model and View communicate (the JS, Py etc; that is, the logic/_code that does the thinking and decison-making_)
    * Controller _orchestrates_; it is the conductor of all other aspects of MVC (brains of the operation, if you like)
* recall [request-response cycle][def6]: user clicks on link, browser intercepts, browser sends a _GET_ request to web server, web server _web serves_, browser receives a response from web server, browser parses said response, browser renders data in response to user; the _web server web-serves_ part is covered by MVC
* tasks inside the web server
    * handle input --> process any user input data; possibly store it in a db or perform an action on said data eg delete a record 
    * store data --> decide which screen to send back to the user
    * retrieve any data needed
    * build HTML --> produce HTML response(s) and send that to browser (a template)
* in a django app
    * the _models_ functionality (`_models.py_` and the db) is the model
    * the _views_ fuctionality (`_views.py_`, `_forms.py_`, `_templates_`) is the view
    * the _routing_ functionality (containing `_urls.py_`) is the controller
[def]: www.ietf.com
[def2]: https://www.ietf.org/standards/rfcs/
[def3]: https://www.freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples/
[def4]: https://en.wikipedia.org/wiki/Schema_evolution
[def5]: https://www.techopedia.com/definition/6752/data-portability
[def6]: #request-response-cycle
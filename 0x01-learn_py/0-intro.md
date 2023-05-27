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

[def]: www.ietf.com
[def2]: https://www.ietf.org/standards/rfcs/
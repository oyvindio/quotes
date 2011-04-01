Quotes
======
Web interface for the Quote module in murr4y/grouphugs.

Setup
-----
    cd quotes
    mkvirtualenv --no-site-packages quotes # or whatever you want to call it
    pip install -r requirements.txt

Apache/mod_wsgi setup
---------------------

    WSGIDaemonProcess some-unique-id user=unixuser group=unixgroup threads=10 python-path=/absolute/path/to/virtualenv/lib/python2.7/site-packages
    WSGIProcessGroup some-unique-id
    WSGIScriptAlias /url/to/quotes/ /absolute/path/to/project/quotes/dispatch.wsgi/
    
    AddType text/html .wsgi
    
    RewriteEngine On
    RewriteRule ^/url/to/quotes$ /url/to/ [R]
    
    Alias /url/to/quotes/static /absolute/path/o/project/quotes/static/
    <Directory /absolute/path/to/quotes/static>
        Order deny,allow
        Allow from all
    </Directory>
                                                
Did you remember to fix the Python version (`python2.7`) in the
python-path argument to WSGIDaemonProcess, so it matches the Python
version your virtualenv is using? Do it now.

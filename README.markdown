Quotes
======
Web interface for the Quote module in murr4y/grouphugs.

Setup
-----
On your pc
    
    cd quotes
    mkvirtualenv --no-site-packages quotes # or whatever you want to call it
    pip install -r requirements.txt
    cp settings.py{.template,}
    $EDITOR settings.py

Deployment
----------
On your pc

    fab deploy
    
This will make a tarball from git HEAD, scp it to the server you set
up in `settings.py`, extract it into its own directory, symlink your
database into this directory, scp `settings.py` to your server, and
restart apache. Read `fabfile.py` for details.

Apache/mod_wsgi setup
---------------------
Use this as a guideline to set up Apache+mod_wsgi to load quotes on
your server (it goes in your apache config file somewhere).
    WSGIDaemonProcess some-unique-id user=unixuser group=unixgroup threads=10 python-path=/absolute/path/to/virtualenv/lib/python2.7/site-packages
    WSGIProcessGroup some-unique-id
    WSGIScriptAlias /url/to/quotes/ /absolute/path/to/project/quotes/releases/current/dispatch.wsgi/
    
    AddType text/html .wsgi
    
    RewriteEngine On
    RewriteRule ^/url/to/quotes$ /url/to/ [R]
    
    Alias /url/to/quotes/static /absolute/path/o/project/quotes/releases/current/static/
    <Directory /absolute/path/to/quotes/releases/current/static>
        Order deny,allow
        Allow from all
    </Directory>
                                                
Did you remember to fix the Python version (`python2.7`) in the
python-path argument to WSGIDaemonProcess, so it matches the Python
version your virtualenv is using? Do it now.

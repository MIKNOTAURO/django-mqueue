Configuration
=============

Mqueue can deliver the messages in real time to the users. This is made using the `Centrifugo <https://github.com/centrifugal/centrifugo/>`_  websockets server.
 
**Warning**: this feature is experimental and is not yet in the pip version (use master). The api may change.

1. Install Centrifugo: example for Debian: 

.. highlight:: bash

::

   sudo apt-get install golang
   mkdir go && cd go
   wget https://github.com/centrifugal/centrifugo/releases/download/v1.5.1/centrifugo-1.5.1-linux-386.zip
   unzip centrifugo-1.5.1-linux-386.zip
   cd centrifugo-1.5.1-linux-386


2. Configure Centrifugo

::

   ./centrifugo genconfig
   
This will generate your secret key. Set anonymous to true if you want all users to receive the messages. 
Leave it if you want only the logged in users to see the messages.

.. highlight:: json

::

   {
  "secret": "70b651f6-775a-4949-982b-b387b31c1d84",
  "anonymous": true
  }

3. Install the python requirements

::

   pip install cent
   cd my_django_project_root
   git clone https://github.com/synw/django-instant.git
   mv django-instant/instant . && rm -rf django_instant
   
Set the urls:

.. highlight:: python

::

   url('^mq/', include('instant.urls')),
   
4. Install the js part with npm:

.. highlight:: python

::

   cd static/instant
   npm install centrifuge

Settings
~~~~~~~~

Add ``'instant',`` to installed apps and configure settings.py:

::

   # required settings
   SITE_SLUG = "my_site" # used internaly to prefix the channels
   MQUEUE_LIVE_STREAM = True # tell mqueue we want to use the stream future
   CENTRIFUGO_SECRET_KEY = "the_key_that_is_in_config.json"
   # optionnal settings
   CENTRIFUGO_HOST = 'http://ip_here' #default: localhost
   CENTRIFUGO_PORT = 8012 # default: 8001



Important: if you use the log handler these settings must be placed before ``from mqueue.conf import LOGGING``

Templates
~~~~~~~~~

Include the template ``{% include "instant/stream.html" %}`` anywhere (nothing will be displayed it is the engine), 
in the footer for example. Add ``{% include "instant/messages.html" %}`` where you want the message counter to be.

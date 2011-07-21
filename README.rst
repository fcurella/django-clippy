Django-Clippy
======================================

Provides a template tag for a 'copy to clipboard' button, based on GitHub's Clippy.

Instructions
------------

1. Add ``clippy`` to ``INSTALLED_APPS``

2. In your template::

    {% load clippy %}
    <div id="mycode"><a href=""><img src="" alt="" /></a></div>
    {% clippy "<element_id>" "<size>" "<bgcolor>" "<wmode>" %}

The ``element_id`` parameter is mandatory. All other parameters are optional. Defaults are ``size='14x210'``, ``bgcolor='#FFFFFF'``, ``wmode='opaque'``

Clippy's template can be overridden creating your own template file at `clippy/clippy.html` in your templates directory.

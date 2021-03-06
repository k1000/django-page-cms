============
Installation
============

This document explain how to install django page CMS into an existing Django project.
This document assume that you already know how to setup a Django project.

If you have any problem installing this CMS, take a look at the example application that stands in the example directory.
This application works out of the box and will certainly help you to get started.

.. contents::
    :local:
    :depth: 1

Evaluate quickly the application
=================================

After you have installed all the dependencies you can simply checkout the code with git::

    git clone git://github.com/batiste/django-page-cms.git django-page-cms

And then, run the example project::

    cd django-page-cms/example/
    python manage.py syncdb
    python manage.py build_media pages
    python manage.py runserver

Then visit http://127.0.0.1:8000/admin/ and create a few pages.


Install dependencies by using pip
==================================

The pip install is the easiest and the recommended installation method. Use::

    $ sudo easy_install pip
    $ wget -c http://github.com/batiste/django-page-cms/blob/master/requirements/external_apps.txt
    $ sudo pip install -r external_apps.txt

Every package listed in the ``external_app.txt`` should be downloaded and installed.

If you are not using the source code version of the application then install it using::

    $ sudo pip install django-page-cms

Install dependencies by using easy_install
==========================================

On debian linux you can do::

    $ sudo easy_install django
    $ sudo easy_install html5lib
    $ sudo easy_install django-staticfiles

If you are not using the source code version of the application then install it using::

    $ sudo easy_install django-page-cms

.. note::

    Django-Tagging and Django-mptt maybe required to be installed by hand or with subversion
    because the available packages are not compatible with django 1.0.

Install by using subversion externals
======================================

You can also use the trunk version of the Django Page CMS by using subversion externals::


    $ svn pe svn:externals .
    pages                   http://django-page-cms.googlecode.com/svn/trunk/pages
    mptt                    http://django-mptt.googlecode.com/svn/trunk/mptt
    tagging                 http://django-tagging.googlecode.com/svn/trunk/tagging

Urls
====

Take a look in the ``example/urls.py`` and copy desired URLs in your own ``urls.py``.
Basically you need to have something like this::

    urlpatterns = patterns('',
        ...
        url(r'^pages/', include('pages.urls')),
        (r'^admin/', include(admin.site.urls)),
    )

When you will visit the site the first time (``/pages/``), you will get a 404 error
because there is no published page. Go to the admin first and create and publish some pages.

You will certainly want to activate the static file serve view in your ``urls.py`` if you are in developement mode::

    if settings.DEBUG:
        urlpatterns += patterns('',
            # Trick for Django to support static files (security hole: only for Dev environement! remove this on Prod!!!)
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
            url(r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
        )

Settings
========

All the Django page CMS specific settings and options are listed and explained in the ``pages/settings.py`` file.

Django page CMS require several of these settings to be set. They are marked in this document with a bold "*must*".

.. note::

    If you want a complete list of the available settings for this CMS visit
    :doc:`the list of all available settings </settings-list>`.


Tagging
-------

Tagging is optional and disabled by default. 

If you want to use it set ``PAGE_TAGGING`` at ``True`` into your setting file and add it to your installed apps::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'mptt',
        'tagging',
        'pages',
        ...
    )

Caching
-------

Django page CMS use the caching framework quite intensively. You should definitely
setting-up a cache-backend_ to have decent performance.

.. _cache-backend: http://docs.djangoproject.com/en/dev/topics/cache/#setting-up-the-cache

You can easily setup a local memory cache this way::

    CACHE_BACKEND = "locmem:///?max_entries=5000"

Languages
---------

Please first read how django handle languages

* http://docs.djangoproject.com/en/dev/ref/settings/#languages
* http://docs.djangoproject.com/en/dev/ref/settings/#language-code

This CMS use the ``PAGE_LANGUAGES`` setting in order to present which language are supported by the CMS.
By default ``PAGE_LANGUAGES`` value is set to ``settings.LANGUAGES`` value.
So you can directly set the ``LANGUAGES`` setting if you want.
In any case *you should set* ``PAGE_LANGUAGES`` or ``LANGUAGES``
yourself because by default the ``LANGUAGES`` list is big.

Django use ``LANGUAGES`` setting to set the ``request.LANGUAGE_CODE`` value that is used by this CMS.
So if the language you want to support is not present in the ``LANGUAGES``
setting the ``request.LANGUAGE_CODE`` will not be set correctly.

A possible solution is to redefine ``settings.LANGUAGES``. For example you can do::

    # Default language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    # This is defined here as a do-nothing function because we can't import
    # django.utils.translation -- that module depends on the settings.
    gettext_noop = lambda s: s

    # here is all the languages supported by the CMS
    PAGE_LANGUAGES = (
        ('de', gettext_noop('German')),
        ('fr-ch', gettext_noop('Swiss french')),
        ('en-us', gettext_noop('US English')),
    )

    # copy PAGE_LANGUAGES
    languages = list(PAGE_LANGUAGES)
    
    # All language accepted as a valid client language
    languages.append(('fr-fr', gettext_noop('French')))
    languages.append(('fr-be', gettext_noop('Belgium french')))
    # redefine the LANGUAGES setting in order to set request.LANGUAGE_CODE correctly
    LANGUAGES = languages

Template context processors and Middlewares
-------------------------------------------

You *must* have these context processors into your ``TEMPLATE_CONTEXT_PROCESSORS`` setting::

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.auth',
        'django.core.context_processors.i18n',
        'django.core.context_processors.debug',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
        'pages.context_processors.media',
        ...
    )

You *must* have these middleware into your ``MIDDLEWARE_CLASSES`` setting::

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.doc.XViewMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        ...
    )

Default template
----------------

You *must* set ``DEFAULT_PAGE_TEMPLATE`` to the name of your default CMS template::

    DEFAULT_PAGE_TEMPLATE = 'pages/index.html'

And you *must* copy the directory ``example/templates/pages`` into your root template directory.

Additional templates
--------------------

Optionally you can set ``PAGE_TEMPLATES`` if you want additional templates choices.
In the the example application you have actually this::

    PAGE_TEMPLATES = (
        ('pages/nice.html', 'nice one'),
        ('pages/cool.html', 'cool one'),
    )

One can also assign a callable (which should return the tuple) to this
setting to achieve dynamic template list e.g.::

    def _get_templates():
        # to avoid any import issues
        from app.models import PageTemplate
        return PageTemplate.get_page_templates()

    PAGE_TEMPLATES = _get_templates

Where the model might look like this::

    class PageTemplate(OrderedModel):
        name = models.CharField(unique=True, max_length=100)
        template = models.CharField(unique=True, max_length=260)

        @staticmethod
        def get_page_templates():
            return PageTemplate.objects.values_list('template', 'name')

        class Meta:
            ordering = ["order"]

        def __unicode__(self):
            return self.name

The sites framework
-------------------

If you want to use the `Django sites framework <http://docs.djangoproject.com/en/dev/ref/contrib/sites/#ref-contrib-sites>`_
with django-page-cms, you *must* define the ``SITE_ID`` and ``PAGE_USE_SITE_ID`` settings and create the appropriate Site object into the admin interface::

    PAGE_USE_SITE_ID = True
    SITE_ID = 1

The Site object should have the domain that match your actual domain (ie: 127.0.0.1:8000)

Media directory
---------------

The django CMS come with some javascript and CSS files.
These files are standing in the ``pages/media/pages`` directory.

To make these files accessible to your project you can simply copy them  or make a symbolic link into
your media directory. That's necessary to have a fully functioning administration interface.

You can also look at how the example project is working to make a local setup. It use the very good
`django-staticfiles <http://pypi.python.org/pypi/django-staticfiles/>`_ application that can gather the media
files for you. After installation in your project just run::

    $ python manage.py build_media

And the cms media files will be copied in your project's media directory.



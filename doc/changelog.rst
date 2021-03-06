============
 Changelog
============

This file describe new features and incompatibilites between released version of the CMS.

Release 1.1.2
=============

    * Change the default value of PAGE_TAGGING and PAGE_TINYMCE to `False`
    * Implement drag and drop within the admin interface.
    * Implement haystack SearchIndex for page content search.
    * Add the untranslated placeholder keyword. Enable the user to have a single
      placeholder content accross all languages.
    * Add back the hierarchical change rights management for every page.

Release 1.1.1
=============

    * Add new inherited placeholder option to inherit content from a parent page.
    * PagePermission object is gone in favor of django-authority.
    * New permission by language.
    * New permission for freezing page content.
    * Add a get_date_ordered_children_for_frontend Page's method.
    * Add missing templates to the package.

Release 1.1.0
=============

    * PAGE_TEMPLATES setting can also be a callable.
    * PAGE_UPLOAD_ROOT setting enable you to choose where files are uploaded.
    * The CMS comes with south migrations if you want to use them.
    * `get_url` is renamed into `get_complete_slug`.
    * `get_absolute_url` is renamed into `get_url_path`.
    * Admin widgets now needs to use a registery to be used within the admin.
      The placeholder template tag doesn't load load external modules for you anymore.
    * RTL support for pages in admin.
    * The context variable `pages` has been renamed to `pages_naviagtion` to avoid
      any name conflict with some pagination tags.

Maintenance
-----------

A new character field called `delegate_to` is added to the page model.
to enable the delegation of the pages rendering to a 3rd party application::

    ALTER TABLE pages_page ADD COLUMN delegate_to varchar(100) NULL;

Release 1.0.9
=============

    * Finish to migrate the old wiki into the sphinx documentation
    * Fix the package so it can be installed properly with easy_install
    * Add a new placeholder {% imageplaceholder %} for a basic automatic image
      handling in the admin.

Release 1.0.8
=============

    * A few bug fix.
    * A automatic internal link system. Page link don't break even if you move the
      linked page.

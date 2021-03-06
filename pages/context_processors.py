"""Context processors for Page CMS."""
from pages import settings

def media(request):
    """Adds media-related variables to the `context`."""
    return {
        'PAGES_MEDIA_URL': settings.PAGES_MEDIA_URL,
        'PAGE_USE_SITE_ID': settings.PAGE_USE_SITE_ID
    }

def pages_navigation(request):
    """Adds essential pages variables to the `context`."""
    pages = Page.objects.navigation().order_by("tree_id")
    return {
        'pages_navigation': pages,
        'current_page':None
    }

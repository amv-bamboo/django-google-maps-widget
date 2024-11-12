from django import forms
from django.conf import settings
from django.forms import widgets
from django.utils.html import format_html


class GoogleMapsAddressWidget(widgets.TextInput):
    """a widget that will place a google map right after the #id_address field"""

    template_name = "django_google_maps_widget/widgets/map_widget.html"

    class Media:
        css = {"all": ("django_google_maps_widget/css/google-maps-admin.css",)}
        js = (
            (
                f"https://maps.googleapis.com/maps/api/js"
                f"?key={settings.GOOGLE_MAPS_API_KEY}&libraries=maps,marker,places,geocoding"
            ),
            "django_google_maps_widget/js/google-maps-admin.js",
        )


def render_js(cls):
    return [format_html('<script src="{}" defer></script>', cls.absolute_path(path)) for path in cls._js]


forms.widgets.Media.render_js = render_js
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_bootstrap4.helpers import concat_classes, get_plugin_template

from .models import OwlCarousel, OwlCarouselSlide
from .constants import CAROUSEL_DEFAULT_SIZE, CAROUSEL_TEMPLATE_CHOICES


class OwlCarouselPlugin(CMSPluginBase):
    """
    Components > "Carousel" Plugin
    https://getbootstrap.com/docs/4.0/components/owlcarousel/
    """
    model = OwlCarousel
    name = _('OwlCarousel')
    module = _('Bootstrap 4')
    allow_children = True
    child_classes = ['OwlCarouselSlidePlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('carousel_aspect_ratio', 'carousel_interval'),
                ('carousel_controls', 'carousel_indicators'),
                ('carousel_keyboard', 'carousel_wrap'),
                ('carousel_ride', 'carousel_pause'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'carousel_style',
                'tag_type',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'owlcarousel', 'owlcarousel', CAROUSEL_TEMPLATE_CHOICES
        )

    def render(self, context, instance, placeholder):
        link_classes = ['hero-slides', 'owl-carousel']

        classes = concat_classes(link_classes + [
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(OwlCarouselPlugin, self).render(
            context, instance, placeholder
        )


class OwlCarouselSlidePlugin(CMSPluginBase):
    """
    Components > "Carousel Slide" Plugin
    https://getbootstrap.com/docs/4.0/components/owlcarousel/
    """
    model = OwlCarouselSlide
    name = _('OwlCarousel slide')
    module = _('Bootstrap 4')
    allow_children = True
    parent_classes = ['OwlCarouselPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'carousel_image',
                'carousel_content',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('external_link', 'internal_link'),
                ('mailto', 'phone'),
                ('anchor', 'target'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        parent = instance.parent.get_plugin_instance()[0]
        width = float(context.get('width') or CAROUSEL_DEFAULT_SIZE[0])
        height = float(context.get('height') or CAROUSEL_DEFAULT_SIZE[1])

        if parent.carousel_aspect_ratio:
            aspect_width, aspect_height = tuple(
                [int(i) for i in parent.carousel_aspect_ratio.split('x')]
            )
            height = width * aspect_height / aspect_width

        context['instance'] = instance
        context['link'] = instance.get_link()
        context['options'] = {
            'crop': 10,
            'size': (width, height),
            'upscale': True
        }
        return context

    def get_render_template(self, context, instance, placeholder):
        return get_plugin_template(
            instance, 'owlcarousel', 'slide', CAROUSEL_TEMPLATE_CHOICES
        )


plugin_pool.register_plugin(OwlCarouselPlugin)
plugin_pool.register_plugin(OwlCarouselSlidePlugin)

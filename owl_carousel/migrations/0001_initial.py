# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-15 08:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import djangocms_bootstrap4.fields
import djangocms_link.validators
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwlCarousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='owl_carousel_owlcarousel', serialize=False, to='cms.CMSPlugin')),
                ('carousel_style', models.CharField(choices=[('default', 'Default')], default='default', help_text='This is the template that will be used for the component.', max_length=255, verbose_name='Template')),
                ('carousel_interval', models.IntegerField(default=5000, help_text='The amount of time to delay between automatically cycling an item. If false, owlcarousel will not automatically cycle.', verbose_name='Interval')),
                ('carousel_controls', models.BooleanField(default=True, help_text='Adding in the previous and next controls.', verbose_name='Controls')),
                ('carousel_indicators', models.BooleanField(default=True, help_text='Adding in the indicators to the owlcarousel.', verbose_name='Indicators')),
                ('carousel_keyboard', models.BooleanField(default=True, help_text='Whether the owlcarousel should react to keyboard events.', verbose_name='Keyboard')),
                ('carousel_pause', models.CharField(choices=[('hover', 'hover'), ('mouseenter', 'mouseenter'), ('mouseleave', 'mouseleave'), ('false', 'off')], default='hover', help_text='If set to "hover", pauses the cycling of the owlcarousel on "mouseenter" and resumes the cycling of the owlcarousel on "mouseleave". If set to "false", hovering over the owlcarousel won\'t pause it.', max_length=255, verbose_name='Pause')),
                ('carousel_ride', models.CharField(choices=[('owlcarousel', 'owlcarousel'), ('false', 'off')], default='owlcarousel', help_text='Autoplays the owlcarousel after the user manually cycles the first item. If "owlcarousel", autoplays the owlcarousel on load.', max_length=255, verbose_name='Ride')),
                ('carousel_wrap', models.BooleanField(default=True, help_text='Whether the owlcarousel should cycle continuously or have hard stops.', verbose_name='Wrap')),
                ('carousel_aspect_ratio', models.CharField(blank=True, choices=[('1x1', '1x1'), ('3x2', '3x2'), ('4x3', '4x3'), ('21x9', '21x9'), ('18x9', '18x9'), ('4x1', '4x1')], default='', help_text='Determines width and height of the image according to the selected ratio.', max_length=255, verbose_name='Aspect ratio')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='OwlCarouselSlide',
            fields=[
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Display name')),
                ('external_link', models.URLField(blank=True, help_text='Provide a valid URL to an external website.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('mailto', models.EmailField(blank=True, max_length=255, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('target', models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Target')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='owl_carousel_owlcarouselslide', serialize=False, to='cms.CMSPlugin')),
                ('carousel_content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', help_text='Content may also be added using child plugins.', verbose_name='Content')),
                ('tag_type', djangocms_bootstrap4.fields.TagTypeField(choices=[('div', 'div'), ('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside')], default='div', help_text='Select the HTML tag to be used.', max_length=255, verbose_name='Tag type')),
                ('carousel_image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Slide image')),
                ('internal_link', models.ForeignKey(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

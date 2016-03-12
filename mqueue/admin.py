# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mqueue.models import MEvent
from mqueue.conf import EVENT_CLASSES


EVENT_CLASSES=getattr(settings, 'MQUEUE_EVENT_CLASSES', EVENT_CLASSES)


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'

def link_to_object_admin(obj):
    return '<a href="'+obj.admin_url+'" target="_blank">'+obj.admin_url+'</a>'

def format_event_class(obj):
    if obj.event_class in EVENT_CLASSES.keys():
        return '<span class="'+EVENT_CLASSES[obj.event_class]+'">'+obj.event_class+'</span>'
    else:
        return '<span class="'+EVENT_CLASSES['Default']+'">'+obj.event_class+'</span>'
    
def format_content_type(obj):
    if obj.content_type:
        return obj.content_type.name
    else:
        return ''

def format_user(obj):
    if obj.user:
        return obj.user.username
    else:
        return ''
    
    
@admin.register(MEvent)
class MEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_posted'
    read_only = ['date_posted']
    list_display = ['name', link_to_object, link_to_object_admin, format_content_type, 'date_posted', format_user, format_event_class]
    list_filter = (
        'event_class',
        'content_type',
        ('user', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'user__username', 'event_class']
    link_to_object.allow_tags = True   
    link_to_object.short_description = _(u'See on site')
    link_to_object_admin.allow_tags = True   
    link_to_object_admin.short_description = _(u'See in admin')
    format_event_class.allow_tags = True   
    format_event_class.short_description = _(u'Class')
    format_user.short_description = _(u'User')
    format_content_type.short_description = _(u'Content type')
    

    
    



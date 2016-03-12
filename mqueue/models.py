# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


class MEventManager(models.Manager):
    def create(self, *args, **kwargs):
        if not 'name' in kwargs.keys():
            raise ValueError(u"You must provide a 'name' argument for the MEvent")
        else:
            name = kwargs['name']
        obj_pk = None
        if 'obj_pk' in kwargs.keys():
            obj_pk = kwargs['obj_pk'] 
        content_type = None
        if 'model' in kwargs.keys():
            content_type = ContentType.objects.get_for_model(kwargs['model'])
        user = None
        if 'user' in kwargs.keys():
            user = kwargs['user']
        notes = ''
        if 'notes' in kwargs.keys():
            notes = kwargs['notes']
        url = ''
        if 'url' in kwargs.keys():
            url = kwargs['url']
        admin_url = ''
        if 'admin_url' in kwargs.keys():
            admin_url = kwargs['admin_url']
        event_class = ''
        if 'event_class' in kwargs.keys():
            event_class = kwargs['event_class']
        mevent = MEvent(name=name, content_type=content_type, obj_pk=obj_pk, user=user, url=url, admin_url=admin_url, notes=notes, event_class=event_class)
        mevent.save(force_insert=True)
        return mevent


class MEvent(models.Model):
    #~ required fields
    content_type = models.ForeignKey(ContentType, null=True, verbose_name=_(u"Content type"))
    obj_pk = models.IntegerField(blank=True, null=True, verbose_name=_(u"Object primary key"))
    name = models.CharField(max_length=120, verbose_name=_(u"Name"))
    #~ content fields
    url = models.CharField(max_length=255, blank=True, verbose_name=_(u"Url"))
    admin_url = models.CharField(max_length=255, blank=True, verbose_name=_(u"Admin url"))
    notes = models.TextField(blank=True)
    #~ meta
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date posted"))
    event_class = models.CharField(max_length=120, blank=True, verbose_name=_(u"Class"))
    user = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name=_(u'User'))   
    #~ manager
    objects = MEventManager()
    
    class Meta:
        verbose_name = _(u'Events')
        verbose_name_plural = _(u'Events')
        ordering = ['-date_posted']
        
    def __unicode__(self):
        return self.name+' - '+str(self.date_posted)
    
class MonitoredModel(models.Model):
    
    class Meta:
        abstract = True
    

    
    
        
        
        

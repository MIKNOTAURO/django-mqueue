# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

def get_subclasses(cls):
    result = [cls]
    classes_to_inspect = [cls]
    while classes_to_inspect:
        class_to_inspect = classes_to_inspect.pop()
        for subclass in class_to_inspect.__subclasses__():
            if subclass not in result:
                result.append(subclass)
                classes_to_inspect.append(subclass)
    return result

def get_object_name(instance, user):
    obj_name=''
    try:
        obj_name=instance.__unicode__()
    except AttributeError:
        try:
            obj_name = ' '+instance.name
        except:
            try:
                obj_name = ' '+instance.title
            except:
                try:
                    obj_name = ' '+instance.slug
                except:
                    try:
                        obj_name = ' '+str(instance.pk)
                    except:
                        pass
    if obj_name:
        if len(obj_name) >= 45:
            obj_name = obj_name[:45]+'...'
    obj_name = instance.__class__.__name__+' '+obj_name
    if user:
        obj_name += ' ('+user.username+')'
    return obj_name

def get_user(instance):
    user = None
    try:
        user = instance.user
    except:
        try:
            user = instance.editor
        except:
            pass
    return user

def get_url(instance):
    url = ''
    get_event_object_url = getattr(instance.__class__, 'get_event_object_url', None)
    if callable(get_event_object_url):
        url = instance.get_event_object_url()
    get_absolute_url = getattr(instance.__class__, 'get_absolute_url', None)
    if callable(get_absolute_url):
        url = instance.get_absolute_url()
    return url

def get_admin_url(instance):
    admin_url = reverse('admin:%s_%s_change' %(instance._meta.app_label,  instance._meta.model_name),  args=[instance.id] )
    return admin_url

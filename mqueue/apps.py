import importlib
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class MqueueConfig(AppConfig):
    name = "mqueue"
    verbose_name = _(u"Events queue")

    def ready(self):
        # models registration from settings
        from django.conf import settings
        from mqueue.tracking import mqueue_tracker
        registered_models = getattr(settings, 'MQUEUE_AUTOREGISTER', [])
        for modtup in registered_models:
            modpath = modtup[0]
            level = modtup[1]
            modsplit = modpath.split('.')
            path = '.'.join(modsplit[:-1])
            modname = '.'.join(modsplit[-1:])
            try:
                module = importlib.import_module(path)
                model = getattr(module, modname)
                mqueue_tracker.register(model, level)
            except ImportError:
                from mqueue.models import MEvent
                msg = "ERROR from Django Mqueue : can not import model " + modpath
                MEvent.objects.create(
                    name=msg, event_class="Error")

        # watchers
        from mqueue.watchers import init_watchers
        from mqueue.conf import WATCH
        init_watchers(WATCH)

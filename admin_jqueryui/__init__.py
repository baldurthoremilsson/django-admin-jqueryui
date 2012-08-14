from django.contrib.admin.options import ModelAdmin
try:
    from django.contrib.staticfiles.templatetags.staticfiles import static
except ImportError:
    static = lambda path: path


ModelAdmin.old_media = ModelAdmin.media

def new_media(self):
    media_instance = self.old_media
    media_instance.add_js(('admin_jqueryui/js/admin_jqueryui.min.js',))
    return media_instance

ModelAdmin.media = property(new_media)

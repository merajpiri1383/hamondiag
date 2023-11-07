from settings.models import Settings
def setting(request):
    object = Settings.objects.all().first()
    return {
        "settings": object
    }
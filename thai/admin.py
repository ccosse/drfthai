from django.contrib import admin
from thai.models import *


class PhraseAdmin(admin.ModelAdmin):
	model=Phrase
	list_display=('id','title')
admin.site.register(Phrase,PhraseAdmin)

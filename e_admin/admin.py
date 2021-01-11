from django.contrib import admin
from .models import GrupKandidat, Kandidat, Pemilih, Voting

# Register your models here.

@admin.register(Kandidat)
class KandidatAdmin(admin.ModelAdmin):
    '''Admin View for Kandidat'''

    # list_display = ('',)
    list_filter = ('grup',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ('published','updated')
    search_fields = ('name',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    '''Admin View for Voting'''

    # list_display = ('',)
    # list_filter = ('grup',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ['slug']
    # search_fields = ('name',)
    # date_hierarchy = ''
    # ordering = ('',)

admin.site.register(GrupKandidat)
admin.site.register(Pemilih)

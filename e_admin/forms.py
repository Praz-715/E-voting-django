from django import forms
from .models import GrupKandidat, Kandidat, Voting

class VotingForm(forms.ModelForm):
    """Form definition for Voting."""

    class Meta:
        """Meta definition for Votingform."""

        model = Voting
        fields = ('namavoting', 'deskripsi', 'user')

class PemilihVotingForm(forms.ModelForm):
    """Form definition for PemilihVoting."""

    class Meta:
        """Meta definition for PemilihVotingform."""

        model = Voting
        fields = ('batas','pilihanumum')


class GrupKandidatForm(forms.ModelForm):
    """Form definition for GrupKandidat."""

    class Meta:
        """Meta definition for GrupKandidatform."""

        model = GrupKandidat
        fields = ('group_name', 'voting')

class KandidatForm(forms.ModelForm):
    """Form definition for Kandidat."""

    class Meta:
        """Meta definition for Kandidatform."""

        model = Kandidat
        fields = ('foto','nama','deskripsi', 'grup')


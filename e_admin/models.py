from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User

class Voting(models.Model):
    """Model definition for Voting."""

    # TODO: Define fields here
    namavoting  = models.CharField(max_length=255)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deskripsi   = models.TextField()
    batas       = models.PositiveSmallIntegerField()
    pilihanumum = models.BooleanField(default=False)
    slug        = models.SlugField()

    class Meta:
        """Meta definition for Voting."""

        verbose_name = 'Voting'
        verbose_name_plural = 'Votings'

    def __str__(self):
        """Unicode representation of Voting."""
        return "{}. {}".format(self.user, self.namavoting)

    def save(self):
        """Save method for Artikel."""
        self.slug = slugify("{} | {}".format(self.namavoting,self.deskripsi))
        super().save()


# Create your models here.

class Pemilih(models.Model):
    """Model definition for Pemilih."""

    # TODO: Define fields here
    token       = models.CharField(max_length=10,unique=True)
    nama        = models.CharField(max_length=255,null=True,blank=True)
    email       = models.EmailField(null=True,blank=True)

    pil1        = models.PositiveIntegerField(null=True,blank=True)
    pil2        = models.PositiveIntegerField(null=True,blank=True)
    pil3        = models.PositiveIntegerField(null=True,blank=True)
    pil4        = models.PositiveIntegerField(null=True,blank=True)
    pil5        = models.PositiveIntegerField(null=True,blank=True)
    pil6        = models.PositiveIntegerField(null=True,blank=True)

    voting      = models.ForeignKey('Voting', on_delete=models.CASCADE)
    status      = models.CharField(
        max_length=5,
        choices=[('BELUM','belum'),('SUDAH','sudah')],
        default='BELUM'
    )


    class Meta:
        """Meta definition for Pemilih."""

        verbose_name = 'Pemilih'
        verbose_name_plural = 'Pemilihs'

    def __str__(self):
        """Unicode representation of Pemilih."""
        return self.token
        

class GrupKandidat(models.Model):
    """Model definition for GrupKandidat."""

    # TODO: Define fields here
    group_name  = models.CharField(max_length=100)
    voting      = models.ForeignKey('Voting', on_delete=models.CASCADE)


    class Meta:
        """Meta definition for GrupKandidat."""

        verbose_name = 'GrupKandidat'
        verbose_name_plural = 'GrupKandidats'

    def __str__(self):
        """Unicode representation of GrupKandidat."""
        return self.group_name


class Kandidat(models.Model):
    """Model definition for Kandidat."""

    # TODO: Define fields here
    nama        = models.CharField(max_length=255)
    deskripsi   = models.TextField()
    suara       = models.PositiveIntegerField(default=0)
    grup        = models.ForeignKey(GrupKandidat, on_delete=models.CASCADE)
    foto        = models.FileField(null=True,upload_to='images/')
    published   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)



    class Meta:
        """Meta definition for Kandidat."""

        verbose_name = 'Kandidat'
        verbose_name_plural = 'Kandidats'

    def __str__(self):
        """Unicode representation of Kandidat."""
        return "{}. {}".format(self.grup, self.nama)



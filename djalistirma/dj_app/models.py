from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    noteauthor = models.ForeignKey(User, verbose_name=("Yazar"), on_delete=models.CASCADE)
    note_title = models.CharField(("Note Başlığı"), max_length=50)
    note_content = models.TextField(("Not İçeriği"),max_length=400)
    note_image = models.FileField(("Not Resmi"), upload_to="uplods/blog", max_length=100, blank=True)
    note_url = models.URLField(("Note Url"), max_length=200, blank=True, null=True)
    approved = models.BooleanField(("Onay Aşaması"), default=False,help_text="Not Onaylandımı ?")
    notsil = models.BooleanField(("Notu Silebilirmi"),default=False,help_text="Kullanıcı Notu Silebilirmi")
    note_createdat = models.DateTimeField(("Oluşturulma zamanı"), auto_now=True)
    def __str__(self) :
        return "Yazıyı {author} yazdı".format(author = self.noteauthor.username)



class logo(models.Model):
    logo_img = models.FileField(("Logo"), upload_to="uplods/logo", max_length=100)

    def __str__(self):
        return "Sadece 1 tane resim girin"
    

class banned(models.Model):
    authorized = models.ForeignKey(User, verbose_name=("Kim banladı"), on_delete=models.CASCADE)
    banneduser = models.ForeignKey(User, verbose_name=("Banlanan kişi"), related_name="banneduser", on_delete=models.CASCADE)
    sebep = models.CharField(("Sebebi"), max_length=200)
    tarih = models.DateTimeField(("Banlanma Zamanı"), auto_now=True)
    
    def __str__(self):
        return self.banneduser.username


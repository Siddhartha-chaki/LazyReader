from django.db import models
#processing languge
LANGS=[
    ('hi','Hindi'),
    ('mr','Marathi'),
    ('bn','Bengali'),
    ('ta','Tamil'),
    ('ur','Urdu'),
    ('en','English')
]
# Create your models here.
class Image(models.Model):
    imgs = models.ImageField(upload_to="Images")
    language=models.CharField(max_length=15,choices=LANGS,default=LANGS[5])
    title = models.CharField(max_length=100)
    res_img=models.ImageField(upload_to="res_img",default="dummy.png")
    content=models.TextField()
    songfile = models.FileField()
    isPlaying = False

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = ['id']

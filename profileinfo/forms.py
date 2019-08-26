from django import forms

class postform(forms.Form):
    posted_by = models.ForeignKey(User , on_delete=models.CASCADE , null = True)
    title = models.CharField(max_length = 40 , null = True)
    content = models.CharField(max_length = 1500 , null = True)
    cover_photo = models.ImageField()

class messageform(forms.Form):
    message = models.CharField(max_length = 500 , null = True)
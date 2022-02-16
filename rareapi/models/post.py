from django.db import models

class Post(models.Model): 
    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    approved = models.BooleanField(default=True)    

from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):

    class Meta:
        model=PhotoPost
        fields=['country','title','comment','itinerary','days1','days2','season1','season2','image1','image2','image3','image4']
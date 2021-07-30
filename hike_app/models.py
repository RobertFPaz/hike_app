from django.db import models
import re
import datetime
from datetime import datetime
from datetime import date

class HikeManager(models.Manager):
    def hike_validation(self,postData):
        errors={}

        date=datetime.today()
        new_date=datetime(date.year, date.month, date.day)

        name_regex= re.compile(r'^[a-zA-Z ]+$')
        if len(postData['event_name']) == 0:
            errors['missing_event_name']="Event name must be included."
        elif not name_regex.match(postData['event_name']):
            errors['regex_event_name']="Event name must only contain letters."
        elif len(postData['event_name']) < 5:
            errors['length_event_name']="Event name must be at least five characters."
        if len(postData['location']) == 0:
            errors['missing_location']="Location must be included."   
        elif len(postData['location']) < 5:
            errors['length_location']="Location name must be at least five characters."
        elif not name_regex.match(postData['location']):
            errors['regex_location']="Location name must only contain letters."
        if len(postData['description']) == 0:
            errors['missing_description'] = "Description must be included."
        elif len(postData['description']) < 10:
            errors['length_description']="Description must be at least ten characters."
        if len(postData['distance']) == 0:
            errors['missing_distance'] = "Distance must be included."
        elif float(postData['distance']) < 1:
            errors['distance'] = "Distance must be at least one mile."
        if len(postData['max_attendees']) == 0:
            errors['missing_max_attendees'] = "Number of attendees must be included."
        elif int(postData['max_attendees']) > 15 or int(postData['max_attendees']) < 2:
            errors['max_attendees'] = "Number of hikers allowed must be between 2 and 15."
        if len(postData['date']) == 0:
            errors['missing_date'] = "Date must be selected"
        elif datetime.strptime(postData['date'],'%Y-%m-%d') <= new_date:
            errors['date']= "Date of hike must be in the future."
        
        return errors

class Hike(models.Model):
    event_name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    description=models.TextField()
    distance=models.FloatField(default=0)
    max_attendees=models.IntegerField()
    difficulty=models.CharField(max_length=60)
    pets=models.CharField(max_length=10)
    date=models.DateField()
    time=models.CharField(max_length=60)
    user = models.ForeignKey("login_app.User", related_name="hikes", on_delete=models.CASCADE)
    attend=models.ManyToManyField("login_app.User", related_name="user_hikes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=HikeManager()

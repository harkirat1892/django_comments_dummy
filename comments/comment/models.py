from django.db import models

# Create your models here.


class MainComment(models.Model):
    text = models.CharField(max_length=500, default='')

    created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Comment text is: " + self.text


class SubComment(models.Model):
    # The relation with parent comment, under which this one has been added
    # Set to CASCADE, because if parent comment is deleted, delete the sub comments too?
    response_to = models.ForeignKey(MainComment, related_name='sub_comments', on_delete=models.CASCADE)

    text = models.CharField(max_length=500, default='')

    created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '%d: %s' % (self.id, self.text)

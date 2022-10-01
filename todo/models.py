from django.db import models

# Create your models here.
class Todo(models.Model):
	PRIORITIES = (
		('red', 'RED'),
		('green', 'GREEN'),
		('yellow', 'YELLOW'),
		)
	title = models.CharField('Title',max_length=200)
	text = models.CharField('Text', max_length=800,blank=True)
	date = models.DateTimeField('Time', auto_now_add=True)
	done = models.BooleanField('Done ?', default=False)
	priority = models.CharField('Priority',max_length=50,choices=PRIORITIES, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
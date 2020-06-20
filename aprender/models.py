from django.db import models

# Create your models here.
class Quiz(models.Model):
    """
    Exam's model, works as a wrapper for the questions
    """
    name = models.CharField(max_length=100, verbose_name=u'Quiz name', )
    displayName = models.CharField(max_length=100, verbose_name=u'Display name', )
    #slug = models.SlugField()

    def __str__(self):
        return self.displayName

class Question(models.Model):
	MC = 'MC'
	FI = 'FI'
	TYPE_CHOICES = [(MC,'MC'),(FI,'FI'),]
	ques_Type = models.CharField(max_length=2,choices=TYPE_CHOICES,default=MC,)
	question = models.CharField(max_length=250,)
	#quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE,related_name="questions",)
	quiz = models.ManyToManyField(Quiz,related_name="questions",)
	answer = models.CharField(max_length=150)
	choice1 = models.CharField(max_length=150,blank=True)
	choice2 = models.CharField(max_length=150,blank=True)
	choice3 = models.CharField(max_length=150,blank=True)
	choice4 = models.CharField(max_length=150,blank=True)
	imgPath = models.CharField(max_length=250,blank=True)
	resourcePath = models.CharField(max_length=250,blank=True)
	def __str__(self):
		return '%s' % (self.question)

# class Choice(models.Model):
#     question = models.ForeignKey("Question", on_delete=models.CASCADE,related_name="choices")
#     choice = models.CharField("Choice", max_length=50)
#     position = models.IntegerField("position")

#     class Meta:
#         unique_together = [
#             # no duplicated choice per question
#             ("question", "choice"), 
#             # no duplicated position per question 
#             ("question", "position") 
#         ]
#         ordering = ("position",)
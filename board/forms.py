from django.forms import ModelForm
from board.models import *

class Form(ModelForm):
	class Meta:
		model = Article
		fields = ['name', 'title', 'contents', 'email']

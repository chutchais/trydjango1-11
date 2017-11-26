from django import forms

from .models import Item
from resturants.models import RestaurantLocation

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields =[
			'restaurant',
			'name',
			'contents',
			'excludes',
			'public'
		]

	def __init__(self,user=None,*args,**kwargs):
		# print(kwargs.pop('user'))
		print(user)
		# print(kwargs.pop('instance'))
		print(kwargs)
		super(ItemForm,self).__init__(*args,**kwargs)
		self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user) #.exclude(item__isnull=False)




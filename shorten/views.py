from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Links
from .forms import LinkForm

class LinkView(TemplateView):
	template_name = 'shorten/index.html'
	your_domain = 'https://getitshort.herokuapp.com/'

	def get(self, request):
		form = LinkForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = LinkForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['link']
			form = Links(link=text)
			form.save()
			link_id = Links.objects.only('id').get(link=text).id
			return HttpResponse(f'Your shorten link: {self.your_domain}{link_id}')

		args = {'form':form, 'text':text}
		return render(request, self.template_name, args)


	def results(request, shorten_id):
		database = Links.objects.filter(id=shorten_id)
		linkus = database[0].link
		if 'http' not in linkus:
			linkus = f'https://{linkus}'
		return redirect(str(linkus))		

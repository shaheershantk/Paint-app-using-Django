from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import Images
import json

# Create your views here.
def paint(request):
	
	images = Images.objects.all()
	return render(request,'paint.html',{ 'images' : images})

@csrf_exempt
def gallery(request,imagename=None):
	print imagename
	if request.method == 'POST':
		title = request.POST['pname']
		img_data = request.POST['pdata']
		p = Images(title = title, img_data = img_data)
		p.save()
	if request.method == 'GET':
		image = Images.objects.filter(title = imagename)
		for i in image:
			data = i.img_data
		print json.dumps(data)
		t = get_template('paint.html')
		html = t.render(Context({}))
		if data:
			html="""<script>var data=JSON.parse(' """+data+""" ');</script>"""+html		
		else:
			html="""<script>alert("Image not found")</script>"""+html
		return HttpResponse(html)
		 
	

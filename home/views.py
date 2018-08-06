from django.shortcuts import render, HttpResponse
import json

def simpleajax(request):
    if request.method == 'POST':
        if request.is_ajax():

            data1 = request.POST['field1']
            output = [{"field1": data1}]

            return HttpResponse(json.dumps(output), content_type='application/json')

    return render(request)


def index(request, template='home/index.html'):
    return render(request, template)

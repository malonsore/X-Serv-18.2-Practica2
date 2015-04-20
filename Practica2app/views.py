# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from models import Practica2appData
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Practica2 (request, recurso):
	recurso = request.path
	
	formulario = ('<form action="" method="POST"> Solicita tu URL corta:'	
				+'<input type="text" name="nombre" value="" /><br/>'
					+ '<input type="submit" value="Enviar" /></form>')

	if request.method == "POST":
		cuerpo = request.body.split("=")[1];
		print "Cuerpo " + cuerpo

 		if cuerpo == "":
			htmlBody = ("<html><body>No se introdujo URL</body></html>")				
	 		return HttpResponseNotFound(htmlBody)
		elif cuerpo.find("http") == -1:
			cuerpo = "http://" + cuerpo				
		else:
			cuerpo = (cuerpo.split("%3A%2F%2F")[0] + "://" +cuerpo.split("%3A%2F%2F")[1])

	  	corta = Practica2appData.objects.filter(larga=cuerpo)
		
		if not corta.values("corta"):
			num = Practica2appData.objects.count() + 1
			b = Practica2appData(corta=str(num), larga=cuerpo)
			b.save()
		else:
			num = corta.values("corta")[0]["corta"]		

		htmlBody = ("<html><body>" +
				"<h1>URL original y acortada:</h1>" +
				"<a href=" + cuerpo + ">" + cuerpo + "</href></br>" +
				"<a href=" + str(num)  + ">" +
				str(num) + "</href></body></html>")
		return HttpResponse(htmlBody)

	elif request.method == "GET":
		print "Recurso" + recurso
		if recurso == '/':
			htmlBody = ""
			salida = "<p><b>Lista URLS</b></p>"
			urls = Practica2appData.objects.all()
			for fila in urls:
				htmlBody += "<p> Larga: "+ fila.larga + " // Corta: " + fila.corta + "</p>"

			return HttpResponse(salida + htmlBody + formulario)
		else:

	  		x = Practica2appData.objects.filter(corta=recurso.split('/')[1])

			if x.values("larga"):
				htmlBody = "<html><body>Redirigiendo...</body></html>"
				direccion = x.values("larga")[0]
				return HttpResponseRedirect(direccion["larga"])
			else:
				htmlBody = ("<html><body>Not Found </body></html>")
	 			return HttpResponseNotFound(htmlBody)
	else:
		htmlBody = "<html><body>Metodo no entendido</body></html>"
	 	return HttpResponseNotFound(htmlBody)





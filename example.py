# -*- coding: utf-8 -*-

from ci_uy import CedulaUruguaya

cedula = CedulaUruguaya()

print "\n--- Verifica tu cedula ---"
ci1 = raw_input("Ingresa tu cedula sin el digito verificador: ")
if cedula.validate_ci(int(ci1)):
	print "¡La cedula que has ingresado es valida!"
else:
	print "La cedula que has ingresado no es valida..."

print "\n\n--- MAS EJEMPLOS PROXIMAMENTE! ---"
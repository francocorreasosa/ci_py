# -*- coding: utf-8 -*-

import random

class CedulaUruguaya:
	def get_validation_digit(self, ci):
		a = 0
		i = 0
		if len(str(ci)) <= 6:
			for i in xrange(len(ci), 7):
				ci = '0' + ci
				i = i + 1

		for i in xrange(0,7):
			a += (int("2987634"[i]) * int(str(ci)[i])) % 10
			i = i + 1

		if a % 10 == 0:
			return 0
		else:
			return 10 - a % 10

	def clean_ci(self, ci):
		return int(str(ci).replace("-",""))
		return int(str(ci).replace("/",""))
		return int(str(ci).replace(".",""))

	def validate_ci(self, ci):
		ci = self.clean_ci(ci)
		dig = int(str(ci)[int(len(str(ci))) - 1])
		#ci  = ci.replace(/[0-9]$/, '')
		return dig == self.get_validation_digit(ci)

	def random_ci(self):
		ci = random.randint(0000000,9999999)
		return int(str(ci) + str(self.get_validation_digit(ci)))


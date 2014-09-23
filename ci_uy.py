# -*- coding: utf-8 -*-

#The MIT License (MIT)
#
#Copyright (c) 2014 Franco Correa
#
#Permission is hereby granted, free of charge, #to any person obtaining a copy
#of this software and associated documentation #files (the "Software"), to deal
#in the Software without restriction, #including without limitation the rights
#to use, copy, modify, merge, publish, #distribute, sublicense, and/or sell
#copies of the Software, and to permit persons #to whom the Software is
#furnished to do so, subject to the following #conditions:
#
#The above copyright notice and this #permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.



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


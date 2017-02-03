def size(num):
	'''Basic byte to human conversion'''
	unit = 'MB'
	num = num/1024/1024.0

	if num>1000:
		num = num/1024
		unit = 'GB'

	if num>1000:
		num = num/1024
		unit = 'TB'

	num = round(num,2)

	return str(num),unit

def bytesize(num):
	'''Converts human readable file sizes into actual size'''

	if not num[-1].isalpha():
		print 'Please use 30G format, number ending in a letter'
		return False
	if num[-1] in ['k','K']:
		return int(num[:-1]) * 1024
	elif num[-1] in ['m','M']:
		return (int(num[:-1]) * 1024) * 1024
	elif num[-1] in ['g','G']:
		return ((int(num[:-1]) * 1024) * 1024) * 1024
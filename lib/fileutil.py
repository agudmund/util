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
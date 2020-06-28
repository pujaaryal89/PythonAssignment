def add(tag, word):
    	return "<%s>%s</%s>" % (tag, word, tag)
print(add('i', 'Python'))
print(add('b', 'Python Tutorial'))
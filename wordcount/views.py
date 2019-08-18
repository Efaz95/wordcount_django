from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	word_dictionary = {}

	for word in wordlist:
	    if word not in word_dictionary:
	        word_dictionary[word] = 1
	    else:
	        word_dictionary[word] += 1

	sorted_list = sorted(word_dictionary.items(), key=lambda tup: tup[1], reverse=True)
	return render(request, 'count.html', {'fulltext':fulltext, 'wordlist':len(wordlist), 'word_dictionary':sorted_list})
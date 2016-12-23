#creating housekeeping functions. This program is made to scrap a website but all the functions are made by me. It doesn't use scerapy or beautifulsoup.
#The libraries used are solely urllib and os related

import os

#create a directory if it doesn't already exist
def create_project_dir(directory):	
	if not os.path.exists(directory):
		print("Creating directory: " + directory)
		os.makedirs(directory)

#creates a .txt file for the queue which stores the links crawled by spider
#creates a .txt file for the crawwled links
def Create_data_files(project_name, base_url):
	queue= project_name + '/queue.txt'
	crawled = project_name + 'crawled.txt'
	if not os.path.isfile(queue, base_url):
		write_file(queue)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

#housekeeping function to write a file
def write_file(path, data)
	f = open(path, 'w')
	f.write(data)
	f.close()

def append_to_file(path, data):
	with open(path, 'a') as f:
		f.write(data + '\n')

def delete_file_contents(path):
	with open(path, 'w'):
		pass

def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		append_to_file(file, link)
		
	


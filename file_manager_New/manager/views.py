from django.shortcuts import render, reverse, HttpResponse, get_object_or_404, redirect
import os
import subprocess
from django.http import JsonResponse
# Create your views here.
 
def index(request):
    return render(request,'index.html' )   

def list_folders(request, directory):
    # if directory.startswith("\\"):
    
    paths= [fr"\\multad\EN7B\FOCUSSED_PROJECTS\{directory}" , fr"\\multad\DCM-ERD-TA\2022-23\Feb-23\{directory}" , fr"{directory}"]
    
    for file_path in paths:
        if os.path.exists(file_path):
            file_in_directory = os.path.join(file_path)
            print(file_in_directory)
            if os.path.exists(file_in_directory):
                os.startfile(file_in_directory, 'open')
                return HttpResponse('<script type="text/javascript">alert("File Open Successfully!");window.history.back();</script>')
            else:
                return HttpResponse('<script type="text/javascript">alert("File not found!");window.history.back();</script>')

            # Get the list of folders and files 
    items = os.listdir(directory)

    items_list =[]
    for item in items:
        item_dict = {'name': item}
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            item_dict['type'] = 'folder'
            item_dict['url'] = f"{directory}/{item}"
        else:
            item_dict['type'] = 'file'
            item_dict['url'] = full_path
        items_list.append(item_dict)
    # print(items_list)
    context = {'directory':directory, 'items_list': items_list}
    return render(request, 'list_folders.html', context)



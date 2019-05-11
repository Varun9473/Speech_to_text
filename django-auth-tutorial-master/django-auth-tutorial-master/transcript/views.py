from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from accounts.models import fileupload
from django.contrib import messages
import speech_recognition as sr

# from transcript import script

# import speech_recognition as sr
# Create your views here.
def transcript(request, id=None):
    D = fileupload.objects.get(id=id)
  
    
    
    r=sr.Recognizer()
    
    var=sr.AudioFile(r"C:\Users\varum\Desktop\Django Projects\django-auth-tutorial-master\django-auth-tutorial-master\transcript\file.wav")
    with var as source:
        audio = r.record(source)

    st=r.recognize_google(audio)
    with open(r"C:\Users\sachin\Desktop\django-auth-tutorial-master\django-auth-tutorial-master\media\transcript\Output"+str(id)+".txt", "w+") as p:
        p.seek(0)
        p.write(st)

    t = fileupload.objects.get(id=id)
    t.text_url = "media/transcript/Output"+str(id)+".txt"
    t.save(update_fields=['text_url'])
    t.save()
    data={'obj1':st , 'file':p , 'obj2':D}
    
    return render(request, 'transcript.html',data)

def deletefile(request, id):
    D = fileupload.objects.get(id=id)
    D.delete()
    messages.success(request, 'File Deleted!')
    return redirect('/home/')


def Download(request):
    with open("Output.txt", "r") as q:
        jk=q.read()
        return HttpResponse(jk, content_type='application/force-download/vnd.txt')
    


def update(request):
    if request.method=='POST':
        id=request.POST.get('id')
        stt=request.POST.get('text-file1')
        

        file=open(r"C:\Users\sachin\Desktop\django-auth-tutorial-master\django-auth-tutorial-master\media\edit\updatedfile"+id+".txt", "w+")
        # file.seek(0)
        # file.truncate()
        file.write(stt)
        
        t = fileupload.objects.get(id=id)
        t.updated_url = "media/edit/updatedfile"+str(id)+".txt"
        t.save(update_fields=['updated_url'])
        t.save()
        file.close()

        
    return HttpResponse('hello')
        
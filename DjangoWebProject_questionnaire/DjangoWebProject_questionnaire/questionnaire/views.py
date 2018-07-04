from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from . import models
# Create your views here.
def index(request):
    contents = models.grid.objects.all()
    contents = contents[1:11]
    return render(request, 'index.html' , {'contents':contents, 'id': 1})
    #content = models.Ariticle.objects.all()
    #return render(request, 'blog/index.html', {'content':content})
    #return HttpResponse("hello world")
def startx(request):
    return render(request,'start.html')
def callfunc(request):
    userip = request.META['REMOTE_ADDR']
    result = models.users.objects.filter(ip = userip)
    if result.exists():
        now_id = models.users.objects.get(ip = userip).now_query_id + 1
        contents = models.dataQuery2.objects.all()
        contents = contents[0+(now_id-1)*10:10+(now_id-1)*10]
    else:
        models.users.objects.create(ip = userip,now_query_id = 0)
        contents = models.dataQuery2.objects.all()
        contents = contents[0:10]
        now_id = 1
    return  render(request, 'index.html' , {'contents':contents, 'id':now_id})
def mainPage(request):
    return render(request,'ok.html')
def endPage(request):
    return render(request,'end.html')
def index_action(request,now_id):
    userip = request.META['REMOTE_ADDR']
    now_id = int(now_id)
    try:
        models.users.objects.filter(ip = userip).update(now_query_id = now_id)
    except:
        print("no id")
    
    for i in range(10):
        content = request.POST.get(str(i+1),'choice1')
        conment = request.POST.get('comment'+str(i+1),' ')
        models.results_final.objects.create(ip = userip, query_id = i+(now_id-1)*10+1,answer = content,comment = conment)
    if(int(now_id) == 10):
        return render(request,'end.html')
    now_id = int(now_id)+1
    contents = models.dataQuery2.objects.all()
    contents = contents[0+(now_id-1)*10:10+(now_id-1)*10]
    return render(request, 'index.html' , {'contents':contents, 'id':now_id})

def download_file(request):
    the_file_name='guideline.docx'             #显示在弹出对话框中的默认的下载文件名    

    filename='C:/guideline.docx'    #要下载的文件路径

    response=StreamingHttpResponse(readFile(filename))

    response['Content-Type']='application/octet-stream'

    response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)

    return response

 

def readFile(filename,chunk_size=512):

    with open(filename,'rb') as f:

        while True:

            c=f.read(chunk_size)

            if c:

                yield c

            else:

                break

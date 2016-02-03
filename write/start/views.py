from django.shortcuts import render

# Create your views here.
#http://www.cnblogs.com/haozi0804/p/4794428.html
#http://www.cnblogs.com/haozi0804/p/4794451.html
from django.http import   HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
import datetime
from django.template.loader import   get_template
from   django.template import Template, Context
def hello(request):
    return HttpResponse("Hello   world")
def current_datetime(request):
    now   = datetime.datetime.now()
    html   = "<html><body>It is now %s.</body></html>"   % now
    return HttpResponse(html)
def post_novel(request):
    now = datetime.datetime.now()
    t =   Template("<html><body>It is now {{ current_date   }}.</body></html>")
    html = t.render(Context({'current_date':   now}))
    return HttpResponse(html)
def use_databases(request):
    db = MySQLdb.connect(user='root', db='main', passwd='', host='localhost')
    cursor = db.cursor()
    cursor.execute('select * from  start_start')
    now = [row[0] for row in cursor.fetchall()]
    html   = "<html><body>It is now %s.</body></html>"   % {{now}}
    db.close()
    return HttpResponse(html)
    #return render_to_response(html)#('mytime.html', {'current_date': now})
def use_database(request):
    db = MySQLdb.connect(user='root', db='main', passwd='', host='localhost')
    cursor = db.cursor()
    cursor.execute('select * from  start_start')
    now = [row[2] for row in cursor.fetchall()]
    db.close()
    return render_to_response('current_datetime.html', {'current_date': now})

def index(request):
    db = MySQLdb.connect(user='root', db='main', passwd='', host='localhost')
    cursor = db.cursor()
    cursor.execute('select * from  start_start')
    now = [row[2] for row in cursor.fetchall()]
    db.close()
    return render_to_response('index.html',{'current_date': now})
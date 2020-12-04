from django.shortcuts import render
from g_stu.models import Grade,Student
# Create your views here.
def index(request):
    g = Grade(g_name="大数据一班")
    g.save()
    return render(request,"index.html")

def show(request):
    g_all = Grade.objects.all()
    print(g_all)
    for i in g_all:
        print(i.g_name)
    return render(request, "show.html",{
        "grade":g_all
    })


def student(request,id):
    gr = Grade.objects.filter(id=id).first()
    s = Student(s_name="宋晨博",age="20",sex="男",emali="250@qq.com",password="250",g=gr)
    s.save()
    return render(request,"scb.html",{"s":s})
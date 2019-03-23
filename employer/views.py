from django.http import HttpResponse
import json
from eims.models import WorkerInfo
from user.models import User
from datetime import datetime


def check(request):
    # 返回信息
    msg = 0
    # 登录检查
    if request.method == 'POST':
        try:
            item = User.objects.get(userName=request.POST.get('userName', ''))
            # 如果用户名为空
            if item.userName == '':
                return HttpResponse(msg)
            # 如果密码错误
            elif item.password != request.POST.get('password', ''):
                return HttpResponse(msg)
            else:
                msg = 1
                return HttpResponse(msg)
        # 如果用户名不存在
        except User.DoesNotExist:
            return HttpResponse(msg)


def submit(request):
    if request.method == 'POST':
        # 员工ID
        workerID = str(request.POST.get('workerID', ''))
        # 员工姓名
        name = str(request.POST.get('name', ''))
        # 员工年龄
        age = str(request.POST.get('age', ''))
        # 员工生日
        date = str(request.POST.get('birth', ''))
        birth = datetime(int(date[0:4]), int(date[5:7]), int(date[8:10])).strftime('%Y-%m-%d')
        # 员工电话
        phone = str(request.POST.get('phone', ''))
        # 员工职位
        position = str(request.POST.get('position', ''))
        # 写入数据库
        WorkerInfo.objects.create(workerID=workerID, name=name, age=age, birth=birth, phone=phone, position=position)
        msg = 'OK!'
        return HttpResponse(msg)


def search(request):
    dic = {}
    employee_list = []
    ans = []
    if request.method == 'GET':
        for item in WorkerInfo.objects.all():
            op = {
                'eid': item.workerID,
                'name': item.name,
                'age': item.age,
                'birth': str(item.birth),
                'tel': item.phone,
                'rank': item.position
            }
            ans.append(op)
        dic = json.dumps(ans)
    if request.method == 'POST':
        # 整理信息
        workerID = str(request.POST.get('workerID', ''))
        name = str(request.POST.get('name', ''))
        age = str(request.POST.get('age', ''))
        date = str(request.POST.get('birth', ''))
        position = str(request.POST.get('position', ''))
        for item in WorkerInfo.objects.all():
            employee_list.append(item)
        # 处理信息
        eid = []
        if workerID == '':
            print(workerID)
            if name == '':
                if age == '':
                    if date == '':
                        if position == '':
                            return HttpResponse(0)
                        else:
                            res = WorkerInfo.objects.filter(position=position)
                            for item in res:
                                eid.append(item.workerID)
                    else:
                        birth = str(datetime(int(date[0:4]), int(date[5:7]), int(date[8:10])+1).strftime('%Y-%m-%d'))
                        res = WorkerInfo.objects.filter(birth=birth)
                        for item in res:
                            eid.append(item.workerID)
                else:
                    for employee in employee_list:
                        if employee.age > int(age):
                            eid.append(employee.workerID)
            else:
                res = WorkerInfo.objects.filter(name=name)
                for item in res:
                    eid.append(item.workerID)
        else:
            res = WorkerInfo.objects.filter(workerID=workerID)
            for item in res:
                eid.append(item.workerID)
        # 准备信息
        for one in eid:
            target = WorkerInfo.objects.get(workerID=one)
            op = {
                'eid': target.workerID,
                'name': target.name,
                'age': target.age,
                'birth': str(target.birth),
                'tel': target.phone,
                'rank': target.position
            }
            ans.append(op)
        dic = json.dumps(ans)
    return HttpResponse(dic)

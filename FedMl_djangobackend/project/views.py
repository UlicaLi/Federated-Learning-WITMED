from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt 
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import subprocess
from django.http import FileResponse
import os
from django.conf import settings
import json
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
import zipfile
import time

User = get_user_model()

@csrf_exempt
@require_http_methods(['POST'])
def signup_view(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Username and password are required'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})



@csrf_exempt
@require_http_methods(['POST'])
def login_view(request):
    data = json.loads(request.body)
    print(data)
    username = data.get('username')
    password = data.get('password')
    print(f'username: {username}, password: {password}')
    user = authenticate(request, username=username, password=password)  
    print(user)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('admin:index'))  # 'admin:index'的URL模式
    else:
        raise Http404("User does not exist")
    
    
@csrf_exempt
@login_required
def create_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # 从POST数据中获取项目的名称、类型ID和描述
        project_name = data.get('project_name')
        project_type_id = data.get('project_type_id')
        project_description = data.get('project_description')
        print(f'project_name: {project_name}, project_type_id: {project_type_id}, project_description: {project_description}')
        # 获取当前登录的用户
       # user = request.user

        # 创建一个新的项目
        project = Project.objects.create(
            #user=user,
            project_name=project_name,
            project_type=project_type_id,
            project_description=project_description,
        )
        print(project.id)

        # 返回一个成功的响应
        return JsonResponse({'status': 'success', 'message': 'Project created successfully'})

    else:
        # 如果不是POST请求，返回一个错误的响应
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



@csrf_exempt
def create_model(request):
    if request.method == 'POST':
        # 从POST数据中获取模型的名称、ID、路径和项目ID
        model_name = request.POST.get('model_name')
        model_id = request.POST.get('model_id')
        project_id = request.POST.get('project_id')
        file = request.FILES.get('file')  # 获取上传的模型文件
        print(f'project_id: {project_id}')

        try:
            # 尝试获取相关的项目实例
            project = Project.objects.get(id=project_id)
        except ObjectDoesNotExist:
            # 如果项目不存在，返回一个错误的响应
            return JsonResponse({'status': 'error', 'message': 'Project does not exist'})

        # 创建一个新的模型实例
        model = Model.objects.create(
            model_name=model_name,
            model_id=model_id,
            model_path=os.path.join(settings.MEDIA_ROOT, file.name),
            file=file,  # 保存上传的模型文件
            project=project
        )

        # 返回一个成功的响应
        return JsonResponse({'status': 'success', 'message': 'Model created successfully'})

    else:
        # 如果不是POST请求，返回一个错误的响应
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    


@csrf_exempt
@login_required
def upload_train_data(request):
    if request.method == 'POST':
        file = request.FILES['file']
        data_name = request.POST['data_name']
        project_id = request.POST['project_id']

        train_data = TrainData.objects.create(
            data_name=data_name,
            data_path=os.path.join(settings.MEDIA_ROOT, file.name),
            file=file,
            project_id=project_id
        )

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
@login_required
def upload_predict_data(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        project_name = request.POST.get('project_name')
        print("接受成功")
        print(project_name)

        project = get_object_or_404(Project, project_name=project_name)  

        predict_data = PredictData.objects.create(
            #data_name=data_name,
            data_path=os.path.join(settings.MEDIA_ROOT, file.name),
            file=file,
            project=project
        )

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



@csrf_exempt
@login_required
def start_predict(request):
    if request.method == 'POST':
        # 从POST数据中获取模型ID和预测数据ID
        model_id = request.POST.get('model_id')
        data_id = request.POST.get('predict_data_id')

        # 获取模型和预测数据对象
        model = Model.objects.get(model_id=model_id)
        predict_data = PredictData.objects.get(data_id=data_id)
        print(model.file.path)
        print(predict_data.file.path)
        
        #运行predict.py脚本
        predict_script_path = os.path.join(settings.BASE_DIR, 'predict.py')
        subprocess.run(['python', predict_script_path, '--data_path', predict_data.file.path, '--model_path', model.file.path])
        
        #predict.py脚本生成了一个名为data_analysis_report.html的文件
        # 返回这个文件的内容给前端
        response = FileResponse(open(os.path.join('report', 'data_analysis_report.html'), 'rb'))
        return response

    else:
        # 如果不是POST请求，返回一个错误的响应
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
@login_required
def start_training(request):
    if request.method == 'POST':
        # 从POST数据中获取模型ID和训练数据ID
        model_id = request.POST.get('model_id')
        data_id = request.POST.get('train_data_id')

        # 获取模型和训练数据对象
        model = Model.objects.get(model_id=model_id)
        train_data = TrainData.objects.get(data_id=data_id)
        
        # 运行train.py脚本
        train_script_path = os.path.join(settings.BASE_DIR, 'train.py')
        subprocess.run(['python', train_script_path, '--data_path', train_data.file.path, '--model_path', model.file.path])
        
        # 返回一个成功的响应
        return JsonResponse({'status': 'success', 'message': 'Training started successfully'})

    else:
        # 如果不是POST请求，返回一个错误的响应
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



@csrf_exempt
@login_required 
def get_project_list(request):
    if request.method == 'GET':
        # 获取所有的项目
        projects = Project.objects.all()

        # 将项目列表转换为JSON格式
        project_list = [project.to_dict() for project in projects]
        return JsonResponse(project_list, safe=False)

    else:
        # 如果不是GET请求，返回一个错误的响应
        return JsonResponse({"error": "Invalid request method"}, status=400)
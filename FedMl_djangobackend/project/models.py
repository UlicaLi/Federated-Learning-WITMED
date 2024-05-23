
from django.conf import settings
from django.db import models



class Project(models.Model):
    # INTERNAL_MEDICINE = 'IM'
    # SURGERY = 'SU'
    # PEDIATRICS = 'PE'

    # PROJECT_TYPE_CHOICES = [
    #     (INTERNAL_MEDICINE, 'Internal Medicine'),
    #     (SURGERY, 'Surgery'),
    #     (PEDIATRICS, 'Pediatrics'),
    # ]
    
    PROJECT_TYPE_CHOICES = [
    ('内科', '内科'),
    ('外科', '外科'),
    ('儿科', '儿科'),
    ('妇科', '妇科'),
    ('眼科', '眼科'),
    ('耳鼻喉科', '耳鼻喉科'),
    ('皮肤科', '皮肤科'),
    ('骨科', '骨科'),
    ('神经科', '神经科'),
    ('心血管科', '心血管科'),
    ('肿瘤科', '肿瘤科'),
    ('康复科', '康复科'),
    ('麻醉科', '麻醉科'),
    ('口腔科', '口腔科'),
    ('精神科', '精神科'),
    ('急诊科', '急诊科'),
]
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    project_name = models.CharField(max_length=128, unique=True)
    project_type = models.CharField(max_length=100, choices=PROJECT_TYPE_CHOICES)
    project_description = models.TextField()

    def to_dict(self):
        return {
            'user': self.user.id,
            'project_name': self.project_name,
            'project_type': self.project_type,
            'project_description': self.project_description,
        }
    class Meta:
        db_table = 'Project'   # 指定数据库中的表名



class Model(models.Model):
    model_name = models.CharField(max_length=128)
    model_id = models.CharField(max_length=128)
    model_path = models.CharField(max_length=256)
    file = models.FileField(upload_to='models/', null=True)  # 新增的模型文件字段
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Model'
        
        


class TrainData(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=128)
    data_path = models.CharField(max_length=256)
    file = models.FileField(upload_to='train_data/', null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TrainData'
        
        
        
class PredictData(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=128)
    data_path = models.CharField(max_length=256)
    file = models.FileField(upload_to='predict_data/', null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        db_table = 'PredictData'
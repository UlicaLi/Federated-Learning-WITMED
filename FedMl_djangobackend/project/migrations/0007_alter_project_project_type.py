# Generated by Django 4.1 on 2024-03-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_model_file_alter_traindata_file_predictdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('内科', '内科'), ('外科', '外科'), ('儿科', '儿科'), ('妇科', '妇科'), ('眼科', '眼科'), ('耳鼻喉科', '耳鼻喉科'), ('皮肤科', '皮肤科'), ('骨科', '骨科'), ('神经科', '神经科'), ('心血管科', '心血管科'), ('肿瘤科', '肿瘤科'), ('康复科', '康复科'), ('麻醉科', '麻醉科'), ('口腔科', '口腔科'), ('精神科', '精神科'), ('急诊科', '急诊科')], max_length=100),
        ),
    ]

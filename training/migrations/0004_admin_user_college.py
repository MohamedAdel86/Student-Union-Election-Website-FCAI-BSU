# Generated by Django 4.1.7 on 2023-05-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_alter_nominee_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_user',
            name='college',
            field=models.CharField(choices=[('1', 'كلية الحاسبات و الذكاء الاصطناعى'), ('2', 'كلية الهندسة'), ('3', 'كلية الطب'), ('4', 'كلية طب الأسنان'), ('5', 'كلية الطب البيطرى'), ('6', 'كلية العلوم'), ('7', 'كلية الصيدلة'), ('8', 'كلية التمريض'), ('9', 'كلية التكنولوجيا و التعليم'), ('10', 'كلية الدراسات العليا للعلوم المتقدمة'), ('11', 'كلية علوم الملاحة و تكنولوجيا الفضاء'), ('12', 'كلية علوم ذوى الاحتياجات الخاصة'), ('13', 'كلية علوم الأرض'), ('14', 'كلية الفنون التطبيقية'), ('15', 'كلية تكنولوجيا العلوم الصحية التطبيقية'), ('16', 'كلية الزراعة'), ('17', 'كلية العلاج الطبيعى'), ('18', 'كلية الإعلام'), ('19', 'كلية التجارة'), ('20', 'كلية الآداب'), ('21', 'كلية التربية'), ('22', 'كلية الحقوق'), ('23', 'كلية التربية الرياضية'), ('24', 'كلية السياسة و الاقتصاد'), ('25', 'كلية التربية للطفولة المبكرة'), ('26', 'كلية الألسن'), ('27', 'كلية الخدمة الاجتماعية التنموية'), ('28', 'كلية السياحة و الفنادق')], default='كلية الحاسبات و الذكاء الاصطناعى', max_length=20),
            preserve_default=False,
        ),
    ]

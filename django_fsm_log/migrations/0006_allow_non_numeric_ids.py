from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fsm_log', '0005_description_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statelog',
            name='object_id',
            field=models.TextField(db_index=True),
        ),
    ]
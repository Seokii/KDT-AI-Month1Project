# Generated by Django 4.1.2 on 2022-10-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0004_post_head_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="file_upload",
            field=models.FileField(blank=True, upload_to="board/files/%Y/%m/%d"),
        ),
    ]

# Generated by Django 2.0 on 2017-12-22 21:51

from django.db import migrations, models
import xorgauth.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_add_account_fields_for_authgroupex'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='schoolid',
            field=xorgauth.utils.fields.UnboundedCharField(help_text='Identification defined by the School',
                                                           null=True, unique=True, verbose_name='School ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='xorgdb_uid',
            field=models.IntegerField(help_text='User ID in Polytechnique.org database', null=True,
                                      unique=True, verbose_name='Polytechnique.org database user ID'),
        ),
    ]

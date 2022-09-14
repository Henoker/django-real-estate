# Generated by Django 3.2.7 on 2022-09-14 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('timestampeduuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.timestampeduuidmodel')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+41524204242', max_length=30, region=None, verbose_name='Phone Number')),
                ('about_me', models.TextField(default='Say something about yourself', verbose_name='About me')),
                ('license', models.CharField(blank=True, max_length=20, null=True, verbose_name='Real Estate License')),
                ('profile_photo', models.ImageField(default='/profile_default.png', upload_to='', verbose_name='Profile Photo')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=20, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(default='KE', max_length=2, verbose_name='Country')),
                ('city', models.CharField(default='Nairobi', help_text='Are you looking to buy property?', max_length=180, verbose_name='City')),
                ('is_seller', models.BooleanField(default=False, help_text='Are you looking to sell a property?', verbose_name='Seller')),
                ('is_agent', models.BooleanField(default=False, help_text='Are you an agent?', verbose_name='Agent')),
                ('top_agent', models.BooleanField(default=False, verbose_name='Top Agent')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of Reviews')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('common.timestampeduuidmodel',),
        ),
    ]

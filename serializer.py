from rest_framework import serializers

from . models import employees


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__'

# to run the server python manage.py runserver
# to migrate DB python manage.py migrate
# to create migration python manage.py makemigrations
# to create web application python manage.py startapp webapp
#  to create project django-admin startproject myproject
# to insatll django pip install Django==3.0.7
# to install api framework pip3 install djangoapifreamwork

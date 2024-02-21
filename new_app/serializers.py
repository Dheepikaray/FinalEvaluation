from rest_framework import serializers

from new_app.models import blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('date','title','content','Information','Image')

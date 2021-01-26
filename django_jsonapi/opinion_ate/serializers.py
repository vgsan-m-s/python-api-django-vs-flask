from rest_framework_json_api import serializers
from opinion_ate.models import Restaurant, Dish

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'dish_set')

class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'rating', 'restaurant')
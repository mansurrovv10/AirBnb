from .models import (UserProfile,City,Country,Rules,Property,PropertyImage,Booking,Review)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'role',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class UserProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfilePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username','avatar']




class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username','avatar','role']



class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'




class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']




class CityPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name',]




class PropertyListSerializer(serializers.ModelSerializer):
    city = CityPropertySerializer()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['id', 'property_type', 'city', 'price_per_night', 'images', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'



class CityListSerializer(serializers.ModelSerializer):
    city_property = PropertyListSerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['city_name','city_property']





class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['property_image']




class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']



class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ['rules_name','rules_image']





class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    guest = UserProfileReviewSerializer()
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Review
        fields = ['id','guest','rating','comment','created_at']


class PropertyDetailSerializer(serializers.ModelSerializer):
    city = CityPropertySerializer()
    country = CountrySerializer()
    property_photos = PropertyImageSerializer(many=True, read_only=True)
    rules = RulesSerializer(many=True, read_only=True)
    property_review = ReviewSerializer(many=True, read_only=True)
    owner = UserProfilePropertySerializer()
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            'title', 'description','price_per_night', 'city', 'country','property_type',
            'rules', 'max_guests','bedrooms','bathrooms', 'property_photos', 'owner',
            'property_review','address','is_active','avg_rating', 'count_people',
        ]

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class CityDetailSerializer(serializers.ModelSerializer):
    city_property = PropertyDetailSerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['city_name','city_property']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


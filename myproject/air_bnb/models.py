from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                   MaxValueValidator(80)],
                                       null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    RoleChoices= (
    ('admin', 'admin'),
    ('guest', 'guest'),
    ('host', 'host'),
 )
    role = models.CharField(choices=RoleChoices,max_length=40, default='guest')
    avatar = models.ImageField(upload_to='user_avatar', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.role}'


class City(models.Model):
    city_name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f'{self.city_name}'

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.country_name}'


class Rules(models.Model):
    rules_name = models.CharField(max_length=150)
    rules_image = models.ImageField(upload_to='rules_image', null=True, blank=True)

    def __str__(self):
        return f'{self.rules_name}'




class Property(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price_per_night = models.DecimalField(decimal_places=2, max_digits=10)
    Property_Choices= (
         ('apartment', 'apartment'),
         ('house', 'house'),
         ('studio', 'studio'),
     )
    property_type = models.CharField(choices=Property_Choices,max_length=120)
    address = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='city_property')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='country_property')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='owner_property')
    max_guests = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    rules = models.ManyToManyField(Rules,related_name='rules_property')
    is_active = models.BooleanField(default=True)
    images = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_avg_rating(self):
        reviews = self.property_review.all()
        if reviews.exists():
            return round(sum([i.rating for i in reviews]) / reviews.count(),1)
        return 0

    def get_count_people(self):
        return self.property_review.count()


class PropertyImage(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_photos')
    property_image = models.ImageField(upload_to='property_image')


class Booking(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_bookings')
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in =models.DateField()
    check_out =models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    StatusChoices= (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
    ('cancelled', 'Cancelled'),
    )
    status = models.CharField(choices=StatusChoices,max_length=50,default='pending')

class Review(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_review')
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='guest_review')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.guest}'






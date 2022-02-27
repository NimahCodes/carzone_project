from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    state_choice = (
        ("AB", "Abia"),
        ("AD", "Adamawa"),
        ("AK", "Akwa"),
        ("AN", "Anambra"),
        ("BA", "Bauchi"),
        ("BA", "Bayelsa"),
        ("BE", "Benue"),
        ("BO", "Borno"),
        ("CR", "CrossRiver"),
        ("DE", "Delta"),
        ("EB", "Ebonyi"),
        ("ED", "Edo"),
        ("EK", "Ekiti"),
        ("EN", "Enugu"),
        ("GO", "Gombe"),
        ("IM", "Imo"),
        ("JI", "Jigawa"),
        ("KA", "Kaduna"),
        ("KA", "Kano"),
        ("KA", "Katsina"),
        ("KE", "Kebbi"),
        ("KO", "Kogi"),
        ("KW", "Kwara"),
        ("LA", "Lagos"),
        ("NA", "Nasarawa"),
        ("NI", "Niger"),
        ("OG", "Ogun"),
        ("ON", "Ondo"),
        ("OS", "Osun"),
        ("OY", "Oyo"),
        ("PL", "Plateau"),
        ("RI", "Rivers"),
        ("SO", "Sokoto"),
        ("TA", "Taraba"),
        ("YO", "Yobe"),
        ("ZA", "Zamfara"),
    )

    features_choices = (
        ("Cruise Control", "Cruise Control"),
        ("Audio Interface", "Audio Interface"),
        ("Airbags", "Airbags"),
        ("Air Conditioning", "Air Conditioning"),
        ("Seat Heating", "Seat Heating"),
        ("Alarm System", "Alarm System"),
        ("ParkAssist", "ParkAssist"),
        ("Power Steering", "Power Steering"),
        ("Reversing Camera", "Reversing Camera"),
        ("Direct Fuel Injection", "Direct Fuel Injection"),
        ("Auto Start/Stop", "Auto Start/Stop"),
        ("Wind Deflector", "Wind Deflector"),
        ("Bluetooth Handset", "Bluetooth Handset"),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

        door_choices = (
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("5", "5"),
        )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(
        ("year"),
        choices=year_choice,
    )
    condition = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    description = RichTextField()
    car_photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    car_photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(choices=features_choices, max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title

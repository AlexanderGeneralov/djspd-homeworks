from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    model = models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True)
    color = models.CharField(max_length=50, null=True)
    mileage = models.IntegerField(null=True)
    volume = models.IntegerField(null=True)
    body_type = models.CharField(max_length=50, choices=BODY_TYPE_CHOICES, default='sedan')
    drive_unit = models.CharField(max_length=50, choices=DRIVE_UNIT_CHOICES, default='rear')
    gearbox = models.CharField(max_length=50, choices=GEARBOX_CHOICES, default='manual')
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES, default='gasoline')
    price = models.IntegerField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return f'{self.model}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.created_at}, {self.client.name}"

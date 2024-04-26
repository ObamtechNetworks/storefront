from django.db import models

# Create your models here.

# MANY TO MANY RELATIONSHIP
# promotion
class Promotion(models.Model):
    """Defines a promotion model"""
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # products == if we use related name parameter in the associated many to many class, here: products
    # but we are sticking to convention, so this would be 'product_set'


# ONE TO MANY RELATIONSHIP
class Collection(models.Model):
    """Defines model for the collection class"""
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',
                                         on_delete=models.SET_NULL,
                                         null=True, related_name='+')

class Product(models.Model):
    """Defines the model for the products model"""
    # define fields
    # can be used as prkmary key: sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    # 9999.99
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,
                                on_delete=models.PROTECT)  # so as not delete all products in that collection
    # many to many relationship
    promotions = models.ManyToManyField(Promotion) # can have param: related_name='products)

# customer model
class Customer(models.Model):
    """Defines the model for the customer"""
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)  # B for bronze, S silver

# THE ORDER CLASS
class Order(models.Model):
    """Defines the order model"""
    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILED_STATUS = 'F'

    PAYMENT_STATUS = [
        (PENDING_STATUS, 'P'),
        (COMPLETE_STATUS, 'C'),
        (FAILED_STATUS, 'F')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,
                                      choices=PAYMENT_STATUS,
                                      default=PENDING_STATUS)
    # ONE TO MANY RELATIONSHIP
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    """Define model for items ordered"""
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


# ONE TO ONE RELATIONSHIP
class Address(models.Model):
    """Defines a address model with one to one relationship"""
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,
                                    on_delete=models.CASCADE,
                                    primary_key=True)  # primary key is to make each address unique to each customer
    # django automatically creates the reverse attribute : address in the Customer model with same fieldproperities

class Cart(models.Model):
    """Defines a cart model"""
    created_at = models.DateTimeField(auto_now_add=True)

# ONE TO MANY RELATIONSHIP
class CartItem(models.Model):
    """Defines an Item Model"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )
    slug = models.SlugField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["slug", "parent"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " > ".join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"slug": self.slug})


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=99.99)
    image = models.ImageField(upload_to="product_image/", null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(self)

    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={"slug": self.slug})


class ProductManager(models.Manager):
    def get_queryset(self):
        """Return queryset products only available"""

        return super(ProductManager, self).get_queryset().filter(available=True)


class ProductProxy(Product):
    class Meta:
        proxy = True

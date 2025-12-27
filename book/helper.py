from django.utils.text import slugify


def unique_slugify(instance, value, slug_field_name="slug"):
    base = slugify(value)[:200]
    slug = base
    Model = instance.__class__
    i = 1
    while Model.objects.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        i += 1
        slug = f"{base}-{i}"
    setattr(instance, slug_field_name, slug)

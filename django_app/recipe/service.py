from pytils.translit import slugify as ru_slugify

from recipe.models import Recipe


def generate_unique_slug(name, instance_pk=None):
    base_slug = ru_slugify(name) or "recipe"
    slug = base_slug
    counter = 1

    def slug_exists(s):
        qs = Recipe.objects.filter(slug=s)
        if instance_pk:
            qs = qs.exclude(pk=instance_pk)
        return qs.exists()

    while slug_exists(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
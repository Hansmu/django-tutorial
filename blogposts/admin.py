from django.contrib import admin
from .models import Post


admin.site.register(Post)  # Registers the model object on the admin page,
# can add/remove etc to the DB through the admin page.

from django.db import models

class ApiKey(models.Model):
    name = models.CharField(max_length=100)  # A name to identify the API (e.g., 'Google Geocoding')
    key = models.CharField(max_length=255)   # The actual API key
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    url = models.URLField()
    metadata = models.TextField(blank=True, null=True)  # Store as JSON or serialized text
    search = models.ForeignKey('SearchHistory', related_name='images', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

class SearchHistory(models.Model):
    query = models.CharField(max_length=255)  # The search query (address or coordinates)
    search_type = models.CharField(max_length=50)  # 'address' or 'coordinates'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.search_type}: {self.query}"


from django.db import models


class Project(models.Model):
	"""A project showcased in the portfolio.

	Fields:
		name: short project title
		description: longer text about the project
		github_url: optional link to source repository
		live_url: optional link to deployed site/demo
		tags: small JSON list or comma string of tags/technologies
		created_at: timestamp when the entry was created
	"""

	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	github_url = models.URLField(blank=True)
	live_url = models.URLField(blank=True)
	# Use a JSONField to store tags as a list. This is more structured and
	# avoids parsing comma-separated strings in application code. JSONField
	# is supported by Django's ORM and works with SQLite, Postgres, etc.
	# blank=True allows empty input in forms; default=list provides an empty
	# list for existing/new records.
	# Keeping tags as structured data makes filtering and querying easier
	# and is preferred in modern applications.
	tags = models.JSONField(blank=True, default=list)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:  # pragma: no cover - trivial
		return self.name


class Skill(models.Model):
	"""A skill or technology and proficiency level.

	level choices are the typical buckets used on resumes.
	"""

	LEVEL_BEGINNER = 'Beginner'
	LEVEL_INTERMEDIATE = 'Intermediate'
	LEVEL_ADVANCED = 'Advanced'
	LEVEL_EXPERT = 'Expert'

	LEVEL_CHOICES = [
		(LEVEL_BEGINNER, LEVEL_BEGINNER),
		(LEVEL_INTERMEDIATE, LEVEL_INTERMEDIATE),
		(LEVEL_ADVANCED, LEVEL_ADVANCED),
		(LEVEL_EXPERT, LEVEL_EXPERT),
	]

	name = models.CharField(max_length=150)
	level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

	def __str__(self) -> str:  # pragma: no cover - trivial
		return f"{self.name} ({self.level})"


class ContactMessage(models.Model):
	"""Simple contact message posted by visitors.

	This model is write-only in the API (we'll expose a create-only endpoint)
	to avoid showing messages in public APIs.
	"""

	name = models.CharField(max_length=200)
	email = models.EmailField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:  # pragma: no cover - trivial
		return f"Message from {self.name} <{self.email}>"

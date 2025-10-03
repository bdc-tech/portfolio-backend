
from django.contrib import admin
from . import models


"""Django admin customization for portfolio_api.

These admin classes expose list columns, filters, and search fields that are
useful during demos and day-to-day maintenance. Comments explain trade-offs
and why these choices are common in real teams.
"""


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
		"""Admin for Project model.

		- list_display surfaces the most important columns for quick scanning in the
			admin list view (id, name, tags, created_at).
		- list_filter enables simple time-based or tag-based filtering; here we
			add created_at as a date hierarchy and (optionally) a tag filter.
		- search_fields enables fast lookup by name, description, or tags.
		- readonly_fields prevents accidental changing of created timestamps.

		These choices mirror common production admin UIs where staff need to
		triage or edit content quickly without writing custom pages.
		"""

		list_display = ('id', 'name', 'tags', 'created_at')
		search_fields = ('name', 'description', 'tags')
		# Show a date hierarchy for quick drilling into recent/older projects
		date_hierarchy = 'created_at'
		readonly_fields = ('created_at',)


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
		"""Admin for Skill model.

		- list_display shows the skill and its level.
		- list_filter is useful when you want to see only Experts or Advanced
			levels quickly.
		- search_fields supports quick lookup by name.
		"""

		list_display = ('id', 'name', 'level')
		list_filter = ('level',)
		search_fields = ('name',)
		readonly_fields = ()


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
		"""Admin for ContactMessage.

		Messages are often considered write-only from the public perspective, but
		admins need to read and respond to them. Mark the timestamp as read-only
		to preserve auditability.
		"""

		list_display = ('id', 'name', 'email', 'created_at')
		search_fields = ('name', 'email', 'message')
		list_filter = ('created_at',)
		readonly_fields = ('created_at',)



from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model.

    - Accepts tags as either a JSON list or a comma-separated string.
    - Stores tags as a comma-separated string on the model to keep the DB
      storage simple.
    """

    tags = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text='Comma-separated list of tags or JSON list',
    )

    class Meta:
        model = models.Project
        fields = ['id', 'name', 'description', 'github_url', 'live_url', 'tags', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_tags(self, value):
        """Normalize tags into a comma-separated string.

        Accepts a JSON/list-like string such as "[\"django\", \"react\"]" or
        a simple comma-separated string and returns a normalized comma list.
        """

        # If the client sent a JSON-like list (e.g. from JS), try to parse it.
        if value.startswith('[') and value.endswith(']'):
            try:
                import json

                parsed = json.loads(value)
                if isinstance(parsed, list):
                    cleaned = [str(x).strip() for x in parsed if str(x).strip()]
                    return ','.join(cleaned)
            except Exception:
                raise serializers.ValidationError('Invalid JSON list for tags')

        # Otherwise treat it as comma-separated string
        parts = [p.strip() for p in value.split(',') if p.strip()]
        return ','.join(parts)


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for Skill model with level validation.

    We rely on the model's choices but include a clear error message here
    to make validation behaviour explicit during interviews.
    """

    class Meta:
        model = models.Skill
        fields = ['id', 'name', 'level']
        read_only_fields = ['id']

    def validate_level(self, value):
        allowed = [c[0] for c in models.Skill.LEVEL_CHOICES]
        if value not in allowed:
            raise serializers.ValidationError(f'Level must be one of: {allowed}')
        return value


class ContactMessageSerializer(serializers.ModelSerializer):
    """Serializer for ContactMessage.

    This serializer is used for create-only endpoints. We validate that the
    message is not empty and that the email looks correct (EmailField handles it).
    """

    class Meta:
        model = models.ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_message(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('Message cannot be empty')
        if len(value) > 2000:
            raise serializers.ValidationError('Message too long (max 2000 chars)')
        return value

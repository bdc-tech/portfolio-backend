"""API views for portfolio_api.

We expose CRUD for projects and skills via DRF ViewSets and a create-only
endpoint for contact messages (we typically don't expose messages via the API).
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from . import models, serializers


class ProjectViewSet(viewsets.ModelViewSet):
	"""Full CRUD API for Project.

	ModelViewSet gives list/retrieve/create/update/destroy actions that are
	commonly used in portfolio backends. Talking points:
	- Pagination and filtering could be added with DRF mixins
	- Permissions can be set per-action
	"""

	# Allow read-only access for anonymous users and full write access for
	# authenticated users. This is a common pattern for public portfolios where
	# anyone can view projects but only an authenticated admin/editor can modify them.
	permission_classes = [IsAuthenticatedOrReadOnly]

	queryset = models.Project.objects.all().order_by('-created_at')
	serializer_class = serializers.ProjectSerializer


class SkillViewSet(viewsets.ModelViewSet):
	"""Full CRUD API for Skill.

	The model uses explicit choice values for levels which keeps validation
	simple and explicit.
	"""

	queryset = models.Skill.objects.all().order_by('name')
	serializer_class = serializers.SkillSerializer


@api_view(['POST'])
def contact_create(request):
	"""Create-only endpoint for ContactMessage.

	We intentionally expose only POST to avoid listing messages publicly.
	Returns 201 on success with the created object (read-only fields included).
	"""

	serializer = serializers.ContactMessageSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	instance = serializer.save()
	return Response(serializers.ContactMessageSerializer(instance).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
	"""Protected endpoint returning the current user's email.

	This endpoint demonstrates token-protected routes; the frontend can
	call this to validate a token and obtain the current user's basic info.
	"""

	user = request.user
	return Response({'email': getattr(user, 'email', None)}, status=status.HTTP_200_OK)


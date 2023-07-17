from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zones.models import Zone, Distribution

@api_view(['PUT'])
def edit(request):
    zone_id = request.data.get('id')
    name = request.data.get('name')
    updated_at = request.data.get('updated_at')
    distributions = request.data.get('distributions')

    zone = Zone.objects.filter(pk=zone_id).first()
    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)

    zone.name = name
    zone.updated_at = updated_at
    zone.save()

    # Delete existing distributions for the zone
    Distribution.objects.filter(zone=zone).delete()

    # Create and save new distributions for the zone
    for distribution_data in distributions:
        percentage = distribution_data.get('percentage')
        Distribution.objects.create(zone=zone, percentage=percentage)

    return Response()

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Attendee
from events.models import Conference
from common.json import ModelEncoder
from django.forms.models import model_to_dict
import json


class AttendeeListEncoder(ModelEncoder):
    model = Attendee
    properties = ["email", "name", "company_name", "created"]


class AttendeeDetailEncoder(ModelEncoder):
    model = Attendee
    properties = [
        "email",
        "name",
        "company_name",
        "created",
        "conference",
    ]
    encoders = {
        "conference": AttendeeListEncoder,
    }


@require_http_methods(["GET", "POST"])
def api_list_attendees(request, conference_id):
    attendees = Attendee.objects.all()
    if request.method == "GET":
        return JsonResponse(
            {"attendees": list(attendees.values())},
            encoder=AttendeeListEncoder,
        )
    else:
        content = json.loads(request.body)
        # Get the Conference object and put it in the content dict
        try:
            conference = Conference.objects.get(attendees=conference_id)
            content["conference"] = conference
        except Conference.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid conference id"},
                status=400,
            )
        attendee = Attendee.objects.create(**content)
        return JsonResponse(
            model_to_dict(attendee),
            encoder=AttendeeDetailEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_attendee(request, id):
    if request.method == "GET":
        try:
            attendee = Attendee.objects.get(id=id)
            return JsonResponse(
                model_to_dict(attendee),
                encoder=AttendeeDetailEncoder,
                safe=False,
            )
        except Attendee.DoesNotExist:
            return JsonResponse(
                {"message": "Attendee not found"},
                status=404,
            )
    elif request.method == "DELETE":
        count, _ = Attendee.objects.filter(id=id).delete()
        if count > 0:
            return JsonResponse({"deleted": True}, status=200)
        else:
            return JsonResponse({"deleted": False}, status=200)
    else:
        content = json.loads(request.body)
        try:
            attendee = Attendee.objects.get(id=id)
        except Attendee.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid state Abbreviation"}, status=400
            )

        Attendee.objects.filter(id=id).update(**content)

        location = Location.objects.get(id=id)
        return JsonResponse(
            attendee,
            encoder=AttendeeDetailEncoder,
            safe=False,
        )

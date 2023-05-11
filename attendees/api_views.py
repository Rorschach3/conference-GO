from django.http import JsonResponse

from .models import Attendee


def api_list_attendees(request, conference_id):
    attendees = Attendee.objects.filter(conference=conference_id)
    return JsonResponse(
        {"attendees": attendees},
        encoder=AttendeeListEncoder,
    )


def api_show_attendee(request, id):
    """
    Returns the details for the Attendee model specified
    by the id parameter.

    This should return a dictionary with email, name,
    company name, created, and conference properties for
    the specified Attendee instance.

    {
        "email": the attendee's email,
        "name": the attendee's name,
        "company_name": the attendee's company's name,
        "created": the date/time when the record was created,
        "conference": {
            "name": the name of the conference,
            "href": the URL to the conference,
        }
    }
    """
    attendee = Attendee.objects.get(id=id)
    return JsonResponse(
        {
            "email": attendee.email,
            "name": attendee.name,
            "company_name": attendee.company_name,
            "created": attendee.created,
            "conference": {
                "name": attendee.conference.name,
                "href": attendee.conference.get_api_url(),
            },
        }
    )

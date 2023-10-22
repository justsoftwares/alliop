from django.db.models import Q


def get_queryset_for_user(model, user_id, show_user_fields, edit_user_fields, only_user_objects):
    query = Q()
    if only_user_objects and (show_user_fields or edit_user_fields):
        for field in edit_user_fields + show_user_fields:
            query |= Q(**{field: user_id})

    return model.objects.filter(query)

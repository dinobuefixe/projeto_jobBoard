from .status_rules import VALID_TRANSITIONS

def update_status(application, new_status):
    if new_status not in VALID_TRANSITIONS.get(application.status, []):
        raise ValueError(f"Cannot move from {application.status} to {new_status}")
    application.status = new_status
    application.save()
    return application
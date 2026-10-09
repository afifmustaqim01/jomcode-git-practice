role = "organizer"
owner_id = "u1"
current_user_id = "u2"
if role == "organizer" and owner_id == current_user_id:
    print("Can edit")
else:
    print("Forbidden")

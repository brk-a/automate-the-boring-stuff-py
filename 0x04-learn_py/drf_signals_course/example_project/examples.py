from django.contrib.auth import get_user_model

User = get_user_model()

#pre_save signal sends instance
instance = User.objects.create() #save user to db
#post_save signal sends instance and flag `created`

#pre_save signal sends instance
instance = save() #re-save user to db (example: update user data)
#post_save signal sends instance and flag `created`
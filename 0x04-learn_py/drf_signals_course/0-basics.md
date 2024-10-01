# basics of django signals
* django implementation of event handlers and/or callbacks
* [more info][def]
### examples
##### save a user to DB
* say we have a django app that creates users among other things
* the `pre_save` and `post_save` signals are sent right before and right after the user is created

    ```python
        from django.contrib.auth import get_user_model

        User = get_user_model()

        #pre_save signal sends instance to a handler function called a receiver
        instance = User.objects.create() #save user to db
        #post_save signal sends instance and flag `created=True` to a handler function called a receiver
    ```

* say, for one reason or another, the instance is saved again; the signals will be sent as well, however, `created` will be `False`

    ```python
        from django.contrib.auth import get_user_model

        User = get_user_model()

        #pre_save signal sends instance to a handler function called a receiver
        instance = User.objects.create() #save user to db
        #post_save signal sends instance and flag `created=True` to a handler function called a receiver

        #pre_save signal sends instance to a handler function called a receiver
        instance.save()
        #post_save signal sends instance and flag `created=False` to a handler function called a receiver
    ```

* you may have as many receivers as your app requires
* `instance.delete()` triggers the `pre_delete` and `post_delete` signals
### connect to a signal
* two methods
    - pass the relevant parameters: `receiver`, `sender` etc to `signal` and call it
    - pass the relevant parameters:`signal`, `sender` etc to the `receiver` decorator
* *for dummies*
    - method 1: **call the `signal`**; **pass the `receiver` and `sender` to it**
    - method 2: **decorate the `receiver`**; **pass the `signal` and `sender` to it**

[def]: https://docs.djangoproject.com/en/5.1/topics/signals/
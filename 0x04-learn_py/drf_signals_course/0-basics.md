# basics of django signals
* django implementation of event receivers and/or callbacks
* [more info][def]
### 1. `post_save`
* say we have a django app that creates users among other things
* the `pre_save` and `post_save` signals are sent right before and right after the user is created

    ```python
        from django.contrib.auth import get_user_model

        User = get_user_model()

        #pre_save signal sends instance to a receiver function called a receiver
        instance = User.objects.create() #save user to db
        #post_save signal sends instance and flag `created=True` to a receiver function called a receiver
    ```

* say, for one reason or another, the instance is saved again; the signals will be sent as well, however, `created` will be `False`

    ```python
        from django.contrib.auth import get_user_model

        User = get_user_model()

        #pre_save signal sends instance to a receiver function called a receiver
        instance = User.objects.create() #save user to db
        #post_save signal sends instance and flag `created=True` to a receiver function called a receiver

        #pre_save signal sends instance to a receiver function called a receiver
        instance.save()
        #post_save signal sends instance and flag `created=False` to a receiver function called a receiver
    ```

* you may have as many receivers as your app requires
* `instance.delete()` triggers the `pre_delete` and `post_delete` signals
#### connect to a signal
* two methods
    - pass the relevant parameters: `receiver`, `sender` etc to `signal` and call it
    - pass the relevant parameters:`signal`, `sender` etc to the `receiver` decorator
* *for dummies*
    - method 1: **call the `signal`**; **pass the `receiver` and `sender` to it**
    - method 2: **decorate the `receiver`**; **pass the `signal` and `sender` to the decorator**
#### how it may appear in a code-base
* you are more likely to encounter the decorator method in more modern apps
* the receiver function will most likely have the following signature

    ```python
        @receiver(signal_name, sender=SenderClass)
        def receiver_function_name(sender, instance, created, *args, **kwargs):
            if created:
                # TODO: do something when `created` is `True`
            else:
                # TODO: do something when `created` is `False`
            
            # TODO: whatever else should happen here
    ```

* example: save user to DB

    ```python
        from django.contrib.auth import get_user_model

        User = get_user_model()

        @receiver(post_save, sender=User)
        def user_post_save_receiver(sender, instance, created, *args, **kwargs):
            if created:
                print(f"Send email to {user.username} succeeded")
            else:
                print(f"Send email to {user.username} failed")
            
            print(f"args: {args}, kwargs: {kwargs}")
    ```

    - where TF does `user.username` come from? why is it not `instance.username`? where did we use `instance`?
    - glad you asked...
    - yes, `user` is not defined anywhere or is it? think about it: what, really, is `instance`
    - `instance` is , well, an *instance* of the class `User`; the `User` class assigned to `sender` in the decorator
    - in other words, `user` is `instance` which itself is an instance of of the class `User`
    - we can replace `user` with `instance` in the code above; everything will work as expected viz:

    ```python
        from django.contrib.auth import get_user_model

        User = get_user_model()

        @receiver(post_save, sender=User)
        def user_post_save_receiver(sender, instance, created, *args, **kwargs):
            if created:
                print(f"Send email to {instance.username} succeeded")
            else:
                print(f"Send email to {instance.username} failed")
    ```

### 2. `pre_save`
* works more or less like `post_save`, however, it does not have the `created` argument and attributes of `instance` may be `None` because `instance` may have not been created (saved to DB)
    - new user has not been saved to DB, therefore, `instance.id` attribute etc will be `None`
    - existing user is already in DB, therefore, `instance.id` attribute will not be `None`
* expect the following signature

    ```python
        @receiver(pre_save, sender=SenderClass)
        def receiver_function_name(sender, instance, *args, **kwargs):
            # TODO: whatever should happen here
    ```

* example: do something before saving saving a user to DB

    ```python
        @receiver(pre_save, sender=User)
        def user_pre_save_receiver(sender, instance, *args,  **kwargs):
            print(f"args: {args}, kwargs: {kwargs}, instance: {instance}, sender: {sender}")
    ```

#### instance.save()
* what happens when `instance.save()` is called?
    - `instance.save()` triggers the `pre_save` signal, saves (successfully or otherwise) then triggers the `post_save` signal
* what do you think will happen when `instance.save()` is called in a `pre_save` receiver function?
    - `RecursionError: maximum recursion depth exceeded while calling a Python object`
    - recall that you are in a `pre_save` receiver function and `instance.save()` triggers a `pre_save` signal: this is a scenario where a `pre_save` signal triggers a `pre_save` signal *ad infinitum*
    - long story short: do not call `instance.save()` in this case
    <img src="./recursion-infinite.jpeg" alt="recursion-infinite"/>
* you can handle `instance.save()` in the `post_save` receiver this way: call it whaen `created` is `True`. the save operation will be done twice, however, this should not be a significant performance issue

     ```python
        @receiver(post_save, sender=User)
        def user_post_save_receiver(sender, instance, created, *args, **kwargs):
            if created:
                print(f"Send email to {instance.username} succeeded")
                instance.save()
            else:
                print(f"Send email to {instance.username} failed")
    ```
### 3. `m2m_changed`
* `m2m_changed` does not fire when you change something connected via an m2m field: it fires when you add or remove a m2m relation
* strictly speaking, this is not a model signal since it is sent by the `ManyToManyField`, however, since it complements the `pre_save`/`post_save` and `pre_delete`/`post_delete` when it comes to tracking changes to models, it is included here
* signature

    ```python
        @receiver(m2m_changed, sender=SenderClass.ManyToManyFieldName.through)
        def  receiver_function_name(sender, instance, action, *args, **kwargs):
            # TODO: whatever should happen here
    ```

* example: do something when a blog post is liked

    ```python
            @receiver(m2m_changed, sender=BlogPost.liked.through)
            def blog_post_m2m_liked_changed_receiver(sender, instance, action, *args, **kwargs):
                # print(f"args: {args}, kwargs: {kwargs}")
                # print(f"action: {action}")
                if action == "pre_add":
                    print(f"user {instance.pk} added to liked blog post {instance.id}")
                    qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk__set"))
                    print(f"liked blog posts: {qs.count()}")
                elif action == "post_add":
                    print(f"user {instance.pk} liked blog post {instance.id}")
                elif action == "post_remove":
                    print(f"user {instance.pk} unliked blog post {instance.id}")
                elif action == "post_clear":
                    print(f"user {instance.pk} unliked all blog posts")
    ```

* WTF is that naming convention of the value to `sender`?
    - glad you asked; see **sender below**
    - `ManyToManyField` is two-way traffic: changes may occur on either end and will affect the other
    - also, there may be more than one `ManyToManyField`s in a model/schema
    - use the convention to be explicit and clear
    - the `through` attribute on the many-to-many field allows you to access said `ManyToManyField`
#### sender
* the intermediate model class describing the `ManyToManyField`
    - automatically created when a many-to-many field is defined; you can access it using the through attribute on the many-to-many field
#### instance
* the instance whose many-to-many relation is updated
    - can be an instance of the sender or of the class the `ManyToManyField` is related to
#### action
* a string indicating the type of update that is done on the relation
* can be one of the following:
    - `"pre_add"` &rarr; sent before one or more objects are added to the relation
    - `"post_add"` &rarr; sent after one or more objects are added to the relation
    - `"pre_remove"` &rarr; sent before one or more objects are removed from the relation
    - `"post_remove"` &rarr; sent after one or more objects are removed from the relation
    - `"pre_clear"` &rarr; sent before the relation is cleared
    - `"post_clear"` &rarr; sent after the relation is cleared
#### reverse
* indicates which side of the relation is updated (i.e., if it is the forward or reverse relation that is being modified)
#### model
* the class of the objects that are added to, removed from or cleared from the relation
#### pk_set
* for the `pre_add` and `post_add` actions, this is a set of primary key values that will be, or have been, added to the relation
    - may be a subset of the values submitted to be added since inserts must filter existing values in order to avoid a database `IntegrityError`
* for the `pre_remove` and `post_remove` actions, this is a set of primary key values that was submitted to be removed from the relation
    - not dependent on whether the values actually will be, or have been, removed
    - non-existent values may be submitted, and will appear in `pk_set`, even though they have no effect on the database
* for the `pre_clear` and `post_clear` actions, this is `None`




[def]: https://docs.djangoproject.com/en/5.1/topics/signals/
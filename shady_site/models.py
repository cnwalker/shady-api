# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assignments(models.Model):
    idea_id = models.IntegerField(blank=True, null=True)
    writer_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    issue_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignments'


class Attachments(models.Model):
    description = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    attachable_id = models.IntegerField(blank=True, null=True)
    attachable_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attachments'

class Editors(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField(blank=True, null=True)
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    last_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    approved = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'editors'


class EditorsRoles(models.Model):
    editor_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editors_roles'


class HelloGreeting(models.Model):
    when = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hello_greeting'


class Ideas(models.Model):
    headline = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    issue_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ideas'


class Images(models.Model):
    description = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    imageable_id = models.IntegerField(blank=True, null=True)
    imageable_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    writer_id = models.IntegerField(blank=True, null=True)
    credit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class Issues(models.Model):
    volume = models.IntegerField(blank=True, null=True)
    issue = models.IntegerField(blank=True, null=True)
    printing_deadline = models.DateTimeField(blank=True, null=True)
    distribution = models.DateTimeField(blank=True, null=True)
    published = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=255, blank=True, null=True)
    published_issue = models.CharField(max_length=255, blank=True, null=True)
    submission_deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class Roles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    resource_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'

class Sessions(models.Model):
    session_id = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Submissions(models.Model):
    headline = models.CharField(max_length=255, blank=True, null=True)
    byline = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    writer_id = models.IntegerField(blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    issue_id = models.IntegerField(blank=True, null=True)
    assignment_id = models.IntegerField(blank=True, null=True)
    copyedited = models.NullBooleanField()
    edited = models.NullBooleanField()
    published = models.NullBooleanField()
    clean_body = models.TextField(blank=True, null=True)
    approved = models.NullBooleanField()
    notes = models.TextField(blank=True, null=True)
    websclusive = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'submissions'


class Versions(models.Model):
    item_type = models.CharField(max_length=255)
    item_id = models.IntegerField()
    event = models.CharField(max_length=255)
    whodunnit = models.CharField(max_length=255, blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versions'


class Writers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'writers'

#!/usr/bin/env python


__author__ = 'ElvisNam'


'''
Models for user, blog, comment.
'''


import time, uuid

from transwarp.db import next_id
from tramswarp.orm import Model. StringField, BooleanField, FloatField, TextField


class User(Model):

	__table__ = 'users'

	id = StringField(primary_key=True, default=next, ddl='varchar(50)')
	email = StringField(update=False, ddl='varchar(50)')
	password = StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varchar(50)')
	image = StirngField(ddl='varchar(500)')
	created_at = FloatField(updatable=False, default=time.time)


class Blog(Model):

	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	user_id = StringField(updatable=False, ddl='varchar(50)')
	user_name = StringField(ddl='vrchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(500)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	created_at = FloatField(updatable=False, default=time.time)


class Comment(Model):
    
    __table__ = 'comment'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(updatable=False, ddl='varchar(50)')
    user_id = StringField(updatable=False, ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(updatable=False, default=time.time)  
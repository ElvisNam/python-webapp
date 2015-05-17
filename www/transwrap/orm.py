#!/user/bin/env python

__author__ = ElvisNam

'''
Database operation module.This module is independent with web module.
'''

import time 
import logging
import db


class Model(dirt):

	__metaclass__ = ModelMetaclass

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getatter__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dirt' object has no attribute '%s'" % key)

	def __setatter__(self, key, value):
		self[key] = value


class ModelMetaclass(type):

	def __new__(cls, name, bases, attrs):
		mapping = ...
		primary_key = ...
		__table = cls.__table 
		attrs['__mapping__'] = mapping
		attrs['__primary_key__'] = __primary_key__
		attrs['__table__'] = __table__
		return type.__new__(cls, name, bases, attrs)



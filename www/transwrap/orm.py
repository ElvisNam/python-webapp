#!/user/bin/env python

__author__ = ElvisNam

'''
Database operation module.This module is independent with web module.
'''

import time 
import logging
import db


class Field(object):

	_count = 0

	def __init__(self, **kw):
		self.name = kw.get('name', None)
		self._default = kw.get('default', None)
		self.primary_key = kw.get('primary_key', False)
		self.nullable = kw.get('nullable', False)
		self.updatable = kw.get('updatable', True)
		self.insertable = kw.get('insertable', True)
		self.ddl = kw.get('ddl', '')
		self._order = Field._count
		Field._count = Field._count + 1

    @property
    def default(self):
    	d = self._default
    	return d() if callable(d) else d

    def __str__(self):
    	s = ['<%s:%s,%s,default(%s),' % (self.__class__.__name__, self.name,\
    		self.ddl, self._default)]
    	self.nullable and s.append('N')
    	self.updatable and s.append('U')
    	self.insertable and s.append('I')
    	s.append('>')
    	return ''.join(s)





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



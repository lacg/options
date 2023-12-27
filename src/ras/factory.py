from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):
	"""
	The Factory class declares the create method that is supposed to return an
	concrete object class. The Factory's subclasses usually provide the
	implementation of this method.
	"""

	@classmethod
	@abstractmethod
	def create(cls, type: str):
		"""
		Note that the Factory may also provide some default implementation of
		the create method.
		"""
		pass
# Auto import celery app when launched

from .celery import app as celery_app

__all__ = ('celery_app',)
import time

from rest_framework import serializers


class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None
        except ValueError:
            return super(UnixEpochDateField, self).to_representation(value)

    def to_internal_value(self, value):
        import datetime
        try:
            internal_value = datetime.datetime.fromtimestamp(int(value))
        except ValueError:
            return super(UnixEpochDateField, self).to_internal_value(value)
        else:
            return internal_value

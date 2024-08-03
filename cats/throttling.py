from rest_framework import throttling

import datetime


class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        return not (3 <= now < 5)

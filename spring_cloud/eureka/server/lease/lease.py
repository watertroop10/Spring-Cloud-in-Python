# -*- coding: utf-8 -*-

__author__ = "Daniel1147 (sxn91401@gmail.com)"
__license__ = "Apache 2.0"

# standard library
import enum

# scip plugin
from spring_cloud.commons.utils.timestamp import current_timestamp


class Lease:
    class Action(enum.Enum):
        REGISTER = "register"
        CANCEL = "cancel"
        RENEW = "renew"

    def __init__(self, holder, duration_in_secs: int):
        self.duration = duration_in_secs * 1000
        self.__holder = holder
        self.__registration_timestamp = current_timestamp()

    @property
    def holder(self):
        return self.__holder

    @property
    def eviction_timestamp(self):
        return self.__eviction_timestamp

    @property
    def registration_timestamp(self):
        return self.__registration_timestamp

    @property
    def last_update_timestamp(self):
        return self.__last_update_timestamp

    @property
    def service_up_timestamp(self):
        return self.__service_up_timestamp

    @service_up_timestamp.setter
    def service_up_timestamp(self, value):
        self.__service_up_timestamp = value

    def is_expired(self):
        return False

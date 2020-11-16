# -*- coding: utf-8 -*-
# standard library
import re
from datetime import datetime

__author__ = "Chaoyuuu (chaoyu2330@gmail.com)"
__license__ = "Apache 2.0"

# scip plugin
from spring_cloud.gateway.handler.predicate.base import RoutePredicateFactory
from spring_cloud.gateway.handler.predicate.predicate import Predicate


class AfterRoutePredicateFactory(RoutePredicateFactory):
    def apply(self, config) -> Predicate:
        return AfterRoutePredicate(config)


class PathRoutePredicateFactory(RoutePredicateFactory):
    def apply(self, config) -> Predicate:
        return PathRoutePredicate(config)


class CookieRoutePredicateFactory(RoutePredicateFactory):
    def apply(self, config) -> Predicate:
        return CookieRoutePredicate(config)


class AfterRoutePredicate(Predicate):
    def __init__(self, config, now_datetime_func=None):
        self.now_datetime_func = now_datetime_func
        self.config = config

    def test(self, obj) -> bool:
        now = self.now_datetime_func() if self.now_datetime_func else datetime.now()
        return now > self.config.date_time

    class Config:
        def __init__(self):
            self.__date_time = None

        @property
        def date_time(self) -> datetime:
            return self.__date_time

        def set_date_time(self, date_time):
            self.__date_time = date_time


class PathRoutePredicate(Predicate):
    def __init__(self, config):
        self.config = config

    def test(self, obj) -> bool:
        path_patterns = obj
        return self.config.pattern in path_patterns

    class Config:
        def __init__(self):
            self.__pattern = None

        @property
        def pattern(self) -> str:
            return self.__pattern

        def set_pattern(self, pattern):
            self.__pattern = pattern


class CookieRoutePredicate(Predicate):
    def __init__(self, config):
        self.config = config

    def test(self, obj) -> bool:
        request_http_cookies = obj
        if request_http_cookies is None:
            return False
        for cookie in request_http_cookies.values():
            if re.match(cookie, self.config.cookie_value):
                return True
        return False

    class Config:
        def __init__(self):
            self.__cookie_name = None
            self.__cookie_value = None

        @property
        def cookie_name(self) -> str:
            return self.__cookie_name

        @property
        def cookie_value(self) -> str:
            return self.__cookie_value

        def set_cookie_name(self, cookie_name: str):
            self.__cookie_name = cookie_name

        def set_cookie_value(self, cookie_value: str):
            self.__cookie_value = cookie_value

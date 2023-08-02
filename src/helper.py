""" Module containing helper methods """

import sys
import time
import traceback
from datetime import datetime
from decimal import Decimal
import requests


def apply_format(value):
    """Method for applying formats"""
    return format(Decimal(value), ".5f")


def apply_format_level(value):
    """Method for applying format levels"""
    return format(Decimal(value), ".2f")


def get_datetime():
    """Method for generating datetime valsuies"""
    return datetime.now().strftime("%Y-%m-%d %h:%m:%s")


def get_timestamp():
    """Method for calculating timestamps"""
    return time.mktime(time.gmtime())


def get_response(url, resourceid, params=None):
    """Method for executing API requests"""
    guard(resourceid, url)
    url = url % resourceid
    if params:
        url = "%s%s" % (url, params)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as exc:
        print("404 Exception during request %s : %s " % (url, exc))
        print("-" * 60)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)
        return None

    except requests.exceptions.RequestException as exc:
        print("Exception during request %s : %s " % (url, exc))
        print("-" * 60)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)
        return None


def guard(resourceid, url):
    """Method for checking parameters supplied"""
    if url is None:
        raise ValueError("URL should have a value supplied")
    if resourceid is None:
        raise ValueError("URL %s should have a resource id value supplied" % url)

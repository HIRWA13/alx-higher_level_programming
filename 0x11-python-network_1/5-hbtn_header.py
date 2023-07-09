#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 9th july 2023
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))

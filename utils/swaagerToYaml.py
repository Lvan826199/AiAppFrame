# -*- coding: utf-8 -*-
"""
@Time : 2025/4/29 14:07
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : swaagerToYaml.py
"""
__author__ = "梦无矶小仔"
from pytest_yaml_yoyo.swagger_parser import SwaggerToYaml
# 作者 上海-悠悠 微信:283340479

# s = SwaggerToYaml('./swagger.json')
# s.parse_json()
s = SwaggerToYaml('http://127.0.0.1:9099/openapi.json')
s.parse_json()
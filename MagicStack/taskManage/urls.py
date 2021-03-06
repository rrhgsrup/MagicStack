#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 MagicStack
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from django.conf.urls import patterns, url
from taskManage.views import *


urlpatterns = patterns("",
    url("^list/$", task_list, name="task_list"),
    url("^adv_task_list/$", adv_task_list, name="adv_task_list"),
    url("^add/$", task_add, name="task_add"),
    url("^adv_task_add/$", adv_task_add, name="adv_task_add"),
    url("^edit/$", task_edit, name="task_edit"),
    url("^adv_task_edit/$", adv_task_edit, name="adv_task_edit"),
    url("^del/$", task_del, name="task_del"),
    url("^action/$", task_action, name="task_action"),
    url("^groups/$", task_group, name="get_task_group"),
    url("^modules/$", task_modules, name="get_task_module"),
    url("^module/$", task_module, name="get_module_comment"),
    url("^exec_info/$", task_exec_info, name="task_exec_info"),
    url("^exec_replay/$", task_exec_replay, name="task_exec_replay"),
    url("^get_html_code/$", get_html_code, name="get_html_code"),
)

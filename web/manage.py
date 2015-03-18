#!/usr/bin/env python
#encoding=utf8
import os
#import sys

#设置系统默认编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_platform.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

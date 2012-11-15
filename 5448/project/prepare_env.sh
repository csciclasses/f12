#!/bin/bash -x

###
# use source ./SCRIPT_NAME
###

GAE_PATH=/opt/google_appengine/
#GAE_DJANGO_PATH=$GAE_PATH/lib/django_1_3

#GAE_DJANGO_ADMIN=$GAE_DJANGO_PATH/django/bin

export PATH=$GAE_PATH:$PATH
#export PYTHONPATH=$GAE_PATH:$GAE_PATH/lib/django_1_3:$PYTHONPATH

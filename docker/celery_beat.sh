#!/bin/bash

sleep 15

celery -A lms_drf beat -l INFO -S django
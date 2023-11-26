#!/bin/bash

sleep 15

celery -A lms_drf.celery worker -l INFO -S django
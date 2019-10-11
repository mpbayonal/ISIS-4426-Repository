#!/bin/bash
celery worker -A back -l info &
celery beat -A back -l info &
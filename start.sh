#!/bin/bash

# Применяем миграции базы данных
echo "Applying database migrations..."
alembic upgrade head

# Запускаем бота
echo "Starting bot..."
python botmain.py 
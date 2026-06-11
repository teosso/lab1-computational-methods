# Модель: Метод простої ітерації (5 семестр)
# Автор: Ковальжі Сергій, група АІ-235

FROM python:3.10-slim
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]
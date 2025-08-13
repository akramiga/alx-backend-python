# Use Python 3.10 as base
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project code
COPY . .

# Expose port 8000 (default Django)
EXPOSE 8000

# Run Django development server (adjust for production later)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


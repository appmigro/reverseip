FROM python:3-alpine

WORKDIR /reverseip

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /reverseip/

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /reverseip

# Expose the application port
EXPOSE 8000

# Set the entrypoint and default command to run the server
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


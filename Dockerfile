# Dockerfile
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run on container start
# prod
CMD ["python", "main.py"]
# debug
# CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "main.py"]

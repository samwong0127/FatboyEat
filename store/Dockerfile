# Use an official Python runtime as a parent image
FROM python:slim
# Copy the current directory contents into the container at /store
COPY . /store
# Set the working directory to /store
WORKDIR /store
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Run store.py when the container launches
CMD ["python3", "store.py"]
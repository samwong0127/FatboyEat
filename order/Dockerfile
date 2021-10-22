# Use an official Python runtime as a parent image
FROM python:slim
# Copy the current directory contents into the container at /order
COPY . /order
# Set the working directory to /order
WORKDIR /order
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Run order.py when the container launches
CMD ["python3", "order.py"]
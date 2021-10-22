# Use an official Python runtime as a parent image
FROM python:slim
# Copy the current directory contents into the container at /order
COPY . /order

# Set the working directory to /order
WORKDIR /order
ENV FLASK_APP=order.py
ENV FLASK_RUN_HOST=0.0.0.0 
# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 15001
COPY order.py .
# Run order.py when the container launches
CMD ["python3", "order.py"]
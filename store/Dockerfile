# Use an official Python runtime as a parent image
FROM python:slim
# Copy the current directory contents into the container at /store
COPY . /store

# Set the working directory to /store
WORKDIR /store
ENV FLASK_APP=store.py
ENV FLASK_RUN_HOST=0.0.0.0 
# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 15002
COPY store.py .
# Run store.py when the container launches
CMD ["python3", "store.py"]
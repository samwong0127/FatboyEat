# Use an official Python runtime as a parent image
FROM python:slim
# Copy the current directory contents into the container at /menu
COPY . /menu

# Set the working directory to /menu
WORKDIR /menu
ENV FLASK_APP=menu.py
ENV FLASK_RUN_HOST=0.0.0.0 
# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 15000
COPY menu.py .
# Run menu.py when the container launches
CMD ["python3", "menu.py"]
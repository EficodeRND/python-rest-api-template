FROM python:3.9

# Install the function's dependencies using file requirements.txt
# from your project folder.
WORKDIR /api
COPY requirements.txt .
RUN  pip3 install --upgrade pip
RUN  pip3 install -r requirements.txt

# Copy function code
COPY tasks.py .
COPY prod_tasks.py .
COPY app/ ./app

# Clean up the Python compilation cache
RUN find ./ -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

CMD invoke -c prod_tasks prodserver -p $PORT

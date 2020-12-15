FROM python:3.7-slim

RUN pip install --upgrade pip
# as far as i know there is no way to install with requirements
RUN pip install torch==1.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD ./degenerator /degenerator
ADD ./models /models
WORKDIR /
EXPOSE 8000

CMD uvicorn degenerator.main:app --reload --host 0.0.0.0

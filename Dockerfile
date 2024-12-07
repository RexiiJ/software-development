FROM python:alpine
ADD . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
     CMD curl -f http://localhost:5001/health || exit 1
ENTRYPOINT [ "python",".app.py" ]
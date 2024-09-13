## Instructions to build and run Docker image on local machine

```
docker build -t hackpackteam06 .
```

```
docker run -d --name hackpack-container -p 8000:8000 hackpackteam06
```

## Accessing the HTML Document
Once your Docker container is running, navigate to http://localhost:8000/index.html in your browser. This URL serves the index.html file, which makes API calls to the FastAPI backend running on the same port (8000) in the Docker container.

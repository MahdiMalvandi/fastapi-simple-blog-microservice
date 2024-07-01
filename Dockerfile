FROM ubuntu:latest
LABEL authors="User1"

ENTRYPOINT ["top", "-b"]
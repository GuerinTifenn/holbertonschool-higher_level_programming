# Use the same Alpine base image as the previous exercise
FROM alpine:latest

# Install curl package
RUN apk update && apk add --no-cache curl
# Copy the configuration file to /app/config.txt
COPY config.txt /app/config.txt

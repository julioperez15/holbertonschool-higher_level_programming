# Use alpine image
FROM alpine:latest

#intalar curl
RUN apk add --no-cache curl

#copiar el archivo config.txt en el container
COPY config.txt /app/config.txt

# Specify the default command to run when the container starts
CMD ["sh"]
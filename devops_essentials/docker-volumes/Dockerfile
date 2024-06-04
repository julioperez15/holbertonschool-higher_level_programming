# Usa una imagen base, por ejemplo, una imagen de Ubuntu
FROM ubuntu:latest

# Instala cualquier dependencia necesaria
RUN apt-get update && apt-get install -y \
	nano \
	&& rm -rf /var/lib/apt/lists/*

# Crea un volumen en /data
VOLUME /data

# Establece el punto de entrada del contenedor
CMD ["bash"]

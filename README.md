# iot-dockerizer

A tiny project to automate bundling an IoT target as a Docker image.

How to use:

```sh
mkdir output
docker run -v `pwd`/iot_image.zip:/input -v `pwd`/output:/output ethan42/iot-dockerizer:1
cd output
docker build -t iotimage .
```
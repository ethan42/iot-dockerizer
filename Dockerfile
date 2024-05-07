FROM ubuntu:24.04 as extractor

RUN apt update

RUN DEBIAN_FRONTEND=noninteractive apt install -fy git binwalk unzip build-essential liblzma-dev liblzo2-dev zlib1g-dev wget

RUN git clone https://github.com/ethan42/sasquatch.git && cd sasquatch && ./build.sh

COPY extract.py /usr/bin/extract

CMD ["extract"]

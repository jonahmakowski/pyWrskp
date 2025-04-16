FROM ubuntu:latest

RUN apt install wget git python3 python3-venv libgl1 libglib2.0-0

RUN wget -q https://raw.githubusercontent.com/openvinotoolkit/stable-diffusion-webui/refs/heads/master/webui.sh

CMD ["bash", "webui.sh"]

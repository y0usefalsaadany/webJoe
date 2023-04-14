# webJoe
This is a framework for web penetration testers and web developers

# installation 

<h1>installation using docker</h1>

```
docker build --tag webjoe-docker .
docker run -it --name=webjoe-container  webjoe-docker
docker start webjoe-container
docker exec -it webjoe-container /bin/sh
docker cp webjoe-container:/app/dy.txt .
```
to work without any problem you should install
```
sudo apt update
sudo apt upgrade
sudo apt upgrade
sudo apt install git python3
sudo apt install python3-pip
git clone https://github.com/y0usefalsaadany/webJoe.git
cd webJoe
```

# setup

```
pip3 install -r requirements.txt
```

# running
```
python3 run.py
```

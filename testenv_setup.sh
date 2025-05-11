apk update
apk add python3 
apk add py3-pip
apk add git

git clone https://github.com/merwin-asm/pysws.git
cd pysws
cd dev_env
python3 env_setup.py # installs pip and other reqs and enables the testrun.sh operations

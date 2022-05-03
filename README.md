# Github Search Application

## Author

[Abdi-Ali](https://github.com/Abdi-Ali33)

# Description

A web application where users can view the latest news from different sources.

## Screenshot

### Prerequisites

- An internet connection is important
- You need to have git installed You can install it with the following command in your terminal $ sudo apt install git-all

## Setup Installation/Requirements

# Setup / Installation

- clone the repo:

```shell
git clone `https://github.com/Abdi-Ali33/News-Highlight.git`
```

```shell
cd news-hub
```

- create virtual environment

```shell
python3.8 -m venv --without-pip venv
```

- To activate the virtual environment

```shell
 venv/scripts/activate
```

- install the packages from requirements.txt

```shell
pip3 freeze >  requirements.txt
```

- setup environment variables

```shell
cp .env.example .env
```

- Execute the shell script and start the server

```shell
chmod a+x start.sh
./start.sh
```

- open the browser and navigate to http://127.0.0.1:5000/ to see the application in action

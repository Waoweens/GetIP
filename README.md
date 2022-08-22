# GetIP
## Setup
> Note: These instructions are for Linux and macOS.

Create virtual environment:

```sh
python3 -m venv venv
```

Activate virtual environment:

> fish and csh users: use activate.fish and activate.csh respectively

```sh
source venv/bin/activate
```

Install required packages:

```sh
pip install requirements.txt
```

## Configuration
> Note: We are planning to switch to a better configuration solution.

File `.env`:

```
TOKEN=YOUR_TOKEN
PREFIX=#!
```

## Running

```sh
python3 main.py
````


<h1 align="center">Skymarket</h1>

Skymarket is a web application for creating and viewing ads.

The backend was created using python (Django), the database - PostgreSQL,
frontend - react (SkyPro was provided).

## Installation and usage

### Installation

Install using git:

`git clone https://github.com/YuZu-original/skymarket.git`

or [download](https://github.com/YuZu-original/skymarket/archive/refs/heads/master.zip) the zip archive.

### Setup
1. **Go to the folder.**
   
   Open `skymarket` folder in the terminal.

2. **Create and activate venv.**

    **Windows**:
    
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
    
    **Linux/MacOS**
    
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install requirements**
   
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Run frontend**
   
   Go to the folder `market_postgres` and use:
   
   `docker-compose up --build -d` (Docker need)

2. **Run backend**

   Run backend server.

   Linux\MacOS: `python3 manage.py runserver`

   Windows: `python manage.py runserver`

3. **Let's go!**
   
   Open [http://localhost:3000/](http://localhost:3000/) and start creating ads! 🎉🎉🎉

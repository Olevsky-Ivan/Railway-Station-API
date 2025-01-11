# Django with Docker: Easy Railway Station Manager 🚂🐳

This project uses **Django** to manage railway stations and has a **PostgreSQL** database. It's all packed neatly in **Docker**! 🐋

---

## What’s Inside 📁

```
station_service/            # Main Django project
    railway_station/        # Manages stations and trains
    user/                   # Handles user accounts
    templates/              # HTML files
    static/                 # CSS, JS, and images
.env                        # Hidden settings
requirements.txt           # Python tools list
Dockerfile                 # Builds our app
docker-compose.yml         # Runs everything together
```

### Docker Boxes 🐳

Two main parts:

1. **Django App**:
   - Runs your Python code 📜
   - Found at [http://127.0.0.1:8000](http://127.0.0.1:8000)

2. **Database (PostgreSQL)**:
   - Stores data 📊
   - Works on port `5432`.

---

## Cool Features ✨

- **APIs** for stations, trains, tickets, and more. 🚉
- Login with **JWT tokens**. 🔒
- Built-in API docs using Swagger and ReDoc. 📘
- Everything runs in Docker. 🐳

---

## Getting Started 🛠️

### What You Need ✅

1. **Docker** installed 🐳
2. (Optional) **Python 3.8+** if running locally. 🐍

### Set Up Settings 🌍

Add a `.env` file with:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=db
POSTGRES_USER=railway
POSTGRES_PASSWORD=railway
POSTGRES_HOST=postgres_container
POSTGRES_PORT=5432
```

### Run With Docker 🐋

1. Build everything:
   ```bash
   docker-compose build
   ```

2. Start the app:
   ```bash
   docker-compose up
   ```

3. Check it out:
   - [App](http://127.0.0.1:8000) 🌐
   - [API Docs](http://127.0.0.1:8000/schema/) 📜

### See Running Parts 🧩

Run this to see Docker containers:
```bash
docker ps
```

You’ll see two: the app and the database. 🛠️

---

## Run Without Docker 💻

1. Install Python tools:
   ```bash
   pip install -r requirements.txt
   ```

2. Prepare database:
   ```bash
   python manage.py migrate
   ```

3. Start the app:
   ```bash
   python manage.py runserver
   ```

4. Open [http://127.0.0.1:8000](http://127.0.0.1:8000). 🌐

---

## Database Setup 🗄️

Change `.env` values for PostgreSQL:

```
POSTGRES_DB=my_db
POSTGRES_USER=my_user
POSTGRES_PASSWORD=my_password
POSTGRES_HOST=my_host
POSTGRES_PORT=my_port
```

---

## URLs 🗺️

### Main Routes 🚦

- Admin Panel: `/admin/`
- Station APIs: `/api/station/`
- API Docs:
  - Schema: `/api/doc/`
  - Swagger: `/api/doc/swagger/`
  - ReDoc: `/api/doc/redoc/`
- Login:
  - Get Token: `/api/token/`
  - Refresh Token: `/api/token/refresh/`

### Station APIs 🚉

- Tickets: `/tickets/`
- Crews: `/crews/`
- Orders: `/orders/`
- Routes: `/routes/`
- Trains: `/trains/`
- Stations: `/stations/`
- Journeys: `/journeys/`
- Train Types: `/train-types/`

### User Features 👤

- Create Account: `/create/`
- Your Profile: `/me/`
- Login: `/login/`

---

## Important Tools 🧰

All tools are in `requirements.txt`:

```plaintext
django>=4.0,<5.0
djangorestframework>=3.14,<4.0
djangorestframework-simplejwt>=5.2,<6.0
drf-spectacular>=0.26,<1.0
django-filter>=23.2,<24.0
pytest-django>=4.5,<5.0
pytest>=7.0,<8.0
psycopg2-binary==2.9.10
psycopg==3.1.12
python-dotenv==1.0.0
```

---

## API Docs 📖

Find the API schema at `/schema/` in JSON or YAML format. 🛠️

---

## How To Test 🧪

Run all tests with:

```bash
pytest
```

---

## What’s Next? 🚀

- Add better API examples.
- Make a pretty design for the web. 🎨
- Prepare for production. 🏭

---

## License 📜

This project uses the MIT License. ✅

Docker Structure
[train_session_diagram_a620513487.webp](..%2F..%2F..%2F..%2FAppData%2FLocal%2FTemp%2Ftrain_session_diagram_a620513487.webp)

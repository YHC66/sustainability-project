# Sustainability Actions Tracker

A full-stack web application for tracking sustainability actions, built with Django REST Framework backend and Angular frontend.


### Backend (Django REST API)
- RESTful API endpoints for CRUD operations
- JSON file storage for sustainability actions
- Endpoints:
  - GET /api/actions/ - List all actions
  - POST /api/actions/ - Create new action
  - PUT /api/actions/<id>/ - Update action
  - DELETE /api/actions/<id>/ - Delete action

### Frontend (Angular)
- Display action
- Add action form

## Setup

### Backend Setup
1. Create and activate virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install django djangorestframework django-cors-headers
```

3. Start Django server:
```bash
python manage.py runserver
```
The backend will be available at `http://localhost:8000/api/actions/`

In content, you should input json information like this (in the same line):
"{ "action": "Recycling", "date": "2025-01-08", "points": 25 }"



### Frontend Setup
1. Install Node.js (v18.19.0 or later)

2. Install Angular CLI:
```bash
npm install -g @angular/cli
```

3. Install dependencies:
```bash
cd frontend
npm install
```

4. Start Angular development server:
```bash
ng serve
```
The frontend will be available at `http://localhost:4200`

## API Endpoints tips

### PUT /api/actions/<id>/
Update existing action
- go to /api/actions/<id>/ to do the update

### DELETE /api/actions/ <id> /
Delete specific action
- go to /api/actions/ <id> / to do the delete



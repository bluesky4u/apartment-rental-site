# Apartment Rental Site

This is a site for viewing apartment rentals posted by a single admin. It is built using the [Django](https://www.djangoproject.com/) web framework
and [Django Rest Framework](https://www.django-rest-framework.org/) as the backend [Nuxt.js](https://nuxtjs.org/) as the frontend.

## Demo

![Demo](/demo/apartment-rentals-3.png)
More screenshots can be found in the [demo](/demo) folder.
For a live demo, visit [https://apartment-rental-site.vercel.app/](https://apartment-rental-site.vercel.app/)
For the admin panel, visit [https://apartment-rental-site.vercel.app/admin](https://apartment-rental-site.vercel.app/admin)

Login with the following credentials:

```
username: admin
password: admin
```

## Directory Structure

The backend is located in the [backend directory](/backend/). The frontend is located in the [frontend directory](/frontend/).

## Installation

The backend and frontend can be separate projects if you have your own api endpoints you'd like use. They can be installed and run independently of each other.
The backend needs to be running in order for the frontend to receive data.

### Requirements

- Python 3.6+
- Node.js 10.13+

1. Clone the repository

### Backend

#### Backend Installation

1. Navigate to the backend directory
1. Install the requirements

```bash
pip install -r requirements.txt
```

3. Run the migrations

```bash
python manage.py migrate
```

4. Create a superuser

```bash
python manage.py createsuperuser
```

5. Run the server

```bash
python manage.py runserver
```

> Server will be running on <http://localhost:8000>

### Frontend

Look at the [nuxt 3 documentation](https://v3.nuxtjs.org) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# yarn
yarn install

# npm
npm install

# pnpm
pnpm install --shamefully-hoist
```

## Development Server

Start the development server on <http://localhost:3000>

```bash
npm run dev
```

## Production

Build the application for production:

```bash
npm run build
```

Locally preview production build:

```bash
npm run preview
```

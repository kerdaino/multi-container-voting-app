Multi-Container Voting App

Project Overview

The Multi-Container Voting App is a Dockerized web application that allows users to vote between predefined options and view voting results in real time.

The project demonstrates modern DevOps practices including containerization, CI/CD automation, cloud deployment, and multi-service application architecture.

⸻

Project Type

Web Application: Voting Application

Purpose

The application allows users to:

* Vote between available options.
* Store votes in a PostgreSQL database.
* Process vote data using a Node.js worker service.
* Display voting results through a Flask-based results application.

⸻

Project Objectives

1. Build a multi-container application using Docker Compose.
2. Demonstrate communication between multiple services.
3. Implement CI/CD using GitHub Actions.
4. Deploy a containerized application on AWS EC2.
5. Apply DevOps best practices including version control, automation, and cloud deployment.
6. Provide a simple voting platform with real-time result tracking.

⸻

Features

* Vote through a web interface.
* Store votes in PostgreSQL.
* Process votes using a Node.js worker service.
* Display voting results.
* Containerized architecture using Docker Compose.
* Automated deployment using GitHub Actions.
* Cloud deployment on AWS EC2.

⸻

Technology Stack

Frontend

* Flask (Python)

Backend Services

* Flask (Python)
* Node.js

Database

* PostgreSQL

Containerization

* Docker
* Docker Compose

CI/CD

* GitHub Actions

Cloud Infrastructure

* AWS EC2

Container Registry

* Docker Hub

⸻

System Architecture

User → Flask Voting App → PostgreSQL Database → Node.js Worker → Flask Results App

All services communicate through Docker Compose within a shared Docker network.

⸻

Project Structure

multi-container-voting-app/
│
├── vote-app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│
├── result-app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│
├── worker/
│   ├── worker.js
│   └── package.json
│
├── db/
│   └── init.sql
│
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
└── .github/workflows/
    └── deploy.yml

⸻

Running Locally

Prerequisites

* Docker Desktop
* Docker Compose
* Git

Clone Repository

git clone https://github.com/kerdaino/multi-container-voting-app.git
cd multi-container-voting-app

Create Environment File

cp .env.example .env

Start Application

docker compose up --build

Access Application

Voting Application:

http://localhost:5050

Results Application:

http://localhost:5001

⸻

Environment Variables

Create a .env file based on .env.example.

Example:

POSTGRES_DB=voting_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

⸻

CI/CD Workflow

The project uses GitHub Actions for Continuous Integration and Continuous Deployment.

Workflow:

1. Developer pushes code to GitHub.
2. GitHub Actions workflow is triggered.
3. Docker images are built automatically.
4. Images are pushed to Docker Hub.
5. AWS EC2 server pulls updated images.
6. Docker Compose redeploys the application.

⸻

Deployment

AWS EC2

The application is deployed on an AWS EC2 instance using Docker Compose.

Live URLs

Voting Application:

http://13.49.243.111:5050

Results Application:

http://13.49.243.111:5001

⸻

Challenges Encountered

Docker Installation Issues

Docker was initially unavailable on the development environment.

Solution: Installed Docker Desktop and configured Docker Compose.

Port Conflicts

Local ports were already occupied.

Solution: Updated application port mappings.

AWS Security Group Restrictions

Application ports were inaccessible externally.

Solution: Configured inbound security group rules for required ports.

CI/CD Configuration

Deployment automation required proper secret management.

Solution: Configured GitHub Secrets and Docker Hub integration.

⸻

Results

* Successfully built a multi-container application.
* Implemented Docker Compose orchestration.
* Automated deployment using GitHub Actions.
* Integrated Docker Hub image registry.
* Deployed application successfully on AWS EC2.
* Achieved end-to-end cloud deployment workflow.

⸻

Future Improvements

* User authentication and authorization.
* Real-time vote updates using WebSockets.
* Enhanced UI/UX design.
* Voting analytics dashboard.
* Support for multiple voting categories.
* Monitoring and logging integration.

⸻

Team Members

* Tobi Adekunle – Team Lead / Development
* Adekunle Jamiu Oyetayo 
* Edet Rosemary Linus
* John Olabeda 
* Ebimoboere Gabriella
* Chukwusa Augustine
* Isaac Ankeli
* Oluwatobi Adekunle
* Wahab Habeeb Kayode
* Afeez Bakare
* James Edgal
* Samson Imhen-isi
* Etiwelu Augustine Chidiebere
* Adedamola Oluwafemi Ige
* Adeyemi Moses
* Monsur-Suleiman Muhsinah
* Joshua Okoro
* Oluwafisayomi Akanji
* Tochukwu EzeObi
* Amina Ibrahim



⸻

Repository

GitHub Repository:

https://github.com/kerdaino/multi-container-voting-app

⸻

License

This project was developed as part of a Cloud Computing and DevOps Capstone Project.
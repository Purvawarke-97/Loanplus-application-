# LoanPlus Application

## About the Project

LoanPlus is a web-based loan application that allows users to apply for and manage loan applications online.

I developed this project using a **three-tier architecture**, where the frontend, backend, and database are separated.

## Architecture

The basic flow of the application is:

**User → Load Balancer → EC2 → RDS**

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python
* **Database:** MySQL on Amazon RDS
* **Web Server:** Nginx

## AWS Services Used

* Amazon EC2
* Amazon VPC
* Amazon RDS
* Application Load Balancer
* Amazon S3
* Auto Scaling
* IAM
* Security Groups
* CloudFormation
* AMI

## How It Works

1. The user opens the LoanPlus application.
2. The request goes through the Application Load Balancer.
3. The Load Balancer sends the request to the EC2 server.
4. The frontend is served using Nginx.
5. The Python backend processes the request.
6. The backend connects to the MySQL database hosted on Amazon RDS.
7. The required data is stored or retrieved from the database.

## AWS Architecture

The project uses a custom VPC with public and private subnets.

* Frontend and application servers run on EC2.
* The database is hosted on Amazon RDS.
* Security Groups are used to control network traffic.
* Load Balancer is used to distribute incoming traffic.
* S3 is used for file/object storage.

## What I Learned

Through this project, I got practical experience with:

* AWS EC2
* VPC and Subnets
* RDS
* Load Balancer
* Security Groups
* IAM
* Linux
* Nginx
* Three-tier architecture

## Technologies Used

**Frontend:** HTML, CSS, JavaScript
**Backend:** Python
**Database:** MySQL
**Cloud:** AWS
**Server:** Nginx, Linux

## Project Goal

The main goal of this project was to understand how a real-world three-tier application can be deployed and managed using AWS services.

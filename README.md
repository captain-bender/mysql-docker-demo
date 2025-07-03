# MySQL Docker Classroom Setup

This repository contains a Dockerfile and initialization SQL script to run a MySQL database pre-populated with the Classicmodels sample dataset. It is designed for teaching and experimentation.

## Requirements

- Docker Desktop installed (Windows, Mac, Linux)
- Basic knowledge of Docker commands
- Install a MySQL client, such as the [DBeaver](https://dbeaver.io/download/) app, or something relevant compatible with your OS.

## Getting Started

1. Clone this repository:
```
git clone https://github.com/captain-bender/mysql-docker-demo.git
cd mysql-docker-demo
```

3. Run the container:
```
docker run -d --name mysql-demo -p 3306:3306 classicmodels-mysql
```

4. Connect to MySQL using your preferred client (e.g., DBeaver):
- Host: `localhost`
- Port: `3306`
- User: `root`
- Password: `passwd`
- Database: `classicmodels`

5. Have a look in the [database schema](./MySQL-Sample-Database-Diagram-PDF-A4.pdf) and run sample queries, for example:
```
SELECT * FROM customers LIMIT 5;
```

## Troubleshooting
- If you get a "Public Key Retrieval is not allowed" error in DBeaver, set `allowPublicKeyRetrieval=true` in the connection properties.
- Make sure Docker Desktop is running and WSL2 is enabled on Windows.

## Credits
- MySQL sample database from [MySQLTutorial](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/) website.
title: Project: Tartan Smart Home System
date: 2024-01-06
tags: project, grading
authors: Hazel Victoria Campbell, Dr. Sarah Nadi
status: published
summary: Tartan System

----

# Platform Installation and Configuration

The initial configuration for the Tartan Smart Home System is done via a YAML
file named *config.yml*. The configuration file contains the initial settings
needed for the system including:

- The configuration information for the Hubs connected to the platform.
- The timer for the data historian (see below).
- The configuration settings for database.

The team has prepared docker containers to quickly get the system up and
running, but for understanding how the system actually works, we describe the
technical components and their configuration below.

## Dependencies

The platform is written in Java, using Java 11. If OpenJDK is used,
dependencies for javafx may need to be installed additionally (e.g., `apt-get
install openjfx` on Ubuntu). Gradle 7.3 is used as a build system and already
included with the gradlew wrapper. Various Java dependencies are automatically
downloaded during the build from the public Maven repository. MySQL 8.0 is used
as database engine. Python 3.7 is used to execute the house simulator/hub.

## Installation/Download links

* Gradle: https://gradle.org/install/
   * For the Gradle Wrapper: go to the directory and run `gradle wrapper`, then you can start using `gradlew`
      e.g., 
      ```
      cd smart-home/Platform
      gradle wrapper
      ```
* Java (Windows): https://www.oracle.com/ca-en/java/technologies/javase/jdk11-archive-downloads.html
* MySQL (Ubuntu): https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04
* MySQL (Windows): https://downloads.mysql.com/archives/installer/ Change version to 8.0
* Docker (Ubuntu): https://docs.docker.com/engine/install/ubuntu/
* Docker Desktop (Docker for Windows): https://docs.docker.com/docker-for-windows/install/
* Windows Subsytem for Linux (needed for Docker Desktop): https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

## Database Configuration

The underlying database used in the current system is [MySQL](https://www.mysql.com/). The *config.yml*
file contains the basic settings for this database:

```yaml
database:
   # the name of the JDBC driver to use
   driverClass: com.mysql.cj.jdbc.Driver

   # the DB username
   user: tartan

   # the DB password
   password: tartan1234

   # the JDBC URL; the database is called TartanHome
   url:
jdbc:mysql://localhost/TartanHome?useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC

   # Allow Hibernate to create tables
   properties:
       hibernate.dialect: org.hibernate.dialect.MySQLDialect

       # leave it to hibernate to update/create the database.
       # Warning, this is generally considered a bad setting for production
       hibernate.hbm2ddl.auto: update
```

That is, the system expects access to a MySQL database on localhost with a user
named **tartan** with a password of **tartan1234** and a database named
**TartanHome**. You can use the sample SQL script *init.sql* found inside the
Database subfolder to create the database and the user. Tables within this
database are automatically created when the system is run. Note that these
credentials are specified in the system YAML configuration file (*config.yml*).

## Building the Platform

The system is currently developed in `smart-home` folder. It contains the
Tartan Service Platform code as well as the house simulator (the Hub).

The current implementation uses Gradle as the build system. You may want to use the
gradle wrapper **gradlew** available in the relevant folders which will automatically
download and use the correct gradle version. To that end, use `./gradlew` in Ubuntu
and macOS, or `gradlew.bat` in Windows. You can supply the same parameters to **gradlew**
as simple **gradle**, e.g., `./gradlew build`.

In the Platform project (*smart-home* directory), executing `./gradlew shadowJar`
inside the */Platform* subfolder will create a single *tartan-1.0-SNAPSHOT.jar*
file that contains the Platform and all dependencies. This file will be created
inside the */Platform/build/libs* subfolder. The Platform can then be launched
with `java -jar build/libs/tartan-1.0-SNAPSHOT.jar <parameters>` (see below for more
details about the parameters).

Many of these decisions were made for legacy reasons. Your team may change all
of these technical decisions and tooling if preferred.

## Running the System

The system consists of the following components that must be launched:

1. One or more House Hubs (the house simulator, inside *smart-home/HouseSimulator* subfolder)
2. The MySQL database (*smart-home/Database* subfolder)
3. The Tartan Service Platform (*smart-home/Platform* subfolder)

A docker setup is provided with a finished configuration in the smart-home
folder that starts two houses. You can launch it with:

```bash
docker-compose up --build
```

If you want to run this version, note that there is a separate config file,
*config.docker.yml*, that is used in this case.

If you have made changes and want your docker setup to reflect it, run
```bash
 docker-compose down && docker-compose build --no-cache && docker-compose up
```


### Windows differences
* Open Docker Desktop and under "Container / Apps" remember to "Start" the "smart-home" container.

Below are the instructions to launch the components individually without docker.
However, it is recommended to use Docker Compose instead of manually controlling
the start and shutdown of the components.

### The House Simulator

The house simulator is a simple Python program that takes two command line
arguments: the host and port to listen for incoming connections. To run the
house simulator simply execute the following command inside */HouseSimulator*
directory (port will need to be changed for each house if simulating multiple
houses):

```bash
python3 simple_server.py localhost 5050
```

The start a second house, consistent with the default *config.yml* configuration,
execute the following command on another command window:

```bash
python3 simple_server.py localhost 5051
```

### The Historian Database

You must start the MySQL server to log house history. You have to make sure that
you start the database before you start the platform. MySQL is typically
started via the following command in Ubuntu:

```bash
sudo systemctl start mysql
```
To start the MySQL service in Windows:
Search for "services" in the Windows search bar, then scroll down and start the "MySQL" service.

If running manually (not using `docker-compose`) then you need to create the database and user manually as well. The following example is for a Windows system.
```
cd C:\Users\UserName\Documents\CMPUT 402\Tartan\smart-home\Database
"C:\ProgramFiles\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p 
source init.sql
```
### The Tartan Smart Home Service

This, again, requires MySQL server. The Platform can be run using the following
command (from */Platform* subfolder):

```bash
java -jar build/libs/tartan-1.0-SNAPSHOT.jar server config.yml
```

It can also be executed with `./gradlew run`, which will pass the same
parameters automatically. Note that the platform must be launched after the
database and the house hub/simulator scripts are running.

This is the standard way to run a [Dropwizard
application](https://www.dropwizard.io/en/stable/getting-started.html). The
`server` command runs your application as an HTTP server and the YAML file
*config.yml* contains the initial configuration settings. If the system is
running correctly, then you should be able to access it by navigating to the
following URL in a web browser:

```
http://localhost:8080/smarthome/state/<housename>
```

Note that **mse** and **cmu** are the names of the default houses configured in
config.yml. The default username and password for access to the system is also
configured in this file ("admin" and "1234" for **mse**, "admin" and "5678" for
**cmu**).

#### Possible issues

While trying to run The Platform, you may encounter the following error:
> _javax.net.ssl.SSLHandshakeException: No appropriate protocol (protocol is disabled or cipher suites are inappropriate)_

Appending `&enabledTLSProtocols=TLSv1.2` to the end of the `${database.url}` property in _config.yml_ will fix the issue (see the [StackOverflow solution](https://stackoverflow.com/a/67918194/9985287)).

ARM based Mac Issues:

ARM based macs (M1 or M2) might have issues running MySQL. If that happens, make sure you are running MySQL 8.0 and not any lower version, even when running with Docker.

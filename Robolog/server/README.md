# Robolog Server

Robolog uses the [CKAN open source data portal](http://ckan.org/) for data ingestion, tagging, indexing, search, retrieval and collaboration. CKAN is used with the default "development" configuration which simplifies installation and allows Robolog to run in a variety of Linux environments. This brief guide walks through the minimum steps needed to install CKAN for use with the Robolog client scripts.

## Overview

The simplest way to install Robolog and CKAN is to follow this process:

1. Create an Ubuntu server using your own hardware or a hosted VM
2. Make the server accessible to external clients (optional)
3. Download and configure the CKAN prerequisites (e.g. open-jdk, solr, git, postgres and python)
4. Download the CKAN source code package
5. Create a CKAN configuration file (development.ini)
6. Create your Team's "robolog.cfg" file with the appropriate parameter settings
7. Load a sample telemetry log file and verify that it's visible in the CKAN portal and accessible via its URL

## Prerequisities

This guide summarizes the [Install CKAN from Source](http://docs.ckan.org/en/latest/maintaining/installing/install-from-source.html) documentation on the CKAN website. Consult this guide for complete information.

The following setup is recommended for a basic evaluation:

* [Ubuntu 14.04.03 LTS (64-bit)](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes?_ga=1.253912650.374798248.1451753044). Use the desktop version if you want to evaluate Robolog in a self-contained environment.
* 4.0GB (4096MB) of RAM
* 10GB of disk space (minimum). Each Robolog telemetry file will use between 2MB-3MB of space (uncompressed).

The installation will use CKAN 2.5.1 and Python 2.7.6.

## Create an Ubuntu server using your own hardware or a hosted VM

If you've never installed Ubuntu, consider following the [Ubuntu Installation Tutorial for FRC](Ubuntu Installation Tutorial for FRC.md). This tutorial will guide you through the installation of Oracle VirtualBox and Ubuntu Desktop 14.04 LTS.

## Make the server accessible to external clients (optional)

A publicly-visible IP address is required if you want to access CKAN from external web browsers and programs. Network setup will vary depending on how Ubuntu has been deployed. For VirtualBox see the VirtualBox documentation section on [virtual networking](http://www.virtualbox.org/manual/ch06.html)

NOTE: this is an optional step. You can use Firefox from the Ubuntu desktop to connect to CKAN locally. If you decide to configure Ubuntu as a network host, change the "127.0.0.1" references below to the assigned IP address for your Ubuntu instance.

## Download and configure the CKAN prerequisites

Install the Ubuntu package prerequisites:

    sudo apt-get install python-dev postgresql libpq-dev python-pip python-virtualenv git-core solr-jetty openjdk-7-jdk python-pastescript python-pylons


Create the required CKAN directories and set permissions:

    cd $HOME

    sudo mkdir -p /usr/lib/ckan/default
    sudo chown `whoami` /usr/lib/ckan/default
    sudo mkdir -p /usr/lib/ckan/default/resources
    sudo chown `whoami` /usr/lib/ckan/default/resources

    mkdir -p ~/ckan/lib
    sudo ln -s ~/ckan/lib /usr/lib/ckan
    mkdir -p ~/ckan/etc
    sudo ln -s ~/ckan/etc /etc/ckan
    
Setup a Python virtual environment for CKAN, then activate it in your shell:

    virtualenv --no-site-packages /usr/lib/ckan/default
    . /usr/lib/ckan/default/bin/activate

Install CKAN 2.5.1 from source:

    pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.5.1#egg=ckan'
    
Install the python packages required by CKAN: 

    pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt
    
Deactivate, then re-initialize the Python virtual environment

    deactivate
    . /usr/lib/ckan/default/bin/activate

Create the postgres user and database used by CKAN.  Give the 'ckan_default' user the password 'frc2016':
    
    sudo -u postgres createuser -S -D -R -P ckan_default
    sudo -u postgres createdb -O ckan_default ckan_default -E utf-8
    
Create a CKAN development configuration file:

    paster make-config ckan /etc/ckan/default/development.ini
    
Use vi (or gedit or nano) to make the following changes to the development.ini file:

    vi /etc/ckan/default/development.ini
	
	# the following are settings in the file, not shell commands:
	
	sqlalchemy.url = postgresql://ckan_default:frc2016@localhost/ckan_default
	ckan.site_url = http://127.0.0.1:5000
	solr_url=http://127.0.0.1:8983/solr

Use vi (or gedit or nano) to make the following changes to /etc/defaut/jetty:

    sudo vi /etc/default/jetty

	# the following are settings in the file, not shell commands:

	NO_START=0            
	JETTY_HOST=127.0.0.1
	JETTY_PORT=8983
	JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/

Configure SOLR to work with CKAN:

    sudo mv /etc/solr/conf/schema.xml /etc/solr/conf/schema.xml.bak
    sudo ln -s /usr/lib/ckan/default/src/ckan/ckan/config/solr/schema.xml /etc/solr/conf/schema.xml

Download and install JSP support for Jetty, then start it:

    cd $HOME/Downloads
    wget 'https://maven-us.nuxeo.org/nexus/content/repositories/public/jetty/jsp/2.1-6.0.2/jsp-2.1-6.0.2.jar'
    sudo cp jsp-2.1-6.0.2.jar /usr/share/jetty/lib/.
    sudo service jetty restart

Initialize the CKAN database:

    cd /usr/lib/ckan/default/src/ckan
    paster db init -c /etc/ckan/default/development.ini
    
Initialize CKAN security, giving the 'sysadmin' account the password 'frc2016':

    cd /usr/lib/ckan/default/src/ckan
    ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini
    paster sysadmin add sysadmin -c /etc/ckan/default/development.ini
    
Start CKAN, then use Firefox to navigate to the portal:

    cd /usr/lib/ckan/default/src/ckan
    paster serve /etc/ckan/default/development.ini

## Operations

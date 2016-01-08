# Robolog Server

Robolog uses the [CKAN open source data portal](http://ckan.org/) for data ingestion, tagging, indexing, search, retrieval and collaboration. CKAN is used with the default "development" configuration which simplifies installation and allows Robolog to run in a variety of Linux environments. This brief guide walks through the minimum steps needed to install CKAN for use with the Robolog client scripts.

## Overview

The simplest way to install Robolog and CKAN is to follow this process:

1. Create an Ubuntu server using your own hardware or a hosted VM
2. Make the server accessible to external clients (optional)
3. Download and configure the CKAN prerequisites (e.g. open-jdk, solr, postgres, Python and Python packages)
4. Download the CKAN source code package
5. Create a CKAN configuration file (development.ini)
6. Create your Team's "robolog.cfg" file with the appropriate parameter settings
7. Load a sample telemetry log file and verify that it's visible in the CKAN portal and accessible via its URL

## Prerequisities

This guide summarizes the [Install CKAN from Source](http://docs.ckan.org/en/latest/maintaining/installing/install-from-source.html) documentation on the CKAN website. Consult this guide for complete information.

The following setup is recommended for a basic evaluation:

* [Ubuntu 14.04.03 LTS (64-bit)](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes?_ga=1.253912650.374798248.1451753044).  Use the desktop version if you want to evaluate Robolog in a self-contained environment.
* 4.0GB (4096MB) of RAM
* 10GB of disk space (minimum).  Each Robolog telemetry file will use between 2MB-3MB of space (uncompressed).

## Create an Ubuntu server using your own hardware or a hosted VM

If you've never installed Ubuntu, consider following the [Ubuntu Installation Tutorial for FRC](Ubuntu Installation Tutorial for FRC.md). This tutorial will guide you through the installation of Oracle VirtualBox and Ubuntu Desktop 14.04 LTS.

http://www.virtualbox.org/manual/ch06.html

## Make the server accessible to external clients (optional)

A publicly-visible IP address is required if you want to access CKAN from external web browsers and programs. Network setup will vary depending on how Ubuntu has been deployed.  For VirtualBox see the VirtualBox documentation section on [virtual networking](http://www.virtualbox.org/manual/ch06.html)

This is an optional step.  You can use Firefox from the Ubuntu desktop to connect to CKAN locally.  If you decide to configure Ubuntu as a network host, change the "127.0.0.1" references below to the assigned IP address for your Ubuntu instance.

## CKAN Installation and Configuration

Follow these steps to install and configure CKAN (v2.5.1) and Python (v2.7.3) for use with Robolog.

Install the Ubuntu package prerequisites:

```
sudo apt-get install python-dev postgresql libpq-dev python-pip python-virtualenv git-core solr-jetty openjdk-7-jdk python-pastescript python-pylons
```

## Operations

# Robolog Server

Robolog uses the [CKAN open source data portal](http://ckan.org/) for data ingestion, tagging, indexing, search, retrieval and collaboration. CKAN is used with the default "development" configuration which simplifies installation and allows Robolog to run in a variety of Linux environments. This brief guide walks through the minimum steps needed to install CKAN for use with the Robolog client scripts.

## Overview

The simplest way to install Robolog and CKAN is to follow this process:

1. Create an Ubuntu server using your own hardware a hosted VM
2. Make the server accessible to external clients
3. Download and configure the CKAN prerequisites. This consists of verifying the Python 2.7 setup and installing the additional Python packages that CKAN requires
4. Download the CKAN source code package
5. Create a CKAN configuration file (development.ini)
6. Create your Team's "robolog.cfg" file with the appropriate parameter settings
7. Load a sample telemetry log file and verify that it's visible in the CKAN portal and accessible via its URL

## Prerequisities

This guide summarizes the [Install CKAN from Source](http://docs.ckan.org/en/latest/maintaining/installing/install-from-source.html) documentation on the CKAN website. Consult this guide for complete information.

### Server Resources

The following setup is recommended for a basic evaluation:

* [Ubuntu 14.04.03 LTS (64-bit)](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes?_ga=1.253912650.374798248.1451753044).  Use the desktop version if you want to evaluate Robolog in a self-contained environment.
* 4.0GB (4096MB) of RAM
* 10GB of disk space (minimum).  Each Robolog telemetry file will use between 2MB-3MB of space (uncompressed).

### Ubuntu Installation

If you've never installed Ubuntu, consider following the [Ubuntu Installation Tutorial for FRC](Ubuntu Installation Tutorial for FRC). This tutorial will guide you through the installation of Oracle VirtualBox and Ubuntu Desktop 14.04 LTS.
 
### Installation

## Operations

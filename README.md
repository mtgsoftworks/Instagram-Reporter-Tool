# IRT® - Instagram Reporter Tool

This Python script can be used to report Instagram accounts for certain violations. After users enter a specific Instagram username, the script automatically retrieves the Instagram User ID of that account. Users can then select a reason to report that account and, if necessary, report multiple accounts simultaneously using multithreading.

# Requirements
Python 3 is required to run this script. It also requires the standard libraries requests, re, time, and random, and the multiprocessing module.
# Installation
Before running the script, run the following command in the terminal or command prompt to install the required modules:

# Usage
When you run the script, a text file with users (users.txt) and a text file with proxy servers (proxy.txt) are loaded.
Next, enter the username of the Instagram account to report.
The script will automatically retrieve the user ID of this account and ask you to select a reporting reason.
Optionally, you can speed up reports using multithreading.

# Features

# User Friendly Interface: 
Users can use the script through a simple text-based interface.
# Proxy Support: 
You can anonymously report Instagram accounts using proxy servers.
# Multi-Threading Support: 
In case the need arises, 

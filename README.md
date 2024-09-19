# Automating_bgp_prefix_list
BGP Prefix List Automation with Flask
This Flask application automates the generation of BGP prefix lists for Juniper routers using the bgpq4 tool. 
It provides a web interface where users can input parameters such as name, AS number, prefix type, and prefix length to generate the prefix list configuration.

Prerequisites
Python 3.x
Flask
bgpq4 tool

Installation
Clone the repository:
Copy
git clone the repository

cd into the repository

Install dependencies:
pip install Flask

Install bgpq4 tool:
For Ubuntu/Debian:
sudo apt-get install bgpq4

For CentOS/RHEL:
sudo yum install bgpq4

Usage
Run the Flask application:

python your_script_name.py

Access the application in your browser at http://localhost:5000.

Fill in the required fields:

Name: Name of the prefix list

AS Number: Autonomous System number

Prefix Type: IPv4 or IPv6

Prefix Length: (Optional) Length of the prefixes

Click on the "Generate Prefix List" button to create the BGP prefix list.

![image](https://github.com/user-attachments/assets/c0d6353b-4734-44e2-b1d1-b62ae723c62f)

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This project uses the Flask web framework.
The bgpq4 tool is utilized for generating the BGP prefix lists.

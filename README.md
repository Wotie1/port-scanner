# port-scanner

🔍 Python TCP Port Scanner

A lightweight, multithreaded TCP port scanning tool written in Python.

This project demonstrates basic network programming, TCP connection handling, socket management, threading, and error handling using Python's standard library.

📌 About the Project

Python TCP Port Scanner is an educational network utility designed to check TCP ports on a specified host.

The program attempts to establish TCP connections to ports within a predefined range and reports ports that accept connections.

It also displays the standard service name associated with each detected open port.

This project is intended for educational purposes and authorized network testing only.

✨ Features
Multithreading: Uses 50 worker threads to process port checks concurrently.
TCP Port Scanning: Checks TCP ports from 1 to 1000.
Open Port Detection: Identifies ports that accept TCP connections.
Service Name Lookup: Displays standard service names associated with port numbers.
Timeout Handling: Uses socket timeouts to prevent indefinite connection attempts.
Error Handling: Handles DNS resolution and socket-related errors.
Automatic Socket Cleanup: Closes sockets using finally to help prevent resource leaks.
Lightweight: Built using Python's standard library without external dependencies.
🛠️ Technologies Used
Technology	Purpose
Python 3	Main programming language
Socket	TCP networking
Threading	Concurrent execution
Queue	Task management
Datetime	Date and time utilities
📋 Requirements
Python 3.8 or newer
Basic networking knowledge
Permission to scan the target system

No external Python packages are required.

🚀 Installation

Clone the repository:

bash
git clone https://github.com/YOUR-USERNAME/python-tcp-port-scanner.git


Navigate to the project directory:

bash
cd python-tcp-port-scanner


Run the program:

bash
python scanner.py

💻 Usage

When the program starts, it asks for a target hostname or IP address.

Example:

text
Target IP (e.g., google.com): 192.168.1.10


The scanner then checks the configured TCP port range.

Example output:

text
Scanning: 192.168.1.10
--------------------------------------------------
Port 22 OPEN | Service: ssh
Port 80 OPEN | Service: http
Port 443 OPEN | Service: https
--------------------------------------------------
Scanning Completed.


Example output is illustrative and does not represent a real scan.

⚙️ How It Works
The user enters a hostname or IP address.
DNS resolution converts the hostname into an IP address when necessary.
A queue stores the ports to be checked.
Multiple worker threads retrieve port numbers from the queue.
Each worker attempts a TCP connection.
Successful connections are reported as open ports.
The program looks up the standard service name associated with each port.
Sockets are closed after each attempt.
The program waits until all queued tasks are completed.
⚠️ Limitations

This project has some technical limitations:

Only TCP ports are checked.
The default scanning range is 1–1000.
Service names are obtained from the system's standard service database. They do not confirm the actual application running on a port.
A successful TCP connection does not reveal whether a service is vulnerable.
Firewalls and network filtering may affect results.
Connection timeouts may cause some reachable ports to be missed.
Scanning results are not a complete security assessment.
🔐 Security & Ethical Use

This tool is intended for:

Personal laboratory environments.
Your own computers and servers.
Authorized network administration.
Python socket programming education.

Important: Only scan systems and networks for which you have explicit authorization.

Unauthorized port scanning may violate organizational policies or applicable laws.

The author does not encourage or accept responsibility for unauthorized use of this software.

📚 Learning Objectives

This project helps demonstrate:

TCP/IP fundamentals.
Python socket programming.
Multithreaded applications.
Queue-based task management.
Exception handling.
Network service identification.
Resource management and socket cleanup.
🔮 Future Improvements

Potential future development ideas:

Configurable port ranges.
Exporting scan results to TXT or JSON.
Improved service identification.
Logging and reporting.
Configurable timeout values.
A graphical user interface.

These are proposed improvements and are not necessarily implemented in the current version.

🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

If you find an issue or have an improvement idea, feel free to open an issue or submit a pull request.

📄 License

This project is intended to be distributed under the MIT License.

Before publishing, add an MIT LICENSE file to the repository.

👨‍💻 Author

YOUR NAME

GitHub: https://github.com/YOUR-USERNAME

⭐ If you find this project useful for learning Python networking, consider giving the repository a star.
# Enterprise Hybrid Cloud Monitoring with Splunk

## Project Overview
This project simulates a corporate environment where a centralized Linux Control Node monitors the health of internal Windows Web Servers. It uses custom Python automation to bypass standard ICMP blocks and feeds real-time data into Splunk Enterprise for dashboard visualization and outage detection.

## Architecture
- **Control Node:** Ubuntu Linux (EC2) running Splunk Enterprise & Python Automation.
- **Target Node:** Windows Server 2022 (EC2) configured with IIS via User Data.
- **Security:** Nodes communicate over private IPs within a VPC; Security Groups restrict traffic to internal monitoring only.

## Key Features
- **Infrastructure as Code:** Windows Server firewall and IIS configured automatically at boot using User Data scripts.
- **Custom Automation:** `healthcheck.py` script performs continuous internal connectivity checks.
- **Real-Time Observability:** Splunk Dashboard captures "UP/DOWN" states with sub-30-second latency.

## How to Run
1. Deploy EC2 instances (Linux & Windows).
2. Install Splunk on Linux: `sudo dpkg -i splunk.deb`.
3. Run the monitor: `nohup python3 healthcheck.py &`.
4. Configure Splunk to monitor `/home/ubuntu/server_status.log`.

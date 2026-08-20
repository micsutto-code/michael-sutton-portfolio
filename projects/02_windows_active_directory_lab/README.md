# Windows Active Directory & Security Lab

## Project Overview

This project documents the design and development of a virtualized Windows domain environment built in my home lab using Proxmox VE.

The lab provides hands-on experience with Windows Server administration, Active Directory, Group Policy, endpoint management, security configuration, event logging, and troubleshooting. It is also being developed as the foundation for a SOC-style environment focused on centralized logging, security monitoring, and incident investigation.

## Lab Environment

| System | Operating System | Role |
| --- | --- | --- |
| DC01 | Windows Server 2022 | Domain Controller / Active Directory |
| SRV01 | Windows Server 2022 | Member Server |
| Client01 | Windows 10 | Domain-Joined Workstation |
| Client02 | Windows 11 Education | Domain-Joined Workstation |

The environment is virtualized using **Proxmox VE**.

## Work Completed

- Deployed Windows Server 2022 virtual machines
- Configured Active Directory Domain Services
- Created a Windows domain environment
- Joined Windows 10 and Windows 11 clients to the domain
- Created organizational units (OUs) for servers and workstations
- Organized domain systems into appropriate OUs
- Created and applied a workstation security baseline Group Policy Object
- Increased Windows Event Log sizes to support security monitoring
- Configured remote administration of lab systems
- Created Proxmox snapshots after major configuration milestones
- Began configuring centralized Windows Event Forwarding

## Active Directory Structure

The lab uses separate organizational units to provide logical management of systems and support targeted Group Policy application.

- **Servers OU**
  - SRV01
- **Workstations OU**
  - Client01
  - Client02

DC01 provides the domain controller and Active Directory services for the environment.

## Security & Administration Concepts

This project provides hands-on practice with:

- Active Directory administration
- Windows Server administration
- Domain membership and authentication
- Organizational Units
- Group Policy
- Security baselines
- Windows Event Logs
- Centralized event collection concepts and configuration
- Remote system administration
- Troubleshooting permissions and configuration issues
- Virtual machine management and recovery

## Current Development

Windows Event Forwarding is currently being developed and tested for centralized collection of security-relevant events.

The longer-term goal is to use the Windows domain as part of a SOC-style lab where controlled activity can be generated, collected, investigated, and eventually visualized through security dashboards.

## Evidence & Documentation

Screenshots and additional technical documentation will be added as the lab continues to develop.

Planned documentation includes:

- Active Directory structure
- Domain-joined systems
- Group Policy configuration
- Windows Event Log configuration
- Windows Event Forwarding
- Security monitoring workflows
- Troubleshooting examples

## Skills Demonstrated

**Windows Server 2022 • Active Directory • Group Policy • Windows 10/11 • Proxmox VE • Windows Event Logging • System Administration • Security Monitoring • Troubleshooting**

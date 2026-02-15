# Project 01 – Homelab Security Baseline (Ubuntu Server Hardening)

## Overview
This project establishes a secure baseline configuration for an Ubuntu Server virtual machine in a home lab environment. The goal is to reduce attack surface, enforce secure authentication, and implement basic intrusion prevention mechanisms.

## Lab Environment
- Host: 2018 Intel Mac mini
- Hypervisor: VMware
- Guest OS: Ubuntu Server 24.04 LTS
- Network Mode: NAT 
- VM IP Address: 172.16.250.134

## Security Objectives
- Enforce SSH key-based authentication
- Disable password-based SSH login
- Configure firewall rules using UFW
- Implement brute-force protection using Fail2ban
- Enable automatic security updates
- Validate configuration using log review

---

## Step 1 – System Updates

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Step 2 – SSH Hardening

### SSH Key-Based Authentication

Generated SSH key on host system:

```bash
ssh-keygen -t ed25519 -C "michael-homelab"

Copied public key to server
~/.ssh/authorized_keys

Set correct permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

Disabled Password Authentication
Initial configuration in /etc/ssh/sshd_config:
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes

After restarting SSH, passowrd authentication was still enabled.
Validated effective configuration:
sudo sshd -T | grep passwordauthentication

Output initially showed:
passwordauthentication yes

Identified override in: 
/etc/ssh/sshd_config.d/50-cloud-init.conf

Modified cloud-init configuration to:
PasswordAuthentication no

Restarted SSH:
sudo systemctl restart ssh

Validated effective configuration: 
sudo sshd -T | grep passwordauthentication

Confirmed:
passwordauthentication no

Validation Test
Forced password authentication attempt:
ssh -o PreferredAuthentications=password user@server-ip

Confirmed failure:
Permission denied (publickey).



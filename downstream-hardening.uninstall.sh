#!/usr/bin/bash

# To be incorporated in the spec file
# This file is for testing only

# The following revokes the changes of "downstream-hardening.install.sh".
# It does not delete "all entries" but "all customizations":
# it will re-create the defaults / default entries
semanage login --deleteall

# The following revokes the changes of "downstream-hardening.install.sh"
# with regards to open/closed ports
rm -f /etc/firewalld/zones/*.hardened.xml
rename .xml.old0 .xml /etc/firewalld/zones/*.xml.old0
firewall-cmd --reload

# The following revokes the changes of "downstream-hardening.install.sh"
# with regards to the SELinux boolean that blocks ptrace redundantly
# with YAMA
setsebool -P deny_ptrace off

# Removing files, disabling systemd path
# Some of the below will take effect only after rebooting!
systemctl disable unconfinehomeusers.path
rm -f /usr/bin/unconfinehomeusers.py
rm -f /usr/lib/systemd/system/unconfinehomeusers.path
rm -f /usr/lib/systemd/system/unconfinehomeusers.service
rm -f /usr/lib/sysctl.d/99-kernel-hardening.conf

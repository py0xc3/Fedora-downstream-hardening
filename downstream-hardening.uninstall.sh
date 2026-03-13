#!/usr/bin/bash

# This has been obsoleted by the file "harden"

"""
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
# Disable unconfinehomeusers.path: the path+service files remain available
# and can be re-activated/re-enabled as long as the package is installed
systemctl disable unconfinehomeusers.path
# Remove the harden state to indicate future invocations harden is deactivated
rm -fr /etc/harden
"""

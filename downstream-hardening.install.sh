#!/usr/bin/bash

# To be incorporated in the spec file
# This file is for testing only

# The following is to ensure that root remains unconfined_u, which should be a default,
# but given the potential impact, this needs to be ensured:
# the two commands cannot impact if root is already set unconfined_u
semanage login -a -s unconfined_u root
semanage login -m -s unconfined_u root

# The following ensures that accounts that are not explicitly excluded
# from confinement will be given minimal privileges and confined as user_u by SELinux
semanage login -m -s user_u -r s0 __default__

# This is to remove open ports, which are usually not necessary for desktop/workstation
# use cases. This aims to keep other and default parameter of different OS, editions,
# spins, variants, etc. in place and make it possible to re-establish the previous
# port configuration of the very OS edition/spin/variant later.
# Do not use "--reset-to-defaults" because this is leads to a general default of
# firewalld and not the default of the very OS edition/spin/variant.
sed -i.old0 '/port port/d' /etc/firewalld/zones/*.xml
rename .xml .hardened.xml /etc/firewalld/zones/*.xml
firewall-cmd --reload

# This adds a mostly redundant security layer to "kernel.yama.ptrace_scope"
# (see "99-downstream-hardening"): this will likely break applications
# like "gdb" or "strace" given their need for ptrace for obvious reasons:
# it can allow processes to access data of other processes, which leads
# to several use cases of ptrace in hostile exploitation (e.g., to
# access secrets / credentials stored in other processes memory, which during
# runtime is not encrypted, even if the disk is encrypted)
setsebool -P deny_ptrace on

# Bringing files in place, enabling systemd path, running once the py
cp 99-kernel-hardening.conf /usr/lib/sysctl.d/
# Remove .py (?)
cp unconfinehomeusers.py /usr/bin/
chmod u+rx /usr/bin/unconfinehomeusers.py
chmod go-wx /usr/bin/unconfinehomeusers.py
cp unconfinehomeusers.path /usr/lib/systemd/system
cp unconfinehomeusers.service /usr/lib/systemd/system
systemctl enable --now unconfinehomeusers.path
chown root /usr/bin/unconfinehomeusers.py
chgrp root /usr/bin/unconfinehomeusers.py
chown root /usr/lib/systemd/system/unconfinehomeusers.path
chgrp root /usr/lib/systemd/system/unconfinehomeusers.path
chown root /usr/lib/systemd/system/unconfinehomeusers.service
chgrp root /usr/lib/systemd/system/unconfinehomeusers.service
chown root /usr/lib/sysctl.d/99-kernel-hardening.conf
chgrp root /usr/lib/sysctl.d/99-kernel-hardening.conf
python3 /usr/bin/unconfinehomeusers.py


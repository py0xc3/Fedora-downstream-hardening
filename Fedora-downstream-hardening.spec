Name:       Fedora-downstream-hardening
Version:    0.3
Release:    %autorelease
Summary:    Security-hardening for Fedora and its downstream distributions in workstation and desktop use cases
BuildArch:  noarch
License:    GPL-2.0-or-later
URL:        https://github.com/py0xc3/Fedora-downstream-hardening/
Source0:    %{name}-%{version}.tar.gz

Requires:    python3
Requires:    policycoreutils-python-utils
Requires:    firewalld
Requires:    bash
Requires:    sed

# If the package name changes, two lines in "harden" and one line in
# "harden-selftest" must be adjusted. Read the comments in the two files!
# Also adjust the paths in all files that contain the package name!

# THIS SPEC FILE IS TO BE OPTIMIZED AND MOVED TO A DIFFERENT REPOSITORY!
# IT IS IN THE SOURCE REPO ONLY FOR TESTING PURPOSES!

# The SECURITY.md should be adjusted upon release 1.0 and/or upon
# integration in Fedora / EPEL.

%description
Self-updating security hardening through more restrictive kernel
parameter, SELinux settings, SELinux Confined Users (only deployed to
non-GUI user accounts!) and other means, applicable to Fedora and its
downstream distributions. Despite a strong emphasis on guaranteeing
confidentiality and integrity, this package aims to provide a good
compromise for the majority of use cases and aims to avoid means that
break tools or means of average use cases, but it can break tools or
use cases that use functions that can be exploited maliciously
(e.g., gdb or strace are likely to be broken by the imposed
`kernel.yama.ptrace_scope=2` parameter and an SELinux boolean likewise).
This package is tailored to desktop and workstation use cases.
The term "hardening" is defined in a special way and more a change in
the system's "approach to compromises" rather than a traditional
hardening: See the README.md of the source for details.

%prep
%autosetup

%build
#not applicable

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_pkgdocdir}

install -p -m 0644 -D -T unconfinehomeusers.path %{buildroot}/%{_unitdir}/unconfinehomeusers.path
install -p -m 0644 -D -T unconfinehomeusers.service %{buildroot}/%{_unitdir}/unconfinehomeusers.service
install -p -m 0644 -D -T hardenupdate.path %{buildroot}/%{_unitdir}/hardenupdate.path
install -p -m 0644 -D -T hardenupdate.service %{buildroot}/%{_unitdir}/hardenupdate.service
install -p -m 0644 -D -T 99-kernel-hardening.conf %{buildroot}/%{_pkgdocdir}/99-kernel-hardening.conf
install -p -m 0755 -D -T unconfinehomeusers %{buildroot}/%{_bindir}/unconfinehomeusers
install -p -m 0755 -D -T harden %{buildroot}/%{_bindir}/harden
install -p -m 0755 -D -T harden-selftest %{buildroot}/%{_bindir}/harden-selftest

%files
%license LICENSE
%{_unitdir}/unconfinehomeusers.path
%{_unitdir}/unconfinehomeusers.service
%{_unitdir}/hardenupdate.path
%{_unitdir}/hardenupdate.service
%{_pkgdocdir}/99-kernel-hardening.conf
%{_bindir}/unconfinehomeusers
%{_bindir}/harden
%{_bindir}/harden-selftest

%changelog
%autochangelog

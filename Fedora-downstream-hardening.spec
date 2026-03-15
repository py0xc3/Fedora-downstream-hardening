Name:       Fedora-downstream-hardening
Version:    0.1
Release:    %autorelease
Summary:    Security-hardening for Fedora and its downstream distributions in workstation and desktop use cases
BuildArch:  noarch
License:    MIT
URL:        https://github.com/py0xc3/Fedora-downstream-hardening/
Source0:    %{name}-%{version}.tar.gz

Requires:    python3
Requires:    policycoreutils-python-utils
Requires:    firewalld
Requires:    bash
Requires:    sed

# If the package name changes, adjust the file name for "/etc/dnf/protected.d/Fedora-downstream-hardening.conf" in "harden" to contain the updated name

# THIS SPEC FILE IS NOT YET SUFFICIENTLY TESTED, TAILORED TO TEST PURPOSES ONLY AND NOT YET FINISHED BUT JUST A ROUGH ACCUMULATION OF THE LINES THAT MIGHT MAKE SENSE IN CONJUNCTION WITH THE OTHER FILES AND SCRIPTS

%description
Security hardening through more restrictive kernel parameter, SELinux settings,
SELinux Confined Users (only deployed to non-GUI user accounts!) and other means,
applicable to Fedora and its downstream distributions. Despite a strong emphasis
on guaranteeing confidentiality and integrity, this package aims to provide a
good compromise for the majority of use cases and aims to avoid means that break
tools or use cases, but it can break tools or use cases that use functions that
can be exploited maliciously (e.g., gdb or strace are likely to be broken by
the imposed `kernel.yama.ptrace_scope=2` parameter and an SELinux boolean
likewise). This package is tailored to desktop and workstation use cases.

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

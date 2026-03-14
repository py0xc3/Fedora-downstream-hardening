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

# If the package name changes, adjust the file name for "/etc/dnf/protected.d/Fedora-downstream-hardening.conf" in "harden" to contain the updated name

# THIS SPEC FILE IS NOT YET TESTED AND NOT YET FINISHED BUT JUST A ROUGH ACCUMULATION OF THE LINES THAT MIGHT MAKE SENSE IN CONJUNCTION WITH THE OTHER FILES AND SCRIPTS

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

install -D -m 0644 unconfinehomeusers.path %{buildroot}/%{_unitdir}/unconfinehomeusers.path
install -D -m 0644 unconfinehomeusers.service %{buildroot}/%{_unitdir}/unconfinehomeusers.service
install -D -m 0644 hardenupdate.path %{buildroot}/%{_unitdir}/hardenupdate.path
install -D -m 0644 hardenupdate.service %{buildroot}/%{_unitdir}/hardenupdate.service
install -D -m 0644 99-kernel-hardening.conf %{buildroot}/%{_pkgdocdir}/99-kernel-hardening.conf
install -D -m 0755 unconfinehomeusers %{buildroot}/%{_bindir}/unconfinehomeusers
install -D -m 0755 harden %{buildroot}/%{_bindir}/harden

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}
%{_pkgdocdir}/%{name}


%changelog
%autochangelog

Name:     Fedora-downstream-hardening
Version:  0.1
Release:  %autorelease
Summary:  Security-hardening for Fedora and its downstream distributions in workstation and desktop use cases
License:  MIT
URL:      https://github.com/py0xc3/Fedora-downstream-hardening/
Source:

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

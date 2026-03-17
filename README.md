# Fedora-downstream-hardening
Desktop/Workstation hardening for Fedora and its downstream distributions (CentOS Stream, AlmaLinux, RockyLinux).

Version 0.2 implements all functions and selftests immediately necessary for Fedora-downstream hardening. It has been tested and works out fine, but it is not yet recommended to use this tool in a production environment! More testing is necessary!

Tests have been done with Fedora KDE 43 and CentOS Stream 10 KDE.

Full PEP 8 compliance to be implemented later. Files are intentionally written/kept as simple as possible, not emphasizing code efficiency or so (at the best, sufficiently understandable by everyone with general understanding of working with the command line and general understanding of IF/ELSE and other clauses from spreadsheets or so).

Suggested versioning:

\<major release\>.\<minor release\>

-> major release: new security functions added -> it is not possible to always prove that this does not break anything in any context. Therefore, it needs to be obvious in the versioning. Also, it can in some cases be that Fedora enables functions that are not yet existing or not yet useful downstream: so at the worst, two major releases with each its own minor releases are temporarily necessary.

-> minor releases: bug fixes, improving comments/text, disabling security functions (obsoleted or replaced or broken etc.)

-> releases that apply not to all downstream (fedora, centos, alma, rocky) might be marked additionally with "f","c","a","r": e.g., "2.5f" and "1.8car"

-> 0.n implies no full release yet (= not yet eligible for production)

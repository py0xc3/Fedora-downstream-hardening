# Fedora-downstream-hardening
Desktop/Workstation hardening for Fedora and its downstream distributions (CentOS Stream, AlmaLinux, RockyLinux).

This tool aims to harden most private and professional real world desktop/workstation use cases that have different needs than traditional hardening: the sudo user and the major user of the system are equal, and all value of the system is within their one user account. Having access to the data of that user account and its processes makes further protection of the system obsolete: the binaries can be donwloaded freely anyway :) At the same time, origins of attacks are likely to also rise directly/indirectly from this one account. Still, the User Experience of average use cases shall not be broken: a denial of service can be as dangerous as some attacks.

Therefore, the major goal shifts from protecting the system from its accounts to protecting the GUI-using accounts from everything else of the system (e.g., to add protection against half-administrated half-understood services/processes the user deployed intentionally or by accident), and to protect processes within the GUI-using accounts from each along with their data.

The hardening tool aims to be usable by all audiences, including beginners: it can be deployed "fire and forget" and is self-updating its hardening.

Communities have to find compromises for many user groups / audiences, and some of the compromises can lead to outcomes that are disadvantageous for some of the user groups: this hardening tool narrows the interests that are considered (emphasizing major desktop/workstation use cases and also user groups who might not be able to identify optimal compromises for themselves) in order to achieve predictability of the system (short term and long term). This is less a shift from "UX first" to "Security first", but more a shift from "deploy the least common denominator by default" to "emphasize the majority and otherwise let it break so that I know and can decide myself which compromise I prefer": the focus is that average use cases are not broken and always working by default (browser, email, desktop/GUI, office, etc.), and average users should not be bothered with broken processes/tools. A major compromise at the moment is that the hardening tool breaks tools like `gdb` or `strace` because the ptrace they use can be also used by processes to steal data from other processes (e.g., a manually installed untrusted application could steal credentials stored in the browser's memory during runtime): the hardening tool assumes that developers who deploy this tool would be able to identify the issue and solve it by finding a tailored compromise for themselves.

With this in mind, the files of the tool contain many comments that sufficiently detail what happens where and allow users to modify contents if they want (e.g., disable the lines that break `gdb` or `strace`), and if preferred, allow to just deploy some files or lines manually to fit their personal compromises.

----------

Version 0.2 implements all functions and selftests immediately necessary for Fedora-downstream hardening. It has been tested and works out fine, but it is **not yet recommended to use this tool in a production environment!** More testing is necessary!

Tests have been done with Fedora KDE 43 and CentOS Stream 10 KDE.

Full PEP 8 compliance to be implemented later. Files are intentionally written/kept as simple as possible, not emphasizing code efficiency or so (at the best, sufficiently understandable by everyone with general understanding of working with the command line and general understanding of IF/ELSE and clauses known from spreadsheets). This tool aims to not break the review/testing guarantees created in the development process of the OS.

Suggested versioning:

\<major release\>.\<minor release\>

-> major release: new security functions added -> it is not possible to always prove that this does not break anything in any context. Therefore, it needs to be obvious in the versioning. Also, it can in some cases be that Fedora enables functions that are not yet existing or not yet useful downstream: so at the worst, two major releases with each its own minor releases are temporarily necessary.

-> minor releases: bug fixes, improving comments/text, disabling security functions (obsoleted or replaced or broken etc.)

-> releases that apply not to all downstream (fedora, centos, alma, rocky) might be marked additionally with "f","c","a","r": e.g., "2.5f" and "1.8car"

-> 0.n implies no full release yet (= not yet eligible for production)

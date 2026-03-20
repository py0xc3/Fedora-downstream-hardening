# Fedora-downstream-hardening
Desktop/Workstation hardening for Fedora and its downstream distributions (CentOS Stream, AlmaLinux, RockyLinux).

### Goals and background of the tool

This tool aims to harden (and achieve predictability in) average private and professional real world desktop/workstation use cases that have different needs than traditional hardening: the sudo user and the major user of the system are equal, and all value of the system is within their one user account. Having access to the data of that user account and its processes makes further protection of the system obsolete: the binaries can be donwloaded freely anyway :) At the same time, origins of attacks are likely to also rise directly/indirectly from this one account. Sudo rights might not always be used by a trained admin. Still, the User Experience of average use cases shall not be broken: a denial of service can be as dangerous as some attacks.

Therefore, the major goal shifts from protecting the system from its accounts to protecting the GUI-using accounts from everything else of the system (e.g., to add protection against half-administrated half-understood services/processes the user deployed intentionally or by accident), and to protect processes within the GUI-using accounts from each along with their data. The goal includes protecting stored data (not equal to the memory of processes) within the accounts from processes that should not have access to it (regarding the latter, the default of Fedora & downstream, if properly setup, facilitate already most that can be done; more improvements for this are planned for the future, but wome of these means will be restricted to flatpak-users).

From some perspective, **it's not hardening but changing the system's "approach to compromises"** towards a "harder" one that might create more "predictable" outcomes for "average desktop/workstation audiences/use cases": from "deploy the least common denominator by default" to "emphasize the majority and otherwise let it break so that the user knows and can decide themselves which compromise they prefer". Average users should not end up with making decisions about compromises though: they shall be covered by the average use cases that are facilitated without issues anyway. It can be also said this tool just narrows the interests considered in the compromises and emphasizes major-use-case-audiences and audiences who cannot make optimal compromises (short and long term) for themselves (the latter audience is usually covered by the first), which also allows a more explicit security model and hardening as far as it does not break these user experiences. 

The hardening tool is self-updating its hardenings as long as the rpm from which it is installed is updated as well (e.g., through the normal daily updates with `dnf`): if the community has to make changes in its "deploy the least common denominator by default" compromises, the tool can adjust its "hardened" systems adaptively and automatically in parallel towards the above mentioned compromise approach: no user interaction necessary. Communities have to find compromises that fit for many user groups / audiences, and some of the compromises can lead to outcomes that are disadvantageous for some of the user groups but are a demand for another: the tool keeps the users' systems focused, mitigating conflicts that can have perceived or hidden impacts.

The hardening tool aims to be usable by all audiences, including beginners: it can be deployed "fire and forget" and is self-updating its hardening. Installation is easy: install the tool + run one copy/paste command to activate the tool (and another copy/paste command to test it, and another to deactivate it).

### Excluded/unconsidered use cases

The focus is that average use cases do not break and always work by default (browser, email, desktop/GUI, office, etc.), and average users should not be bothered with broken processes/tools. Yet, some tools that are not deployed by the average user / majority and that can cause trouble to others might be broken: so far, the hardening tool breaks software development tools like `gdb` or `strace` because the ptrace they use can be also used by processes to steal data from other processes (e.g., a manually installed untrusted application could steal credentials used in the browser, stored unencrypted in it's memory during runtime, even if otherwise encrypted on disk): the hardening tool assumes that software developers who deploy this tool would be able to identify the issue and solve it by finding a tailored compromise for themselves.

With this in mind, the files of the tool contain many comments that sufficiently detail what happens where and allow more advanced users to modify contents if they want (e.g., disable the lines that break `gdb` or `strace`), and if preferred, allow to just deploy some files or lines manually to fit their personal compromises.

### How to use the tool

Once available as package on Fedora and EPEL, the tool can be installed with `dnf install fedora-downstream-hardening`: keep in mind that CentOS Stream, Rocky, Alma might need you to enable EPEL manually in advance if you have not already done so. The tool will **not** be active or harden anything just by installing it with dnf!

But once installed, you can do `harden activate`: if the output then says the hardening worked out, your system is hardened **once you rebooted**. It is suggested to run the selftest **after rebooting** in order to verify the hardening has worked out: `harden selftest`. If this leads to an error output, please read the instructions of the error output and follow them properly: you can open a ticket about this here.

In order to ensure that active hardenings are properly updated, the package `fedora-downstream-hardening` will be protected from removing as long as the hardening is active.

To remove the hardening and the package again, you need to do the following two commands in this very order: first, `harden deactivate` and then `dnf remove fedora-downstream-hardening`: after rebooting, your system is back to the earlier defaults.

Keep in mind that the name of the tool might change before its release!

### Versioning, to do, current testing!

Version 0.2 implements all functions and selftests immediately necessary for Fedora-downstream hardening. It has been tested and works out fine, but it is **not yet recommended to use this tool in a production environment!** More testing is necessary!

Tests have been done with Fedora KDE 43 and CentOS Stream 10 KDE.

Full PEP 8 compliance to be implemented later. Files are intentionally written/kept as simple as possible, not emphasizing code efficiency or so (at the best, sufficiently understandable by everyone with general understanding of working with the command line and general understanding of IF/ELSE and clauses known from spreadsheets). This tool aims to not break the review/testing guarantees created in the development process of the OS.

Suggested versioning:

\<major release\>.\<minor release\>

-> major release: new security functions added -> it is not possible to always prove that this does not break anything in any context. Therefore, it needs to be obvious in the versioning. Also, it can in some cases be that Fedora enables functions that are not yet existing or not yet useful downstream: so at the worst, two major releases with each its own minor releases are temporarily necessary.

-> minor releases: bug fixes, improving comments/text, disabling security functions (obsoleted or replaced or broken etc.)

-> releases that apply not to all downstream (fedora, centos, alma, rocky) might be marked additionally with "f","c","a","r": e.g., "2.5f" and "1.8car"

-> 0.n implies no full release yet (= not yet eligible for production)

Name:           oocrc32
Version:        0.1.0
Release:        1%{?dist}
Summary:        Cyclic redundancy check generator utilizing hardware carry-less multiplication.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocrc32
Source0:        oocrc32-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocrc32 is a sovereign, capability-bounded CRC32 CHECKSUM written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocrc32
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocrc32-uninstall

%files
/usr/bin/oocrc32
/usr/bin/oocrc32-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding

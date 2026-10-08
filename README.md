# oocrc32: Sovereign CRC32 Checksum & Verification Engine

<div align="center">

```
================================================================================
                                 oocrc32
               Sovereign openOODA CRC32 Checksum Engine
================================================================================
```

**Sovereign CRC32 Checksum Engine**  
*Cyclic redundancy check generator utilizing multi-polynomial evaluation, manifest verification, and streaming MCP.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Streaming MCP stdio for AI agents  
Written in 100% pure native [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocrc32/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocrc32-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocrc32/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocrc32/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocrc32-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocrc32/uninstall.sh | bash
```

---

## 2. CLI Usage

```
Usage: oocrc32 [OPTIONS] [FILE]...

Cyclic redundancy check generator utilizing hardware carry-less multiplication.

Options:
  -a, --algorithm <NAME>   Polynomial algorithm: ieee (default), castagnoli/crc32c, koopman
  -C, --crc32c             Shortcut for --algorithm castagnoli
  -c, --check [FILE]       Read checksums from manifest FILE and verify them
      --verify <HASH>      Verify input data against expected hex checksum
  -u, --upper              Format hexadecimal checksum in uppercase
  -r, --raw                Output raw decimal unsigned 32-bit integer
  -q, --quiet              Do not print OK for each successfully verified file
  -d, --demo               Run synthetic RFC 3720 test vector and benchmark suite
  -j, --json               Output structured JSON
      --theme <THEME>      Select terminal color theme (ember, ocean, matrix, cyber, monochrome)
      --mcp                Run streaming MCP JSON-RPC 2.0 server on stdio
  -h, --help               Show this help message and exit
  -v, --version            Show version information and exit
```

---

## 3. Supported Polynomials

* **IEEE 802.3 (`0xEDB88320`):** Canonical standard used in Ethernet, gzip, zip, PNG, and POSIX `cksum`.
* **Castagnoli / CRC-32C (`0x82F63B78`):** Optimal error detection in iSCSI (RFC 3720), Btrfs, ext4, SCTP, and NVMe.
* **Koopman / CRC-32K (`0xEB31D82E`):** Optimal HD=6 detection for payloads under 2048 bits.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocrc32` runs a JSON-RPC 2.0 stdio server providing five sovereign checksum tools:

* `crc32_calculate`: Compute CRC32 checksum of string data or disk file.
* `crc32_verify`: Verify CRC32 checksum against expected hex string.
* `crc32_check_file`: Verify checksums listed in a manifest file or string.
* `crc32_polynomials`: Return specifications of supported CRC32 polynomials.
* `crc32_demo`: Return RFC 3720 and IEEE 802.3 test vectors and benchmark telemetry.

```bash
oocrc32 --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`).
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency compiled openOODA executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

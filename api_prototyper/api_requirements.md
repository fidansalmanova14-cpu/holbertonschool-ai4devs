# API Requirements – Network Device Inventory API

## Domain
IT Infrastructure & Network Operations Management. This API manages the lifecycle of physical and virtual network assets.

## Target Users
- **Network Engineers:** To register and track hardware configurations.
- **System Administrators:** To monitor device status and security compliance.
- **IT Managers:** To generate inventory and lifecycle reports.

## Core Operations (10 total)
1. **Create Device:** Register a new network asset.
2. **Get All Devices:** List all devices with pagination support.
3. **Get Device by ID:** Retrieve full metadata for a specific device.
4. **Update Device Details:** Modify general info (location, description).
5. **Delete Device:** Securely remove a device from the active inventory.
6. **Update Firmware Version:** Log firmware upgrades and history.
7. **Search by IP:** Query devices using IPv4 or IPv6 addresses.
8. **Get Devices by Category:** Filter assets by type (Router, Switch, etc.).
9. **Assign Technician:** Assign a responsible person for device maintenance.
10. **Get Audit Logs:** View a history of changes for a specific device.

## Data Validation Rules
- **Hostname:** Must be unique, 3-50 characters, no special characters except hyphens.
- **IP Address:** Must strictly follow IPv4 (e.g., 192.168.1.1) or IPv6 format.
- **MAC Address:** Must be a valid 48-bit hex string (XX:XX:XX:XX:XX:XX).
- **Status:** Limited to specific enums: `online`, `offline`, `maintenance`, `decommissioned`.
- **Serial Number:** Mandatory field, must be alphanumeric and unique.
- **Price:** If provided, must be a positive decimal value.

## Non-Functional Requirements
- **Latency:** 95% of GET requests must respond in less than 200ms.
- **Availability:** The API must maintain 99.9% uptime.
- **Authentication:** Mandatory JWT (JSON Web Token) via the Authorization header.
- **Rate Limiting:** Maximum of 100 requests per minute per authenticated user.
- **Security:** Use HTTPS (TLS 1.2+) for all data transmissions.
- **Scalability:** System must support up to 10,000 device records without performance loss.
- **Logging:** All failed authentication attempts must be logged for security audits.

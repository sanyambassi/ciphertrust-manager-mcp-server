# Example Prompts for CipherTrust MCP Server

This document provides example prompts you can use with AI assistants (like Cursor or Claude Desktop) to interact with the CipherTrust MCP server. Just type these prompts to the assistant, and it will translate them into the correct tool calls for you.

---

## User Management

- **List all users**
  > List all users in domain "finance".

- **Get details for a specific user**
  > Get details for user "bob".

---

## System Information

- **Get system information**
  > Show system information.

- **Check CipherTrust Manager version**
  > What is the version of CipherTrust Manager?

---

## Key Management

- **List all keys**
  > List all keys.

- **Create a new AES key named "test-key"**
  > Create a new AES key named "test-key".

- **Delete a key**
  > Delete the key named "old-key".

---

## Tips for Best Results

- Be specific for best results (e.g., "List users with email containing 'example.com'").
- You can ask for lists, details, creation, or deletion of resources.
- If you get an error, check the tool documentation or ask the assistant for help.

---

## Advanced Examples

- **List users with a filter**
  > List users whose email contains "admin".

- **Show all available tools**
  > What tools are available?

---

## Domain Operations

- **List all domains**
  > List all domains.

- **Switch to domain "finance"**
  > Switch to the domain named "finance".

- **Create a new AES key named "payroll-key" in domain "hr"**
  > Create a new AES key named "payroll-key" in the "hr" domain.

- **List all users in domain "engineering"**
  > List all users in the "engineering" domain.

---

## CTE (CipherTrust Transparent Encryption) Operations

- **List all CTE client groups**
  > List all CTE client groups.

- **Create a new CTE client group named "prod-servers"**
  > Create a new CTE client group named "prod-servers".

- **Add client "web01" to CTE client group "prod-servers"**
  > Add client "web01" to the CTE client group "prod-servers".

- **List all guardpoints for client group "prod-servers"**
  > List all guardpoints for the CTE client group "prod-servers".

- **Create a guardpoint on path "/data/secure" for client group "prod-servers"**
  > Create a guardpoint on "/data/secure" for the CTE client group "prod-servers".

- **Rotate the key used by guardpoint "/data/secure"**
  > Rotate the key used by the guardpoint on "/data/secure".

- **List all CTE clients"**
  > List all CTE clients in the connected domain.

- **Create a guardpoint on CTE client win-client with policy policy-name at localtion C:\SensitiveData"**
  > Add guardpoint on CTE client win-client.

- **Create an LDT CTE policy with name ldt-pol-01. Userset user-set-01 should have full access (all_ops, apply_key). Use clear_key as the current key and LDTKey01 as the transoformation key"**
  > Create a CTE LDT policy with userset user-set-01 with full access. 
---

## Service and Maintenance Operations

- **Forcefully restart the web service**
  > Forcefully restart the web service.

- **Restart all services**
  > Restart all services.

- **Check the status of the NTP service**
  > Check the status of the NTP service.

---

## Key Lifecycle and Compliance

- **Rotate key "customer-data-key" in domain "prod"**
  > Rotate the key named "customer-data-key" in the "prod" domain.

- **Generate a key compliance report for all active keys**
  > Generate a key compliance report for all active keys.

- **Show the rotation history for key "test-key"**
  > Show the rotation history for the key named "test-key".

- **List all keys that have not been rotated in the last 90 days**
  > List all keys that have not been rotated in the last 90 days.

---

## Creative & Advanced Scenarios

- **Find all CTE clients with errors in the "finance" domain**
  > List all CTE clients with errors in the "finance" domain.

- **Pause LDT (Live Data Transformation) for client group "analytics"**
  > Pause LDT for the client group "analytics".

- **Enable ransomware protection for guardpoint "/shared/data"**
  > Enable ransomware protection for the guardpoint on "/shared/data".
---
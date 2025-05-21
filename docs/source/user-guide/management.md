# User Management

This guide explains how to manage users in the AI-Guard system, including user roles, enrollment status, and access management.

## User Types

AI-Guard manages two different types of users:

### System Users

These are the operators who use the AI-Guard system itself:

- **Administrators**: Have full system access and configuration rights
- **Enrollment Operators**: Can register new individuals in the system
- **Security Guards**: Monitor recognition feeds and respond to alerts

### Enrolled Individuals

These are the people registered in the face recognition database:

- **Authorized Personnel**: Employees, students, or staff with access permission
- **Temporary Visitors**: Guests with limited-time access
- **Restricted Access**: Individuals with access to specific areas only

## Current User Management

In the current proof-of-concept version, user management is handled through data files in a simplified manner:

### System User Management

System users are defined in a configuration file:

```python
# Example system_users.json file
{
  "users": [
    {
      "username": "admin",
      "full_name": "System Administrator",
      "role": "admin",
      "email": "admin@example.com"
    },
    {
      "username": "enroller1",
      "full_name": "Enrollment Operator",
      "role": "enroller",
      "email": "enroller@example.com"
    },
    {
      "username": "guard1",
      "full_name": "Security Guard",
      "role": "guard",
      "email": "guard@example.com"
    }
  ]
}
```

### Enrolled Individuals Management

Enrolled individuals are stored in a database file:

```python
# Example enrolled_individuals.json structure
{
  "individuals": [
    {
      "id": "001",
      "full_name": "John Doe",
      "department": "IT",
      "access_level": "full",
      "enrollment_date": "2023-09-15",
      "status": "active",
      "embeddings_file": "data/embeddings/001_john_doe.pkl"
    },
    {
      "id": "002",
      "full_name": "Jane Smith",
      "department": "HR",
      "access_level": "standard",
      "enrollment_date": "2023-09-16",
      "status": "active",
      "embeddings_file": "data/embeddings/002_jane_smith.pkl"
    }
  ]
}
```

## Managing System Users

In the current implementation, system users are managed directly by editing the configuration files. In future releases, a web-based administration interface will be available.

### Adding a System User

1. Open the `system_users.json` file
2. Add a new user entry with the required fields
3. Save the file
4. Restart the AI-Guard system to apply changes

### Modifying User Roles

1. Open the `system_users.json` file
2. Locate the user entry to modify
3. Change the `role` field to the appropriate value:
   - `admin`
   - `enroller`
   - `guard`
4. Save the file
5. Restart the AI-Guard system to apply changes

### Deactivating a System User

1. Open the `system_users.json` file
2. Locate the user entry to deactivate
3. Add the field `"status": "inactive"` to the user entry
4. Save the file
5. Restart the AI-Guard system to apply changes

## Managing Enrolled Individuals

### Adding an Individual

New individuals are added through the [Face Enrollment](enrollment.md) process, which:

1. Captures face images from multiple angles
2. Processes the images to generate embeddings
3. Creates a new entry in the enrolled individuals database
4. Saves the embeddings to the specified location

### Viewing Enrolled Individuals

To view all enrolled individuals:

```bash
# Using the provided utility script
python scripts/list_enrolled.py

# Output example:
ID    | Name        | Department | Status | Enrollment Date
------|-------------|------------|--------|----------------
001   | John Doe    | IT         | Active | 2023-09-15
002   | Jane Smith  | HR         | Active | 2023-09-16
```

### Updating Enrollment Information

To update an individual's metadata:

1. Locate the individual's entry in `enrolled_individuals.json`
2. Modify the appropriate fields
3. Save the file

### Updating Face Embeddings

To update an individual's face data, you'll need to re-enroll them:

1. Launch the enrollment notebook
2. Select the "Update Existing Enrollment" option
3. Enter the individual's ID or name
4. Complete the enrollment process as with a new user

### Deactivating an Individual

To deactivate an individual (revoke their access):

1. Locate the individual's entry in `enrolled_individuals.json`
2. Change the `status` field from `active` to `inactive`
3. Save the file

## Access Levels

AI-Guard supports different access levels for enrolled individuals:

- **Full Access**: Access to all areas
- **Standard Access**: Access to common areas only
- **Restricted Access**: Access limited to specific areas
- **Temporary Access**: Time-limited access for visitors

### Setting Access Levels

Access levels are set during enrollment or can be updated later:

1. Open the `enrolled_individuals.json` file
2. Locate the individual's entry
3. Set the `access_level` field to the appropriate value
4. Save the file

## Planned User Management Features

The following features are planned for future releases:

### Web-Based Administration Interface

A comprehensive web interface for managing:
- System users and their roles
- Enrolled individuals and their access levels
- Access control policies and rules
- System configuration

### Role-Based Access Control

Enhanced role definitions with granular permissions:
- Custom role creation
- Permission assignment
- Multi-factor authentication
- Access logs and audit trails

### Integration with HR Systems

Automated user management through integration with:
- HR databases
- Student information systems
- Visitor management systems
- Physical access control systems

## Best Practices

### Security Recommendations

- **Principle of Least Privilege**: Assign only necessary permissions to users
- **Regular Audits**: Review user accounts and access levels periodically
- **Strong Authentication**: Implement multi-factor authentication for system users
- **Enrollment Verification**: Verify identity before enrollment

### Operational Recommendations

- **User Documentation**: Maintain thorough records of all enrolled individuals
- **Regular Updates**: Update face embeddings periodically for better recognition
- **Deactivation Process**: Establish clear procedures for removing access
- **Privacy Protection**: Store only necessary personal information

## Troubleshooting

### Common Issues

1. **User Cannot Log In**
   - Verify the user exists in `system_users.json`
   - Check that the user status is `active`
   - Confirm the role assignment is correct

2. **Individual Not Recognized**
   - Verify the individual is in `enrolled_individuals.json`
   - Check that their status is `active`
   - Ensure their embeddings file exists
   - Consider re-enrolling with better quality images

3. **Access Level Issues**
   - Verify the access level is correctly set
   - Check the access control configuration
   - Restart the system to apply recent changes

## Next Steps

- [Face Enrollment Guide](enrollment.md) - Learn how to enroll new individuals
- [System Configuration](../getting-started/configuration.md) - Configure user management settings
- [Technical Documentation](../technical/index.md) - Understand system architecture
Service Request Management - Odoo Module
A feature-rich Service Request Management module for Odoo that allows tracking, assigning, and monitoring service requests like repairs, installations, and complaints. Includes a dynamic dashboard for quick status overviews.

![Screenshot from 2025-06-28 23-42-12](https://github.com/user-attachments/assets/d752927c-1ba0-490e-acf6-f052ba9301a8)

🔧 Features!

Auto-generated Request Numbers

Trackable service request lifecycle (draft, assigned, in progress, done, cancelled)

Assign responsible users with validation

Priority classification (low, medium, high)

Email notification on assignment

Access control on deletion (only allowed in draft or cancelled states)

Integrated Chatter Support

Interactive Dashboard for request status monitoring

![Screenshot from 2025-06-28 23-41-22](https://github.com/user-attachments/assets/41ccac2f-0a18-4f42-a172-fe5cca8a45fe)

📬 Email Notification

When a request state is changed to Assigned, an email is sent to the assigned user using a QWeb template (email_template_service_request_assignment) if defined. A message is also posted in the chatter.

![Screenshot from 2025-06-28 23-41-38](https://github.com/user-attachments/assets/bae7a92d-f322-40c5-9b0d-288128a2ef9e)

🚫 Access Restriction
Only requests in Draft or Cancelled states can be deleted. This prevents accidental deletion of active/in-progress service records.


![Screenshot from 2025-06-28 23-42-38](https://github.com/user-attachments/assets/79186f9d-0d78-450e-ab8e-ef0bf4830b57)

📊 Request Status Dashboard

This module includes a custom Dashboard that gives a quick overview of request counts grouped by their current state.

![Screenshot from 2025-06-28 23-43-03](https://github.com/user-attachments/assets/5e5a1ccf-b321-4e0d-9da0-6746de7f2259)

✅ Dashboard Features

Shows count of requests by each state (e.g., Assigned: 5, Done: 3)

Clickable status cards redirect to filtered tree view

Graceful "no data" message if there are no requests

[Screenshot from 2025-06-28 23-40-46](https://github.com/user-attachments/assets/abfb8da1-f6ff-4c0f-a64b-4e90f59ffb88)

![Screenshot from 2025-06-28 23-41-02](https://github.com/user-attachments/assets/219b703a-83cf-40b4-9e74-d44528d59d9c)

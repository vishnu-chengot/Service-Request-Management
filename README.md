Service Request Management - Odoo Module
A feature-rich Service Request Management module for Odoo that allows tracking, assigning, and monitoring service requests like repairs, installations, and complaints. Includes a dynamic dashboard for quick status overviews.

🔧 Features

Auto-generated Request Numbers

Trackable service request lifecycle (draft, assigned, in progress, done, cancelled)

Assign responsible users with validation

Priority classification (low, medium, high)

Email notification on assignment

Access control on deletion (only allowed in draft or cancelled states)

Integrated Chatter Support

Interactive Dashboard for request status monitoring


📬 Email Notification

When a request state is changed to Assigned, an email is sent to the assigned user using a QWeb template (email_template_service_request_assignment) if defined. A message is also posted in the chatter.


🚫 Access Restriction
Only requests in Draft or Cancelled states can be deleted. This prevents accidental deletion of active/in-progress service records.



📊 Request Status Dashboard

This module includes a custom Dashboard that gives a quick overview of request counts grouped by their current state.

✅ Dashboard Features

Shows count of requests by each state (e.g., Assigned: 5, Done: 3)

Clickable status cards redirect to filtered tree view

Graceful "no data" message if there are no requests

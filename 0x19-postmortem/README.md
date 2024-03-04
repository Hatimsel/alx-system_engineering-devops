Issue Summary:
From 10:34 AM to 1:48 PM GMT, requests to all NurseNetwork APIs resulted in
500 error response messages. The service downtime affected the entire web
application, resulting in slow response times and intermittent errors for
approximately 70% of users. The main cause of this downtime was the improper
use of SQLAlchemy's session management led to database connection leaks, causing
resource exhaustion and performance degradation.

Timeline (all times Greenwich Mean Time):

10:34 AM: The issue was detected when the monitoring system flagged unusually high
database query latencies.
10:35 AM: Pagers alerted teams
10:48 AM: Engineers investigated recent code changes and database configurations
assuming a potential performance bottleneck.
11:05 AM: Misleadingly, focus shifted towards server infrastructure due to initial
diagnostic indications.
12:35 AM: Incident was escalated to the database and application teams.
1:48 PM: The issue was resolved by optimizing SQLAlchemy session management and
introducing connection pooling adjustments.

Root Cause:
Improper session management in SQLAlchemy led to persistent database connections not
being properly released after use, resulting in connection leaks and eventual resource
exhaustion.

Resolution:
The issue was addressed by implementing scoped sessions, configuring connection pooling
parameters, and ensuring explicit session closure after transactional operations within
the Flask application.

Corrective and Preventative Measures:

Improvements/Fixes:
Enhance code review processes to identify and rectify improper SQLAlchemy usage patterns.
Implement automated testing suites to detect and prevent resource leakage and performance
bottlenecks.
Establish comprehensive documentation and training materials on best practices for SQLAlchemy
integration within Flask applications.

Tasks to Address the Issue:
Conduct a thorough audit of SQLAlchemy usage across the application codebase.
Implement automated code analysis tools to identify potential session management issues during
development.
Integrate SQLAlchemy performance monitoring and alerting mechanisms to detect abnormal resource
consumption patterns.
Develop and enforce coding standards and guidelines for proper SQLAlchemy session lifecycle management.

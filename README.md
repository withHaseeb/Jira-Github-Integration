# Jira-Github-Integration
This GitHub project is designed to streamline the process of creating Jira tickets directly from GitHub issues by leveraging the power of automation. The integration is facilitated through a Flask application connected to both GitHub and Jira.

How It Works:
Issue Creation:
Developers and testers can create issues on GitHub to report bugs, request features, or document tasks.

Triggering Jira Ticket Creation:
If a developer or tester wants to create a corresponding Jira ticket, they simply need to add a specific comment under the GitHub issue with the command "create jira".

Flask Application Integration:
A Flask application acts as the intermediary between GitHub and Jira. It monitors comments on GitHub issues for the specified command.

Communication with GitHub:
The Flask application communicates with the GitHub API to detect the "create jira" command in the issue comments.

Automatic Jira Ticket Creation:
Once the command is detected, the Flask application interacts with the Jira API to create a new ticket with relevant details, such as the issue title and description.

Benefits:
Efficiency:
Streamlines the workflow for creating Jira tickets, reducing manual effort and ensuring consistency.

Real-time Integration:
The integration works in real-time, ensuring that Jira tickets are created promptly after the command is added to the GitHub issue.

Enhanced Collaboration:
Developers and testers can seamlessly connect GitHub and Jira, fostering better collaboration between development and project management teams.

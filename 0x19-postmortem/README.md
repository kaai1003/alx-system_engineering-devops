PostMortem



Issue Summary :

Duration of outage : November , 6, 2024 06:00 AM - 07:30 AM (GMT+1).
Impact : All, Automotive Harness, Electrical Test Stations are completely down , leading to a total halt in production lines.
Route Cause: Failure in order generation service after a planned windows server reboot , causing it to stop this service and not restarted automatically .
Timeline :

06:00 AM : Electrical Test station operator complains about an error shown after scanning a new order Harness .
06:05 AM : Initial analysis done by IT Support , by verifying that the Station is connected to the network.
06:20 AM : IT support confirmed that there is no network issue and that the error message indicates that the order file is missing.
06:25 AM : the incident escalated to Test Technology support in order to check the electrical test Server .
06:26 AM : discovered that 100 % of stations are affected.
06:27 AM : investigate the electrical test server in order to identify the issue.
06:35 AM : discovering that the service responsible for Order generation and preparation of order files is not working.
06:35 AM : restart the affected service manually.
06:40 AM : successfully restart Order generation service .
06:45 AM : verified that the service is working as expected.
06:50 AM : verified that electrical test stations are working properly .
07:30 AM : declared that the issue is resolved and all stations are working as expected.

Root cause and resolution:

Route Cause: The primary route cause was that the order generation service can’t start automatically after planned windows server restart or even if the service is stopped accidentally , preventing working stations from receiving harness orders that should be tested.
Resolution : the issue has been resolved simply by starting the service again.

Corrective and preventative measures:

improved/fixed : 

implementation of start-up script that checks if the service is stopped and starts it .
Monitor the service in order to be alerted if the service is stopped.
Create an error message that will help identify the issue easily .

tasks to address the issue:

Check and review the start-up script that will start the service automatically .
Monitor the service in order to prevent any future stoppage.

By addressing these corrective measures, we aim to prevent similar incidents in the future and ensure a more resilient order generation system.

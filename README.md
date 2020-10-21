# Octopus-updates
An update mechanisem for the Octopus

## Project goal
Your goal is to implement a mechanisem for transmitting a database table update to one or more web clients at the same time.

The chain should look like this:

MySQL db table is updated &#10140; a trigger is activated &#10140; python script is launched&#10140; an SSE is sent &#10140; the SSE is received be the web clients &#10140; some control is updated
### Implementation tasks: (Mark completed)
- [ ] Set up a mysql database - Local (with MySQL community edition) or remote on some host (Heroku/pythonanywhere)
- [ ] Create some simple db table
- [ ] Set up a simple web sever with the FLASK python framework - Local or remote
- [ ] Server sends a simple HTML with a table representing the table you created
- [ ] Whenever the db table is updated the mechanisem will transmit the changes to the HTML table

### Requirements:
 - Python
 - Flask framework
 - MySQL db
 - SSE (Server Sent Events)
 - Transmitted data format will be JSON

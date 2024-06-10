import yagmail

def send_update_email(username):

  yag = yagmail.SMTP('corieleclair@leclairfoundation.org', 'ybmq kpif rfbw rlmg')
  contents = ['There has been an update to the client portal']
  yag.send('requests@leclairfoundation.org', 'CLIENT PORTAL UPDATE: ' + username, contents)
  
  
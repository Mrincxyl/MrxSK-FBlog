import os
import secrets
from PIL import Image
from flask import url_for
from flaskblog import mail
from flask_mail import Message
from flask import current_app


def save_picture(form_picture): # form_picture is the data which user submit to update
    random_hex = secrets.token_hex(8) #8 represent 8bytes
    #to get the extension of the file -> os.path.splitext -> it returns two thing 
    # 1st return filename without the extension and extension itself
    f_name , f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext #-> concatenate random_hex with the file extension
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics',picture_fn)
    #app.root_path -> is going to give us the full path all way to our package directory
    #static/profile_pics -> withing static folder in profile_pics
    output_size = (125,125) #tuple
    i = Image.open(form_picture) # open the form picture
    i.thumbnail(output_size)  # resize the form_picture to equal to the output size
    i.save(picture_path) 

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender=os.environ.get('EMAIL_USER'),
        recipients=[user.email]
    )
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, simply ignore this email.
'''
    mail.send(msg)
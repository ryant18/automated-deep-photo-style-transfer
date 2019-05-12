import subprocess
import os

content_image = 'brownbear'
style_image = 'polarbear'
iterations = '4000'

subprocess.call([os.path.join('.', 'venv', 'Scripts', 'python.exe'), os.path.join('.', 'style_transfer.py'),
                 '--content_image', os.path.join('.', 'images', content_image+'.jpg'),
                 '--style_image', os.path.join('.', 'images', style_image+'.jpg'),
                 '--iterations', iterations])

import plumbum
from plumbum import local
import plumbum.cmd
from plumbum.cmd import rm

python = local["python"]

rm("db.sqlite3")
rm("-rf", "e_riding_app/migrations")
python("manage.py", "makemigrations", "e_riding_app")
python("manage.py", "migrate")

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_riding.settings")
django.setup()


from django.contrib.auth import get_user_model

User = get_user_model()

u = User(username='admin')
u.set_password('admin')
u.is_superuser = True
u.is_staff = True
u.save()

python("manage.py", *"loadtestdata e_riding_app.CustomUser:10 "
                     "e_riding_app.VetCard:10 "
                     "e_riding_app.Horse:20 "
                     "e_riding_app.PairOnStart:10 "
                     "e_riding_app.Pair:10 "
                     "e_riding_app.Team:10 "
                     "e_riding_app.DescriptionStep:10 "
                     "e_riding_app.Step:10 "
                     "e_riding_app.Competition:15".split(" "))

python("manage.py", "loaddata", "e_riding_app/dumped_data/news.json")
python("manage.py", "loaddata", "e_riding_app/dumped_data/group.json")
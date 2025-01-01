
# Flask Example Project
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

flask shell
from app import db
from app.models import User
admin = User(username='admin')
admin.set_password('admin123')
db.session.add(admin)
db.session.commit()
```
# Extensoes da aplicacao.
#
# O objeto db mora sozinho neste arquivo para que models, dao e app possam
# importa-lo sem que um precise importar o outro.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

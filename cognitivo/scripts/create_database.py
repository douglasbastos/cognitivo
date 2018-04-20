from cognitivo.config import engine
from cognitivo.models import Base


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print('Todas as tabelas criadas com sucesso')

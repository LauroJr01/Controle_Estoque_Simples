from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime


engine = create_engine("sqlite:///database.db")
Base = declarative_base()

# Usuários
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

# Produtos
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto_nome = Column(String, nullable=False)
    quantidade = Column(Integer, default=0, nullable=False)
    preco_custo = Column(Float, nullable=False)
    preco_venda = Column(Float, nullable=False)

# Movimentações
class Movimentacao(Base):
    __tablename__ = 'movimentacoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    tipo = Column(String, nullable=False) #Entrada ou Saida.
    quantidade = Column(Integer, nullable=False)
    data = Column(DateTime, default=datetime.now, nullable=False)
    produto = relationship("Produto")
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=True)
    cliente = relationship("Cliente")

# Clientes
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    endereco = Column(String, nullable=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
'''sessao = Session()

novo_usuario = Usuario(nome="Lauro", senha="1234")

sessao.add(novo_usuario)
sessao.commit()

sessao.close()'''


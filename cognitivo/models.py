from sqlalchemy import Column, String, ForeignKey, Integer, Float, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class TubeAssembly(Base):
    __tablename__ = 'tube_assembly'

    id = Column(String(10), primary_key=True)


class OutsideShape(Base):
    __tablename__ = 'outside_shape'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class BaseType(Base):
    __tablename__ = 'base_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Component(Base):
    __tablename__ = 'component'

    id = Column(String, primary_key=True)

    component_type_id = Column(String, nullable=False)
    connection_type_id = Column(String, nullable=False)

    outside_shape_id = Column(Integer, ForeignKey(OutsideShape.id))
    outside_shape = relationship(OutsideShape)

    base_type_id = Column(Integer, ForeignKey(BaseType.id))
    base_type = relationship(BaseType)

    type = Column(String)
    height_over_tube = Column(Float)
    bolt_pattern_long = Column(Float)
    bolt_pattern_wide = Column(Float)
    groove = Column(Boolean)
    base_diameter = Column(Float)
    shoulder_diameter = Column(Float)
    unique_feature = Column(Boolean, nullable=False)
    orientation = Column(Boolean, nullable=False)
    weight = Column(Float)


class TubeAssemblyHasComponent(Base):
    __tablename__ = 'tube_assembly_has_component'

    tube_assembly_id = Column(String,
                              ForeignKey(TubeAssembly.id),
                              primary_key=True,
                              nullable=False)
    tube_assembly = relationship(TubeAssembly)

    component_id = Column(String,
                          ForeignKey(Component.id),
                          primary_key=True,
                          nullable=False)
    component = relationship(Component)

    quantity = Column(Integer)


class PriceQuote(Base):
    __tablename__ = 'price_quote'

    id = Column(Integer, primary_key=True)
    tube_assembly_id = Column(String,
                              ForeignKey(TubeAssembly.id),
                              nullable=False)
    tube_assembly = relationship(TubeAssembly)

    supplier = Column(String)
    quote_date = Column(Date)
    annual_usage = Column(Integer)
    min_order_quantity = Column(Integer)
    bracket_pricing = Column(Boolean)
    quantity = Column(Integer)
    cost = Column(Float)

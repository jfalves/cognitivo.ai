
from orm import Base
from sqlalchemy import Integer, String, DECIMAL, Boolean, Date, ForeignKey, Column
from sqlalchemy.orm import relationship

class Supplier(Base):
    __tablename__ = 'Supplier'
    id = Column(String, primary_key=True)

    tube_assembly = relationship('PriceQuote', back_populates='supplier')


class TubeAssembly(Base):
    __tablename__ = 'TubeAssembly'
    id = Column(String, primary_key=True)

    supplier = relationship('PriceQuote', back_populates='tube_assembly')
    component = relationship('MaterialBill', back_populates='tube_assembly')

class ComponentType(Base):
    __tablename__ = 'ComponentType'
    id = Column(String, primary_key=True)

    component = relationship('Component', back_populates='component_type')

class ConnectionType(Base):
    __tablename__ = 'ConnectionType'
    id = Column(String, primary_key=True)

    component = relationship('Component', back_populates='connection_type')

class Component(Base):
    __tablename__ = 'Component'
    id = Column(String, primary_key=True)
    component_type_id = Column(String, ForeignKey('ComponentType.id'), primary_key=True)
    connection_type_id = Column(String, ForeignKey('ConnectionType.id'), primary_key=True)

    type = Column(String)
    outside_shape = Column(Integer)
    base_type = Column(String)
    height_over_tube = Column(DECIMAL(10,2))
    bolt_pattern_long = Column(DECIMAL(10,2))
    bolt_pattern_wide = Column(DECIMAL(10,2))
    groove = Column(Boolean)
    base_diameter = Column(DECIMAL(10,2))
    shoulder_diameter = Column(DECIMAL(10,2))
    unique_feature = Column(Boolean)
    orientation = Column(Boolean)
    weight = Column(DECIMAL(10,2))

    component_type = relationship('ComponentType', back_populates='component')
    connection_type = relationship('ConnectionType', back_populates='component')
    tube_assembly = relationship('MaterialBill', back_populates='component')

#Association tables
class MaterialBill(Base):
    __tablename__ = 'MaterialBill'
    tube_assembly_id = Column(String, ForeignKey('TubeAssembly.id'), primary_key=True)
    component_id = Column(String, ForeignKey('Component.id'), primary_key=True)

    quantity = Column(String)

    tube_assembly = relationship("TubeAssembly", back_populates="component")
    component = relationship("Component", back_populates="tube_assembly")

class PriceQuote(Base):
    __tablename__ = 'PriceQuote'
    tube_assembly_id = Column(String, ForeignKey('TubeAssembly.id'), primary_key=True)
    supplier_id = Column(String, ForeignKey('Supplier.id'), primary_key=True)

    quote_date = Column(Date, primary_key=True)
    annual_usage = Column(Integer, primary_key=True)
    min_order_quantity = Column(Integer, primary_key=True)
    bracket_pricing = Column(Boolean)
    quantity = Column(Integer, primary_key=True)
    cost = Column(DECIMAL(10,2))

    supplier = relationship('Supplier', back_populates='tube_assembly')
    tube_assembly = relationship('TubeAssembly', back_populates='supplier')

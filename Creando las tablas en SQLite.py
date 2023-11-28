CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE Producto (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    marca TEXT,
    categoria_id INTEGER,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

CREATE TABLE Sucursal (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL
);

CREATE TABLE Stock (
    id INTEGER PRIMARY KEY,
    sucursal_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id),
    UNIQUE (sucursal_id, producto_id)
);

CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono INTEGER NOT NULL
);

CREATE TABLE Orden (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    sucursal_id INTEGER,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id)
);

CREATE TABLE Item (
    id INTEGER PRIMARY KEY,
    orden_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    monto_venta DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES Orden(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

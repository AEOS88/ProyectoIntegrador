
CREATE TABLE Categoria (
    id INT PRIMARY KEY,
    nombre VARCHAR NOT NULL
);

CREATE TABLE Producto (
    id INT PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    marca VARCHAR,
    categoria_id INT,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

CREATE TABLE Sucursal (
    id INT PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    direccion VARCHAR NOT NULL
);

CREATE TABLE Stock (
    id INT PRIMARY KEY,
    sucursal_id INT,
    producto_id INT,
    cantidad INT,
    UNIQUE (sucursal_id, producto_id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

CREATE TABLE Cliente (
    id INT PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    telefono INT NOT NULL
);

CREATE TABLE Orden (
    id INT PRIMARY KEY,
    cliente_id INT,
    sucursal_id INT,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id)
);

CREATE TABLE Item (
    id INT PRIMARY KEY,
    orden_id INT,
    producto_id INT,
    cantidad INT,
    monto_venta DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES Orden(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);

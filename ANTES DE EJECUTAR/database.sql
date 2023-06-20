


CREATE DATABASE hostal;
use hostal;

CREATE TABLE Reserva (
  IdReserva VARCHAR(30) PRIMARY KEY,
  IdHostal VARCHAR(30),
  IdHabitacion VARCHAR(30),
  IdHuesped VARCHAR(30),
  IdRecepcionista VARCHAR(30),
  FechaLlegada DATE,
  FechaSalida DATE
);

CREATE TABLE Cliente (
	RUT VARCHAR(30) PRIMARY KEY,
	Nombre VARCHAR(30),
	Correo VARCHAR(30),
	Contrasena VARCHAR(30),
	Nacimiento VARCHAR(30),
	Direccion VARCHAR(30),
	Pais VARCHAR(30),
	NTelefono VARCHAR(30)
);

CREATE TABLE Pago (
	Ntransaccion VARCHAR(30) PRIMARY KEY,
	Monto VARCHAR(30),
	Metodo VARCHAR(30),
	FechaDePago VARCHAR(30)
);

CREATE TABLE Opiniones (
	IDopinion VARCHAR(30)
);

CREATE TABLE Hostal (
	IdHostal VARCHAR(30) PRIMARY KEY,
	Nombre VARCHAR(30),
	Direccion VARCHAR(30)
);

CREATE TABLE Habitacion (
	IdHabitacion VARCHAR(30) PRIMARY KEY,
	MaxHab INT(11),
	Disponibilidad VARCHAR(30),
	IdHostal VARCHAR(30)
);

CREATE TABLE Recepcionista (
	RUT VARCHAR(30) PRIMARY KEY,
	Nombre VARCHAR(30),
	Apellido VARCHAR(30),
	Contrasena VARCHAR(30),
	HorarioLaboral VARCHAR(30),
	Sueldo VARCHAR(30),
	Gmail VARCHAR(30),
	Telefono VARCHAR(30),
	IdHostal VARCHAR(30)
);

ALTER TABLE Reserva 
ADD CONSTRAINT Reserva_Hostal_FK 
FOREIGN KEY (IdHostal)
REFERENCES Hostal (IdHostal);

ALTER TABLE Reserva 
ADD CONSTRAINT Reserva_Habitacion_FK 
FOREIGN KEY (IdHabitacion)
REFERENCES Habitacion (IdHabitacion);

ALTER TABLE Reserva 
ADD CONSTRAINT Reserva_Recepcionista_FK 
FOREIGN KEY (IdRecepcionista)
REFERENCES Recepcionista (RUT);

ALTER TABLE Recepcionista
ADD CONSTRAINT Recepcionista_IdHostal_FK 
FOREIGN KEY (IdHostal)
REFERENCES Hostal (IdHostal);

ALTER TABLE Habitacion
ADD CONSTRAINT Habitacion_IdHostal_FK 
FOREIGN KEY (IdHostal)
REFERENCES Hostal (IdHostal);

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais, NTelefono)
VALUES ('12345678-9', 'Juan Pérez', 'juanperez@gmail.com', 'hola123', '1990-01-01', 'Los Pastores 123', 'Chile', '1');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais, NTelefono)
VALUES ('19239102-1', 'Pedro Gómez', 'pedrogomez@gmail.com', '123hola', '1992-05-15', 'Calle Uruguay 822', 'Chile', '2');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais, NTelefono)
VALUES ('21390129-3', 'Marcela Rojas', 'marcelarojas@gmail.com', 'mrojas1988', '1988-11-30', 'Calle Sanchez 452', 'Chile', '3');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais, NTelefono)
VALUES ('16239087-5', 'Carolina Mendoza', 'carolinamendoza@gmail.com', 'caro123', '1995-07-20', 'Calle Vidal 721', 'Chile', '4');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais, NTelefono)
VALUES ('19210295-7', 'Laura Gutiérrez', 'lauragutierrez@gmail.com', 'lauraguti10', '1994-03-10', 'Calle Bravo 210', 'Chile', '5');

INSERT INTO Hostal (IdHostal, Nombre, Direccion)
VALUES ('H001', 'Hostal Pedro de Valdivia', 'Avenida Alameda 456');

INSERT INTO Hostal (IdHostal, Nombre, Direccion)
VALUES ('H002', 'Hostal Iquique', 'Avenida del Mar 789');

INSERT INTO Hostal (IdHostal, Nombre, Direccion)
VALUES ('H003', 'Hostal Pto Montt', 'Avenida Montt 987');

INSERT INTO Hostal (IdHostal, Nombre, Direccion)
VALUES ('H004', 'Hostal Arica', 'Avenida Peru 654');

INSERT INTO Hostal (IdHostal, Nombre, Direccion)
VALUES ('H005', 'Hostal Coquimbo', 'Avenida Herradura 312');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad, IdHostal)
VALUES ('H001', 2, 'Disponible', 'H001');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad, IdHostal)
VALUES ('H002', 1, 'Disponible', 'H002');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad, IdHostal)
VALUES ('H003', 2, 'Disponible', 'H003');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad, IdHostal)
VALUES ('H004', 7, 'Disponible', 'H004');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad, IdHostal)
VALUES ('H005', 0, 'Ocupada', 'H005');

INSERT INTO Recepcionista (RUT, Nombre, Apellido, Contrasena, HorarioLaboral, Sueldo, Gmail, Telefono, IdHostal)
VALUES ('18765432-1', 'María', 'López', 'mlopez123' ,'9AM - 5PM', '2000', 'marialopez@gmail.com', '123456789', 'H001');

INSERT INTO Recepcionista (RUT, Nombre, Apellido, Contrasena, HorarioLaboral, Sueldo, Gmail, Telefono, IdHostal)
VALUES ('13751298-2', 'Ana', 'Torres',  'atorres123','8AM - 4PM' ,'1800', 'anatorres@gmail.com', '987654321', 'H002');

INSERT INTO Recepcionista (RUT, Nombre, Apellido, Contrasena, HorarioLaboral, Sueldo, Gmail, Telefono, IdHostal)
VALUES ('14650974-4', 'Luis', 'Silva', 'lsilva123', '10AM - 6PM', '2200', 'luissilva@gmail.com', '654321987', 'H003');

INSERT INTO Recepcionista (RUT, Nombre, Apellido, Contrasena, HorarioLaboral, Sueldo, Gmail, Telefono, IdHostal)
VALUES ('20132439-6', 'Roberto', 'Fernández', 'rfernandez123', '11AM - 7PM', '2400', 'robertofernandez@gmail.com', '789456123', 'H004');

INSERT INTO Recepcionista (RUT, Nombre, Apellido, Contrasena, HorarioLaboral, Sueldo, Gmail, Telefono, IdHostal)
VALUES ('21354678-8', 'Diego', 'Rojas', 'drojas123','9AM - 5PM', '2000', 'diegorojas@gmail.com', '123987456', 'H005');

INSERT INTO Recepcionista (RUT, Nombre, Apellido, Contrasena, HorarioLaboral, Sueldo, Gmail, Telefono, IdHostal)
VALUES ('web', 'Reservas', 'web', 'sys','FULL TIME', '0', 'sys@gmail.com', '0', 'H004');

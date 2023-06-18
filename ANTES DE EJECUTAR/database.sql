


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
	Pais VARCHAR(30)
);

CREATE TABLE Pago (
	Ntransaccion VARCHAR(30) PRIMARY KEY,
	Monto VARCHAR(30),
	FechaDePago VARCHAR(30)
);

CREATE TABLE Opiniones (
	IDopinion VARCHAR(30)
);

CREATE TABLE Hostal (
	IdHostal VARCHAR(30) PRIMARY KEY,
	Nombre VARCHAR(30),
	Direccion VARCHAR(30),
	Ingresos VARCHAR(30)
);

CREATE TABLE Habitacion (
	IdHabitacion VARCHAR(30) PRIMARY KEY,
	MaxHab VARCHAR(30),
	Disponibilidad VARCHAR(30)
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

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais)
VALUES ('12345678-9', 'Juan Pérez', 'juanperez@gmail.com', 'hola123', '1990-01-01', 'Los Pastores 123', 'Chile');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais)
VALUES ('19239102-1', 'Pedro Gómez', 'pedrogomez@gmail.com', '123hola', '1992-05-15', 'Calle Uruguay 822', 'Chile');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais)
VALUES ('21390129-3', 'Marcela Rojas', 'marcelarojas@gmail.com', 'mrojas1988', '1988-11-30', 'Calle Sanchez 452', 'Chile');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais)
VALUES ('16239087-5', 'Carolina Mendoza', 'carolinamendoza@gmail.com', 'caro123', '1995-07-20', 'Calle Vidal 721', 'Chile');

INSERT INTO Cliente (RUT, Nombre, Correo, Contrasena, Nacimiento, Direccion, Pais)
VALUES ('19210295-7', 'Laura Gutiérrez', 'lauragutierrez@gmail.com', 'lauraguti10', '1994-03-10', 'Calle Bravo 210', 'Chile');

INSERT INTO Hostal (IdHostal, Nombre, Direccion, Ingresos)
VALUES ('H001', 'Hostal Pedro de Valdivia', 'Avenida Alameda 456', '10000');

INSERT INTO Hostal (IdHostal, Nombre, Direccion, Ingresos)
VALUES ('H002', 'Hostal Iquique', 'Avenida del Mar 789', '15000');

INSERT INTO Hostal (IdHostal, Nombre, Direccion, Ingresos)
VALUES ('H003', 'Hostal Pto Montt', 'Avenida Montt 987', '93102');

INSERT INTO Hostal (IdHostal, Nombre, Direccion, Ingresos)
VALUES ('H004', 'Hostal Arica', 'Avenida Peru 654', '10030');

INSERT INTO Hostal (IdHostal, Nombre, Direccion, Ingresos)
VALUES ('H005', 'Hostal Coquimbo', 'Avenida Herradura 312', '8020');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad)
VALUES ('H001', '2', 'Disponible');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad)
VALUES ('H002', '1', 'Disponible');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad)
VALUES ('H003', '2', 'Disponible');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad)
VALUES ('H004', '7', 'Disponible');

INSERT INTO Habitacion (IdHabitacion, MaxHab, Disponibilidad)
VALUES ('H005', '0', 'Ocupada');

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

INSERT INTO Reserva (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida)
VALUES ('R001', 'H001', 'H001', '12345678-9', '18765432-1', '2023-07-01', '2023-07-05');

INSERT INTO Reserva (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida)
VALUES ('R002', 'H002', 'H002', '19239102-1', '13751298-2', '2023-08-10', '2023-08-15');

INSERT INTO Reserva (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida)
VALUES ('R003', 'H003', 'H003', '21390129-3', '14650974-4', '2023-09-20', '2023-09-25');

INSERT INTO Reserva (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida)
VALUES ('R004', 'H004', 'H004', '16239087-5', '20132439-6', '2023-10-15', '2023-10-20');

INSERT INTO Reserva (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida)
VALUES ('R005', 'H005', 'H005', '19210295-7', '21354678-8', '2023-11-30', '2023-12-05');

from principal.connector import Operaciones 
from principal.main import bconsola
# from principal.menui import MenuPrincipal
op = Operaciones
listareservas = []
listainfohos = []
def verReservas():
    listareservas = op.getReservas()
    print("==================== Reservas ====================")
    reservas = []
    for r in listareservas:
        reservas.append(r)
        print(len(reservas), ".- ", r.IdReserva)
    print("101.- Para regresar al Menu Principal")
    print("==================================================")
    s = int(input("Selecciona una reserva para ver mas información sobre esta: "))
    if s >= 1 and s <= len(reservas):
        rs = reservas[s-1]
        listainfohos = op.getinfoHostalporID(rs.IdHostal)
        for h in listainfohos:
            print("============== Información sobre ",rs.IdHostal," ================")
            print(h.nombre)
            print("Dirección: ",h.direccion)
            print("Reservado mediante: ",r.IdRecepcionista)
            print("Reservado por: ",r.IdHuesped)
            print("Fecha de Llegada: ", r.FechaLlegada)
            print("Fecha de Regreso: ", r.FechaSalida)
    # elif s == 101:
    
    #     MenuPrincipal()

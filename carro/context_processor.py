from .carro import Carro


def importe_total_carro(request):
    carro = Carro(request)
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + (float(value["precio"]) * value["cantidad"])
            total = round(total,2)

    else:
        total = "DEBES HACER LOGING"
    return {"importe_total_carro": total}

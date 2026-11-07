from django.contrib.auth import authenticate, login, logout
from django.db.models import Max
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from videojuegos.models import Paquete, Videojuego


def inicio(request):
    videojuego_destacado = Videojuego.objects.filter(nombre__icontains="Zelda").first()
    paquetes_activos = Paquete.objects.filter(activo=True)
    paquetes = (
        paquetes_activos.select_related('consola', 'videojuego')
        .order_by('-fecha_creacion')[:6]
    )
    descuento_max = (
        paquetes_activos.aggregate(Max('descuento'))['descuento__max'] or 0
    )
    return render(
        request,
        "index.html",
        {
            "videojuego_destacado": videojuego_destacado,
            "paquetes": paquetes,
            "descuento_max": descuento_max,
        },
    )


def contacto(request):
    return render(request, "usuario/contacto.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            proxima = request.GET.get("next")
            # Evita redirecciones abiertas (open redirect) validando el host
            if proxima and url_has_allowed_host_and_scheme(
                proxima,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(proxima)
            return redirect("gestionar_videojuegos")
        return render(
            request,
            "usuario/admin_login.html",
            {"error": "Usuario o contraseña incorrectos."},
        )
    if request.user.is_authenticated:
        return redirect("gestionar_videojuegos")
    aviso = bool(request.GET.get("next"))
    return render(request, "usuario/admin_login.html", {"aviso": aviso})


def admin_logout(request):
    logout(request)
    return redirect("admin_login")

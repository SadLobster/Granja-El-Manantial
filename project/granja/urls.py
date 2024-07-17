from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('equipo/', views.team, name='team'),
    path('productos/', views.product, name='product'),
    path('sobre-nosotros/', views.about, name='about'),
    path('iniciar-sesion/', views.login_view, name='login'),
    path('cerrar-sesion/', views.log_out, name='logout'),
    path('restablecer-contraseña/', views.forgot_password, name='forgot_password'),
    path('cambiar-contraseña/', views.change_password, name='change_password'),

    # ADMINISTRADOR
    path('administrador/', views.administrador, name='administrador'),

    # ANIMALES
    path('admin-animales/', views.animals, name='animals'),
    path('animales/insert/', views.insert_animal, name='insert_animal'),
    path('animales/reload-edad/', views.update_edad, name='update_edad'),
    path('animales/update/', views.update_animal, name='update_animal'),
    path('animales/update/<int:animal_id>/', views.update_form_animal, name='update_form_animal'),
    path('animales/delete/<int:animal_id>/', views.delete_animal, name='delete_animal'),
    path('animales/search', views.lista_animales, name='lista_animales'),

    # TRABAJADORES
    path('trabajadores/', views.workers, name='workers'),
    path('trabajadores/insert/', views.insert_worker, name='insert_worker'),
    path('trabajadores/update/', views.update_worker, name='update_worker'),
    path('trabajadores/update/<int:worker_id>/', views.update_form_worker, name='update_form_worker'),
    path('trabajadores/delete/<int:worker_id>/', views.delete_worker, name='delete_worker'),
    path('trabajadores/search', views.lista_trabajadores, name='lista_trabajadores'),

    # SUMINISTROS
    path('suministros/', views.supplies, name='supplies'),
    path('suministros/insert/', views.insert_supplie, name='insert_supplie'),
    path('suministros/update-cantidad/', views.update_cantidad, name='update_cantidad'),
    path('suministros/update/', views.update_supplie, name='update_supplie'),
    path('suministros/update/<int:suministro_id>/', views.update_form_supplie, name='update_form_supplie'),
    path('suministros/delete/<int:suministro_id>/', views.delete_supplie, name='delete_supplie'),
    path('suministros/search/', views.lista_suministros, name='lista_suministros'),

    path('suministros/grafico-precios/', views.grafico_precio, name='grafico_precio'),
    path('suministros/grafico-existencias/', views.grafico_existencias, name='grafico_existencias'),

    # PRODUCCION
    path('produccion/', views.production, name='production'),
    path('produccion/insert/', views.insert_production, name='insert_production'),
    path('produccion/delete/<int:produccion_id>/', views.delete_production, name='delete_production'),
    path('produccion/search/', views.lista_produccion, name='lista_produccion'),

    # VENTA
    path('venta/', views.sale, name='sales'),
    path('venta/insert/', views.insert_sale, name='insert_sale'),
    path('venta/delete/<int:venta_id>/', views.delete_sale, name='delete_sale'),
    path('venta/search/', views.lista_sale, name='lista_sale'),
    path('venta/reporte/', views.generate_report, name='generar_reporte'),

    # REGISTROS DE SALUD
    path('registros-salud/', views.record, name='record'),
    path('registros-salud/insert/', views.insert_record, name='insert_record'),
    #path('registros-salud/update/', views.update_record, name='update_record'),
    #path('registros-salud/update/<int:record_id>/', views.update_form_record, name='update_form_record'),
    path('registros-salud/delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('registros-salud/search/', views.lista_record, name='lista_registros'),
    path('registros-salud/fluctuacion-registros/', views.grafico_salud, name='grafico_salud'),
    path('registros-salud/grafico-crias/', views.grafico_crias, name='grafico_crias'),

    # TRABAJADOR
    path('trabajador/', views.worker, name='worker'),

    # VETERINARIO
    path('veterinario/', views.vet, name='vet'),

    # TRABAJADOR-ANIMALES
    path('animales/', views.animals2, name='animals2'),

    # TRABAJADOR-SUMINISTROS
    path('trabajador/suministros/', views.supplies2, name='supplies2'),

    # TRABAJADOR-PRODUCCION
    path('trabajador/produccion/', views.production2, name='production2'),

    path('trabajador/venta/', views.sale2, name='sales2'),

    # VETERINARIO-REGISTROS DE SALUD
    path('veterinario/registros-salud/', views.record2, name='record2'),
]
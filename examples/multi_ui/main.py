#!/usr/bin/env python3
from nicegui.element import Element
from router import Router

from nicegui import ui


@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page
def main():
    router = Router()

    @router.add('/')
    def show_root():
        ui.label('Quasar component').classes('text-2xl')
    
    @router.add('/quasar')
    def show_quasar():
        ui.label('Quasar components').classes('text-2xl')
        ui.button('Quasar', on_click=lambda: router.open(show_quasar)).classes('w-32')
        ui.date('30-04-2020', mask='DD-MM-YY')

    @router.add('/primevue')
    def show_primevue():
        ui.label('PrimeVue components').classes('text-2xl')
        ui.buttonPri('PrimeVue', on_click=lambda: router.open(show_primevue)).classes('w-32')  
        ui.datePri('04/30/2020 01:02:03', mask='MM/dd/yyyy HH:mm:ss', on_change=lambda e: ui.notify(e.args)).props('showTime hourFormat="24"')

    @router.add('/vuetify')
    def show_vuetify():
        ui.label('Vuetify components').classes('text-2xl')
        ui.buttonVfy('Vuetify', on_click=lambda: router.open(show_vuetify)).classes('w-32')
        ui.dateVfy('30-04-2020', mask='dd-MM-yyyy', on_change=lambda e: ui.notify(e.args)) #  solo date 
    
    @router.add('/naive')
    def show_naive():
        ui.label('Naive components').classes('text-2xl')
        ui.buttonNve('Naive', on_click=lambda: router.open(show_naive)).classes('w-32') # formato obbligato per via della visualizzazione nell'input
        ui.dateNve('30-04-2020 01:02:03', valueFormat='dd-MM-yyyy HH:mm:ss', format='dd/MM/yyyy HH:mm:ss', on_change=lambda e: ui.notify(e.args[1])).props('type="datetime"')
             

    @router.add('/element')
    def show_element():
        ui.label('Element components').classes('text-2xl')
        ui.buttonEle('Element', on_click=lambda: router.open(show_element))
        ui.dateEle('30-04-2020 01:02:03', format='DD/MM/YYYY HH:mm:ss', valueFormat='DD-MM-YYYY HH:mm:ss', on_change=lambda e: ui.notify(e.args)).props('type="datetime"')
    

    #@router.add('/ant')
    #def show_ant():
    #    ui.label('Ant components').classes('text-2xl')
    #    ui.buttonAnt('Ant', on_click=lambda: router.open(show_ant))
    #    ui.dateAnt('30-04-2020', format='DD/MM/YYYY', valueFormat='DD-MM-YYYY', on_change=lambda e: ui.notify(e.args))

        
    options =   [{
        'label': "Quasar",
        'key': "quasar-components",
        'path': '/quasar',
        'icon': 'vuejs'
    },
    {
        'label': "Prime Vue",
        'key': "prime-vue",
        'path': '/primevue',
        'icon': 'vuejs'
    },
    {
        'label': "Vuetify",
        'key': "vuetify",
        'disabled': False,   
        'icon': "vuejs",
        'path': '/vuetify'
    },
    {
        'label': "Naive",
        'key': "naive",
        'disabled': False,
        'icon': "vuejs",
        'path': '/naive'
    },
    {
        'label': "Element",
        'key': "element",
        'icon': "vuejs",
        'path': '/element'

    },
    #{
    #    'label': "Ant",
    #    'key': "ant",
    #    'icon': "vuejs",
    #    'path': '/ant'
    #},
    ]

    Element('n-layout-header').props('bordered').classes('py-3 px-4 text-white bg-sky-500').add_slot('default', "Multiple suite of components")
    with Element('n-space').props('vertical').classes('h-full w-full'):
        with Element('n-layout').classes('h-full').props('has-sider'):
            with Element('n-layout-sider').props('bordered collapse-mode="width" :collapse-width="64" :width="240" show-trigger'):
                ui.menuNve(options, on_click=lambda e : router.open(e.args['path']))

            # this places the content which should be displayed
            router.frame().classes('w-full h-screen p-4 bg-gray-100')


ui.run(ui_components_suite='quasar', prod_js=False, native=False, port=8081)

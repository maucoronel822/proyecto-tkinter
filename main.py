import tkinter as tk
from tkinter import messagebox

# Función para mostrar la ventana de pendientes
def mostrar_pendientes():
    ventana_pendientes = tk.Tk()
    ventana_pendientes.children
    ventana_pendientes.title('Pendientes')
    ventana_pendientes.geometry('800x600')
    ventana_pendientes.minsize(300, 200)
    ventana_pendientes.maxsize(1000, 800)

    def agregar_tarea():
        tarea = texto_pendiente.get().strip()
        if tarea:
            listBox_pendientes.insert(tk.END,tarea)
            texto_pendiente.delete(0,tk.END)
        else:
            messagebox.showwarning('Campo vacío', 'Por favor ingresa una tarea')

    def finalizar_tarea():
        seleccion = listBox_pendientes.curselection()
        if seleccion:
            tarea = listBox_pendientes.get(seleccion)
            listBox_pendientes.delete(seleccion)
            listBox_finalizadas.insert(tk.END, tarea)
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea pendiente para finalizar.")

    def eliminar_tarea():
        seleccion = listBox_finalizadas.curselection()
        if seleccion:
            listBox_finalizadas.delete(seleccion)
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")            

    #Etiqueta de bienvenida
    label_bienvenida = tk.Label(ventana_pendientes,text='Bienvenido a tu lista de pendientes', font=('',15,'bold'))
    label_bienvenida.pack(pady=(20,5))

    # Contenedor horizontal
    contenedor_horizontal = tk.Frame(ventana_pendientes)
    contenedor_horizontal.pack(pady=(10, 10))

    #Etiqueta ingresar pendientes
    label_tarea = tk.Label(contenedor_horizontal,text='Ingresa una tarea')
    label_tarea.pack(side='left',padx=(0,10),pady=(0,10))

    #Texto ingresar pendiente
    texto_pendiente = tk.Entry(contenedor_horizontal, width=50)
    texto_pendiente.pack(side='left', padx=(5,0),pady=(0,10))

    #Boton agregar pendiente
    bt_agregarPendiente = tk.Button(ventana_pendientes,text='Agregar tarea',bg='#2b632c', fg='white',font=('',10,'bold'), command=agregar_tarea)
    bt_agregarPendiente.pack(side='top', pady=(5,0))

    #Contenedor label de tareas pendientes y finalizadas
    contenedor_pendientes = tk.Frame(ventana_pendientes)
    contenedor_pendientes.pack(side='top',pady=(10,10))

    #Label lista de tareas
    label_pendientes = tk.Label(contenedor_pendientes, text='Tareas pendientes',font=('',10,'bold'))
    label_pendientes.pack(side='left', padx=(0,118))

    #Label lista de tareas completadas
    label_pendientes = tk.Label(contenedor_pendientes, text='Tareas finalizadas',font=('',10,'bold'))
    label_pendientes.pack(side='left', padx=(118,0))

    #Contenedor de listbox
    contenedor_listBox = tk.Frame(ventana_pendientes,)
    contenedor_listBox.pack(side='top',pady=(0,10))

    #Listbox pendientes
    listBox_pendientes = tk.Listbox(contenedor_listBox, width=50,height=15)
    listBox_pendientes.pack(side='left',padx=(0,20))

    #Listbox finalizadas
    listBox_finalizadas = tk.Listbox(contenedor_listBox,width=50,height=15)
    listBox_finalizadas.pack(side='left',padx=(20,0))

    #Contenedor de botones
    contenedor_botones = tk.Frame(ventana_pendientes,)
    contenedor_botones.pack(side='top',pady=(10,0))

    #Boton agregar pendiente
    bt_finalizar = tk.Button(contenedor_botones,text='Finalizar tarea',bg='#2b632c', fg='white',font=('',10,'bold'),command=finalizar_tarea)
    bt_finalizar.pack(side='left', padx=(0,118))

    #Boton agregar pendiente
    bt_eliminar = tk.Button(contenedor_botones,text='Eliminar tarea',bg='Red', fg='white',font=('',10,'bold'),command=eliminar_tarea)
    bt_eliminar.pack(side='left', padx=(118,0))

    ventana_pendientes.mainloop()

mostrar_pendientes()
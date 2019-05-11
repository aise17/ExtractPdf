export class Bonos {
    id: string;
    titulo: string;
    peticiones: string;
    descripcion: string;
    precio: string;


    constructor(titulo: string, peticiones: string, descripcion: string, precio: string){
        this.titulo = titulo;
        this.peticiones = peticiones;
        this.descripcion = descripcion;
        this.precio = precio;
        
    }

}

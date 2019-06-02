import { Usuario } from './usuario.model';

export class Campaing{

    id:string;
    usuarios: string;
    asunto: string;
    contenido: string;
    fecha_creacion: Date; 
    lanzada: boolean; 
    fecha_publicacion: Date;

}
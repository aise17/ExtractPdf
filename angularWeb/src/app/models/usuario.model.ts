export class Usuario {
    id: any;
    usuario: string;
    password: string;
    first_name: string;
    last_name: string;
    email: string;
    access_token: string;

    constructor(usuario?: string, password?: string) {
        this.usuario = usuario;
        this.password = password;
    }

}

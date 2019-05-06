export class ApiToken{

    usuario: string;
    pass: string;
    client_id: string;
    client_secret: string;
    grant_type: string;

    

    constructor(usuario: string, pass: string){

        this.usuario = usuario;
        this.pass = pass;
        this.client_id = 'iQ4VatZNxqlv5kdXodq1jp47Nc57qCML4giA0vvD';
        this.client_secret = '6QQEnH8OfLICc45i2ynUU7RjOj5F6o3yvQKAHCOTQqoiaRS9aP9SeGe0OoKiVCPiOvzh0exGv3mS8hxRu79W0CGkc0Ly5kQ3IS1KpS9u6GGraUKBQwr56y7cEL7900Rq';
        this.grant_type = 'password';
    }

 

}
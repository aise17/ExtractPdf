export class ApiToken{

    grant_type: string;
    usuario: string;
    pass: string;
    client_id: string;
    client_secret: string;
    

    

    constructor(usuario: string, pass: string){

        this.grant_type = 'password';
        this.usuario = usuario;
        this.pass = pass;
        this.client_id = 'xIlTUtu3pv3YCN0NZxioinzAIvnqhaUPB3j6C9m1';
        this.client_secret = '15VmSMITKwQTOdDxSfUtFa6SGhvSkhRbtumDSJssPaOvhL1BJAoql5SCM6EVGdEPEubougfrpR3f29GoPDhgeez3o9kWlSQFRsd03wiJiHz9Wlgp9V61y8tdom0XyZoj';
        
    }

 

}
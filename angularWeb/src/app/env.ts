export class env{
    ip :string;
    constructor(){
        this.ip = 'localhost';
    }

    public getIp(){
        return this.ip;
    }
}
import { Injectable } from '@angular/core';
import { of, Observable } from 'rxjs';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Usuario } from '../models/usuario.model';
import { tap, catchError } from 'rxjs/operators';
import { UserRequest } from '../models/userRequest.model';

import { environment } from 'src/environments/environment';
import { BonoUsuario } from '../models/Bonousuario.model';
import { envi } from '../env';



@Injectable({
  providedIn: 'root'
})
export class UsuarioService {




  
  constructor(private http: HttpClient) { }

  private loginUrl = 'http://' + envi.ip+ ':80/usuarios/login/';
  private userChangeUrl = 'http://' + envi.ip + ':80/usuarios/user/';
  private userRequestUrl = 'http://' + envi.ip + ':80/usuarios/request_for_user/';
  private logoutUrl = 'http://' + envi.ip + ':80/usuarios/logout/'; 
  private filesUrl = 'http://' + envi.ip + ':80/usuarios/list_files/';
  private registerUrl = 'http://' + envi.ip + ':80/usuarios/register/';
  private userBonusUrl = 'http://' + envi.ip + ':80/usuarios/getUserBonus/';
  private changeBonusActiveUrl = 'http://' + envi.ip + ':80/usuarios/getUserBonus/';



  chageUserBonusActive(bono: BonoUsuario, authorization: string) {
  
    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'application/json');
    
    return this.http.put(this.changeBonusActiveUrl, bono, {headers: headers}  ).pipe(
      tap((res: Response) => this.log(`recivido= ${res}`)),
      catchError(this.handleError<Response>('error al activar el bono'))
    );
  }

  getRequest(user: Usuario, authorization: string): Observable<UserRequest> {

    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'application/json');
   
    return this.http.post(this.userRequestUrl, user, {headers: headers}  ).pipe(
      tap((res: UserRequest) => this.log(`usuario recivido= ${res}`)),
      catchError(this.handleError<UserRequest>('error de peticion UserRequest'))
    );
  }

  getBonos(bono: BonoUsuario, authorization: string): Observable<BonoUsuario> {

    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'application/json');
   
    return this.http.post(this.userBonusUrl, bono, {headers: headers}  ).pipe(
      tap((res: BonoUsuario) => this.log(`bono usuario recivido= ${res}`)),
      catchError(this.handleError<BonoUsuario>('error de peticion bono usuario'))
    );
  }

  getFiles(user: Usuario, authorization: string): Observable<UserRequest> {

    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
      headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'application/json');

    return this.http.post(this.filesUrl, user, {headers: headers}  ).pipe(
      tap((res: UserRequest) => this.log(`usuario recivido= ${res}`)),
      catchError(this.handleError<UserRequest>('error de peticion UserRequest'))
    );
  }

  logout(user: Usuario): Observable<Usuario> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    console.log(user);
    return this.http.post<Usuario>(this.logoutUrl, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }

  login(user: Usuario): Observable<Usuario> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');

    return this.http.post<Usuario>(this.loginUrl, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`reusltad0 =${res['ok']}  usuario recivido=${res['salida']} `)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }

  register(user: Usuario): Observable<Usuario> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');

    return this.http.post<Usuario>(this.registerUrl, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }

  change(user: Usuario, authorization: string): Observable<Usuario> {

    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'PUT');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'blob');
    

    return this.http.post<Usuario>(this.userChangeUrl + user.id, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido= ${res['username']}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }


  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      console.error(error);

      this.log(`${operation} failed: ${error.message}`);

      return of(result as T);
    };
  }

  private log(entrada: string) {
    console.log(entrada);
  }
}

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';
import { Token } from '@angular/compiler';
import { ApiToken } from '../models/token.model';

@Injectable({
  providedIn: 'root'
})
export class Oauth2Service {

  constructor(private http: HttpClient) { }

  private createApiTokenUrl = 'http://localhost:8001/o/token/';


  getToken (usuario: string, pass: string): Observable<Response> {



   

    var token = new ApiToken(usuario.toString(), pass.toString());


    console.log(token)

    const fd = new FormData();
    fd.append('grant_type', token.grant_type);
    fd.append('username', token.usuario);
    fd.append('password', token.pass);
    fd.append('client_id', token.client_id);
    fd.append('client_secret', token.client_secret);
  

  

    console.log(fd);
    return this.http.post<Response>(this.createApiTokenUrl, fd ).pipe(
      tap((res: Response) => this.log(`get token w/ token=${res}`)),
      catchError(this.handleError<Response>('getToken'))
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
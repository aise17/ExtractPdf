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


    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');

    var token = new ApiToken(usuario, pass);

    console.log(token);
    return this.http.post<Response>(this.createApiTokenUrl, token, {headers: headers}  ).pipe(
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

import { Injectable } from '@angular/core';
import { of, Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { Contacto } from '../models/contacto.model';
import { HttpHeaders, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ContactoService {

  
  private contactoUrl = 'http://localhost:8001/file/contacto/';


  constructor(private http: HttpClient) { }


  sendEmail(contacto: Contacto): Observable<Contacto> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': 'my-auth-token',
        'Access-Control-Allow-Origin': '*'
      })
    };

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    console.log(contacto);
    return this.http.post<Contacto>(this.contactoUrl, contacto, {headers: headers}  ).pipe(
      tap((res: Contacto) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Contacto>('error de envio de usuario'))
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

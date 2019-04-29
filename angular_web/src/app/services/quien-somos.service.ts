import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

import { Explicacion } from '../models/explicacion.model';
import { catchError, map, tap } from 'rxjs/operators';
import { QuienSomos } from '../models/quienSomos.model';


@Injectable({
  providedIn: 'root'
})
export class QuienSomosService {


  private explicacionUrl = 'http://localhost:8001/file/quienSomos/';


  constructor(private http: HttpClient) { }


  getContenido (): Observable<QuienSomos[]> {
    return this.http.get<QuienSomos[]>(this.explicacionUrl)
      .pipe(
        tap(contenido => this.log('fetched contenido')),
        catchError(this.handleError('Fallo de peticion', []))
      );
    }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  private log(entrada: string) {
    console.log(entrada);
  }





}

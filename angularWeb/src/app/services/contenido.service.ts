import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Contenido } from '../models/contenido.model';
import { tap, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ContenidoService {

  private explicacionUrl = 'http://localhost:8001/contenido/explicacion-inicio/';


  constructor(private http: HttpClient) { }

  
  getContenido (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.explicacionUrl)
      .pipe(
        tap(explicacion => this.log('fetched explicacion')),
        catchError(this.handleError('getHeroes', []))
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

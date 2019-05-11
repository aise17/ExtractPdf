import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Contenido } from '../models/contenido.model';
import { tap, catchError } from 'rxjs/operators';
import { Bonos } from '../models/bonos.model.';

@Injectable({
  providedIn: 'root'
})
export class ContenidoService {

  private contenidoUrl = 'http://localhost:8001/contenido/explicacion-inicio/';
  private anuncios_superiorUrl = 'http://localhost:8001/contenido/explicacion-inicio/';
  private anuncios_lateralrUrl = 'http://localhost:8001/contenido/explicacion-inicio/';
  private anuncio_inferiorUrl = 'http://localhost:8001/contenido/explicacion-inicio/';
  private bonosUrl = 'http://localhost:8001/contenido/bonos/';


  constructor(private http: HttpClient) { }

  
  getContenido (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.contenidoUrl)
      .pipe(
        tap(contenido => this.log('fetched contenido')),
        catchError(this.handleError('getContenido', []))
      );
    }


  getAnuncioSuperior (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.anuncios_superiorUrl)
      .pipe(
        tap(anuncio_superior => this.log('fetched anuncio superior')),
        catchError(this.handleError('getAnuncioSuperior', []))
      );
    }

  getAnuncioLateral (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.anuncios_lateralrUrl)
      .pipe(
        tap(anuncio_lateral => this.log('fetched anuncio lateral')),
        catchError(this.handleError('getAnuncioLateral', []))
      );
    }

  getAnuncioInferior (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.anuncio_inferiorUrl)
      .pipe(
        tap(anuncio_inferior => this.log('fetched anuncio inferior')),
        catchError(this.handleError('getAnuncioInferior', []))
      );
    }

  getBonos (): Observable<Bonos[]> {
    return this.http.get<Bonos[]>(this.bonosUrl)
      .pipe(
        tap(explicacion => this.log('fetched explicacion')),
        catchError(this.handleError('getBonos', []))
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

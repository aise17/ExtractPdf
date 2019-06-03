import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Contenido } from '../models/contenido.model';
import { tap, catchError } from 'rxjs/operators';
import { Bonos } from '../models/bonos.model.';
import { environment } from 'src/environments/environment';
import { Faqs } from '../models/faqs.model';
import { envi } from '../env';

@Injectable({
  providedIn: 'root'
})
export class ContenidoService {

  private contenidoUrl = 'http://' + envi.ip+ ':80/contenido/explicacion-inicio/';
  private contenidoScrapyUrl = 'http://' + envi.ip+ ':80/contenido/explicacion-scrapy/';
  private faqsUrl = 'http://' + envi.ip+ ':80/contenido/faqs/';
  private anuncios_superiorUrl = 'http://' + envi.ip+ ':80/contenido/explicacion-inicio/';
  private anuncios_lateralrUrl = 'http://' + envi.ip+ ':80/contenido/explicacion-inicio/';
  private anuncio_inferiorUrl = 'http://' + envi.ip+ ':80/contenido/explicacion-inicio/';
  private bonosUrl = 'http://' + envi.ip+ ':80/contenido/bonos/';
  private normas_ocrUrl = 'http://' + envi.ip+ ':80/contenido/normas-ocr/';
  private normas_scrapyURL = 'http://' + envi.ip+ ':80/contenido/normas-scrapy/';


  constructor(private http: HttpClient) { }

  
  getContenido (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.contenidoUrl)
      .pipe(
        tap(contenido => this.log('fetched contenido')),
        catchError(this.handleError('getContenido', []))
      );
    }
  getContenidoScrapy (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.contenidoScrapyUrl)
      .pipe(
        tap(contenido => this.log('fetched contenido')),
        catchError(this.handleError('getContenido', []))
      );
    }

  getFaqs (): Observable<Faqs[]> {
    return this.http.get<Faqs[]>(this.faqsUrl)
      .pipe(
        tap(faqs => this.log('fetched fqs')),
        catchError(this.handleError('getfaqs', []))
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

  getNormasOcr (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.normas_ocrUrl)
      .pipe(
        tap(normas_ocr => this.log('fetched normas ocr')),
        catchError(this.handleError('getNormasOcr', []))
      );
    }

  getNormasScrapy (): Observable<Contenido[]> {
    return this.http.get<Contenido[]>(this.normas_scrapyURL)
      .pipe(
        tap(normas_scrapy => this.log('fetched normas scrapy')),
        catchError(this.handleError('getNormasScrapy', []))
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

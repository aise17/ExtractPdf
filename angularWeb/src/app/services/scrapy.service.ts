import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Ocr } from '../models/ocr.model';
import { Observable, of } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ScrapyService {


  private scrapyUrl = 'http://' + environment.ip+ ':80/file/scrapy/';


  constructor(private http: HttpClient) { }




  addFile (orc: Ocr, authorization: string): Observable<Response> {


    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    const fd = new FormData();
    fd.append('descripcion', orc.descripcion);
    fd.append('documento', orc.documento);
    fd.append('proceso', orc.proceso);
    if (orc.usuario) {
      fd.append('usuario', orc.usuario);
    }


    console.log(orc);
    return this.http.post<Response>(this.scrapyUrl, fd, {headers: headers}  ).pipe(
      tap((res: Response) => this.log(`added file w/ id=${res}`)),
      catchError(this.handleError<Response>('addFile'))
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

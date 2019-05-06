import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of, from } from 'rxjs';

import { Explicacion } from '../models/explicacion.model';
import { catchError, map, tap } from 'rxjs/operators';
import { Ocr } from '../models/ocr.model';
import { JsonOcr } from '../models/JsonOcr.model';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'multipart/form-data'})
};

@Injectable({
  providedIn: 'root'
})
export class OcrService {

  private fileUrl = 'http://localhost:8001/file/upload/';
  private explicacionUrl = 'http://localhost:8001/file/explicacion/?format=json';


  constructor(private http: HttpClient) { }


  addFile (orc: Ocr, api_token: string): Observable<Response> {


    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Authorization', api_token);
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    const fd = new FormData();
    fd.append('descripcion', orc.descripcion);
    fd.append('documento', orc.documento);
    fd.append('proceso', orc.proceso);
    if (orc.usuario) {
      fd.append('usuario', orc.usuario.toString());
    }

    console.log(orc);
    return this.http.post<Response>(this.fileUrl, fd, {headers: headers}  ).pipe(
      tap((res: Response) => this.log(`added file w/ id=${res}`)),
      catchError(this.handleError<Response>('addFile'))
    );
  }

  addFileJson (orc: JsonOcr): Observable<Response> {


    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');



    console.log(orc);
    return this.http.post<Response>(this.fileUrl, orc, {headers: headers}  ).pipe(
      tap((res: Response) => this.log(`added file w/ id=${res}`)),
      catchError(this.handleError<Response>('addFile'))
    );
  }



  postForm( body: Ocr) {
    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/form-data');
    headers.append('Accept', 'application/json');



    return this.http.post<Ocr>(this.fileUrl, body, {headers: headers }).pipe(
      tap((res: Ocr) => console.log(res) ),
      catchError(this.handleError<Ocr>('addFile'))
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

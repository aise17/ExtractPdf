import { Injectable } from '@angular/core';
import { catchError, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { IpFile } from '../models/IpFile.model';
import { Observable, of } from 'rxjs';
import { BonoUsuario } from '../models/Bonousuario.model';

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  
  private contactoUrl = 'http://' + environment.ip+ ':80/file/coor/';
  private bonosUsuariosbyYearUrl = 'http://' + environment.ip+ ':80/usuarios/bono_comprados_by_year/';


  constructor(private http: HttpClient) { }


  getCoordenadas( authorization: string): Observable<IpFile> {


    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    
    return this.http.get<IpFile>(this.contactoUrl, {headers: headers}  ).pipe(
      tap((res: IpFile) => this.log(`coordenadas recivido=${res}`)),
      catchError(this.handleError<IpFile>('error de recivo de coordenadas'))
    );
  }


  getRequesbyYear( authorization: string): Observable<BonoUsuario> {


    const headers = new HttpHeaders({"Authorization": "Bearer " + authorization});
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    
    return this.http.get<BonoUsuario>(this.bonosUsuariosbyYearUrl, {headers: headers}  ).pipe(
      tap((res: BonoUsuario) => this.log(`bonos de usuarios recivido=${res}`)),
      catchError(this.handleError<BonoUsuario>('error de recivo de bonos de usuario'))
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
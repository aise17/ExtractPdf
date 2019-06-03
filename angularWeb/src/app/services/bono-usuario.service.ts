import { Injectable } from '@angular/core';
import { of, Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { Contacto } from '../models/contacto.model';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { BonoUsuario } from '../models/Bonousuario.model';
import { environment } from 'src/environments/environment';
import { envi } from '../env';

@Injectable({
  providedIn: 'root'
})
export class BonoUsuarioService {

   
  private bono_usuarioUrl = 'http://' + envi.ip+ ':80/usuarios/comprar_bono/';


  constructor(private http: HttpClient) { }


  comprarBono(bono_usuario: BonoUsuario): Observable<Response> {


    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');


    console.log('bono usuario que se ba a enviar' +bono_usuario);
    return this.http.post<Response>(this.bono_usuarioUrl, bono_usuario, {headers: headers}  ).pipe(
      tap((res: Response) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Response>('error de envio de usuario'))
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

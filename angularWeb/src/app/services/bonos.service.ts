import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BonosService {


  private BonosUrl = 'http://' + environment.ip+ ':80/contenido/bonos';


  constructor() { }
}

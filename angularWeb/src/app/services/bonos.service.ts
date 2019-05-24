import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class BonosService {


  private BonosUrl = 'http://localhost:80/contenido/bonos';


  constructor() { }
}

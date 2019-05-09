import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class BonosService {


  private BonosUrl = 'http://localhost:8001/contenido/bonos';


  constructor() { }
}

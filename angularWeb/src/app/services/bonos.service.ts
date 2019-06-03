import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { envi } from '../env';

@Injectable({
  providedIn: 'root'
})
export class BonosService {


  private BonosUrl = 'http://' + envi.ip+ ':80/contenido/bonos';


  constructor() { }
}

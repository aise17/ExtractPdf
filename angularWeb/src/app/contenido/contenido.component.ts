import { Component, OnInit } from '@angular/core';
import { ContenidoService } from '../services/contenido.service';
import { Contenido } from '../models/contenido.model';

@Component({
  selector: 'app-contenido',
  templateUrl: './contenido.component.html',
  styleUrls: ['./contenido.component.css']
})
export class ContenidoComponent implements OnInit {

  constructor(private service: ContenidoService) { }
  public result: Contenido[];

  ngOnInit() {
    this.boton();
  }

  boton(): void {
    console.log('pulsado');

    this.service.getContenido()
      .subscribe(entrada => this.result = entrada);
      console.log(this.result);
  }


}

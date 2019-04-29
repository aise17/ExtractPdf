import { Component, OnInit } from '@angular/core';
import { Explicacion } from '../models/explicacion.model';
import { ExplicacionService } from 'src/app/services/explicacion.service';

@Component({
  selector: 'app-explicaciones',
  templateUrl: './explicaciones.component.html',
  styleUrls: ['./explicaciones.component.css']
})
export class ExplicacionesComponent implements OnInit {

  constructor(private service: ExplicacionService) { }
  public result: Explicacion[];

  ngOnInit() {
    this.boton();
  }

  boton(): void {
    console.log('pulsado');

    this.service.getExplicacion()
      .subscribe(entrada => this.result = entrada);
      console.log(this.result);
  }

}

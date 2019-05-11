import { Component, OnInit } from '@angular/core';
import { ContenidoService } from '../services/contenido.service';
import { Bonos } from '../models/bonos.model.';

@Component({
  selector: 'app-bonos',
  templateUrl: './bonos.component.html',
  styleUrls: ['./bonos.component.css']
})
export class BonosComponent implements OnInit {

  constructor(private service: ContenidoService) { }
  public result: Bonos[];

  ngOnInit() {
    this.getBono();
  }

  comprarBono(nombre){
      console.log('bono comprado -> ' + nombre)
  }


  getBono(): void {
    console.log('pulsado');

    this.service.getBonos()
    .subscribe(entrada => {
      console.log('resultado - >' + entrada['ok'])
      if (entrada['ok'] == true){
        this.result = entrada['salida'];
        console.log(this.result)
        console.log('Los bonos optenidos en la peticion son -> ' + this.result);


      }
    }); 
  }

}

import { Component, OnInit } from '@angular/core';
import { QuienSomos } from '../models/quienSomos.model';
import { QuienSomosService } from '../services/quien-somos.service';

@Component({
  selector: 'app-quien-somos',
  templateUrl: './quien-somos.component.html',
  styleUrls: ['./quien-somos.component.css']
})
export class QuienSomosComponent implements OnInit {

  public contenido: QuienSomos;

  constructor(public quienSomosService: QuienSomosService) { }

  ngOnInit() {
    this.getContenido();
  }

  getContenido() {
    this.quienSomosService.getContenido()
    .subscribe(res => {
      console.log(res);
      this.contenido = res[0];
    });
  }


}

import { Component, OnInit } from '@angular/core';
import { Contacto } from '../models/contacto.model';
import { ContactoService } from '../services/contacto.service';

@Component({
  selector: 'app-contacto',
  templateUrl: './contacto.component.html',
  styleUrls: ['./contacto.component.css']
})
export class ContactoComponent implements OnInit {
 
  public contacto = new Contacto();
  public entregado = false;
  is_progres: boolean;

  constructor(public contactoService: ContactoService) { }

  ngOnInit() {

  }



  sendEmail() {
    this.is_progres = true;
    if (sessionStorage.getItem('id')) {
      this.contacto.usuario = sessionStorage.getItem('id');
    }
    console.log(this.contacto);
    this.contactoService.sendEmail(this.contacto)
    .subscribe(res => {
      console.log(res['ok']);

        this.entregado = true;
        this.is_progres = false;
    });
  }
}

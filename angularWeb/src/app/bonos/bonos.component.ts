import { Component, OnInit } from '@angular/core';
import { ContenidoService } from '../services/contenido.service';
import { Bonos } from '../models/bonos.model.';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-bonos',
  templateUrl: './bonos.component.html',
  styleUrls: ['./bonos.component.css']
})
export class BonosComponent implements OnInit {

  constructor(private service: ContenidoService, public dialog: MatDialog) { }
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
    .subscribe(res => {
      console.log('resultado - >' + res['ok'])
      if (res['ok'] === true){
        this.result = res['salida'];
        console.log(this.result)
        console.log('Los bonos optenidos en la peticion son -> ' + this.result);
      }else if(res['ok'] === false){
        this.openDialogError(res['error'])
      }
    }); 
  }


  openDialogError(request): void {
    const dialogRef = this.dialog.open(DialogErrorComponent, {
      width: '250px',
      data: {error: request}
    });

    dialogRef.afterClosed().subscribe(result => {
     
        console.log('dialogo error cerrado')
      
    });
  
  }

}

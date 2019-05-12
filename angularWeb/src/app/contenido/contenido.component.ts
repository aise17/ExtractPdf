import { Component, OnInit } from '@angular/core';
import { ContenidoService } from '../services/contenido.service';
import { Contenido } from '../models/contenido.model';
import { MatDialog } from '@angular/material';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';

@Component({
  selector: 'app-contenido',
  templateUrl: './contenido.component.html',
  styleUrls: ['./contenido.component.css']
})
export class ContenidoComponent implements OnInit {

  constructor(private service: ContenidoService, public dialog: MatDialog) { }
  public result: Contenido[];

  ngOnInit() {
    this.getContenido();
  }

  getContenido(): void {
    console.log('pulsado');

    this.service.getContenido()
      .subscribe(entrada => {
        if(entrada !== undefined)
        this.result = entrada
        else{
          this.openDialogError('error al consegir contenido')
        }
      });
      console.log(this.result);
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

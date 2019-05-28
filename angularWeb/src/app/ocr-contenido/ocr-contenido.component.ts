import { Component, OnInit } from '@angular/core';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { Contenido } from '../models/contenido.model';
import { ContenidoService } from '../services/contenido.service';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-ocr-contenido',
  templateUrl: './ocr-contenido.component.html',
  styleUrls: ['./ocr-contenido.component.css']
})
export class OcrContenidoComponent implements OnInit {

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
